---
title: "Writing upgrade path tests"
source_url: "https://www.drupal.org/docs/7/testing/writing-upgrade-path-tests"
page_type: page
last_updated: "Last updated on 4 January 2017"
published: "2012-02-05T14:05:06+00:00"
modified: "2017-01-04T19:27:14+00:00"
breadcrumb: ["Drupal 7", "Automated testing for Drupal 7"]
fetched: "2026-10-21T08:10:04Z"
raw: "raw/docs/7/testing/writing-upgrade-path-tests.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Writing upgrade path tests

This document explains how to write tests for the Drupal core upgrade path, including:

- Upgrading from one major version of core to the next (e.g., from 6.x to 7.x).
- Updating the minor version of core (e.g., from 7.10 to 7.12).

For Drupal 8, see:

- [Migrate API in Drupal 8](https://www.drupal.org/node/2127611) - used for migrating between major versions, such as between Drupal 6.x and 8.x or 7.x and 8.x.
- [Update API in Drupal 8](https://www.drupal.org/node/2535316) - used for migrating within a major version (within Drupal 8).

## Upgrade tests need database dumps

Upgrade tests are "normal" tests in every way except they don't start off with a fresh Drupal installation. They need a database dump of an older Drupal version to be imported first. Review the existing upgrade path tests:

- [Drupal 6 -\> 7 and 7.0 -\> 7.x upgrade](http://drupalcode.org/project/drupal.git/tree/refs/heads/7.x:/modules/simpletest/tests/upgrade) tests

The database dumps are PHP files that use the Drupal database API to create the expected schemas and data in the backend. Examples:

- [drupal-6.bare.database.php](http://drupalcode.org/project/drupal.git/blob/refs/heads/7.x:/modules/simpletest/tests/upgrade/drupal-6.bare.database.php) contains a large dump of schemas but does not contain much data.
- [drupal-6.comments.database.php](http://drupalcode.org/project/drupal.git/blob/refs/heads/7.x:/modules/simpletest/tests/upgrade/drupal-6.comments.database.php) contains data specific to comment testing.

A test can later use any one of these dumps and can even load a series of these dumps to test the system with a more complex setup. See below for more information.

The database dumps can be compressed with gzip, but that is not a requirement. Drupal 7 mostly uses plain PHP files. At the moment of this writing, Drupal 8 only uses .gz compressed files. The gzip compressed files are harder to diff but are smaller in the checkout / release.

## Creating database dump files for tests

The database dump files are PHP files using the Drupal database API to create the expected schema and import the required data. The files can be generated from an installed Drupal database using scripts included in Drupal core.

### Steps to create a database dump

1.  **Check if a suitable component dump for your update exists** in either the [Drupal 7 upgrade tests](http://drupalcode.org/project/drupal.git/tree/refs/heads/7.x:/modules/simpletest/tests/upgrade) or the [Drupal 8 upgrade tests](http://cgit.drupalcode.org/drupal/tree/core/modules/system/tests/fixtures/update?h=8.3.x) (as appropriate).

    - If a suitable database dump exists, install Drupal using that dump. (In many cases, you can simply See [klausi's blog](http://klau.si/installation-drupal-upgrade-path-test-db) for one method of accomplishing this.)
    - If no suitable dump exists, or if you are adding additional tests using an existing profile, install the pre-upgrade version of Drupal normally.

2.  **Configure Drupal with the minimum changes needed for your test**. For example, if you are adding tests for a particular module, enable and configure that module.

3.  **Use the appropriate shell script to generate a new database dump**:

    - For Drupal 7 -\> 8, use `core/scripts/dump-database-d7.sh`
    - For Drupal 6 -\> 7, use `scripts/dump-database-d6.sh`

4.  **Add your database dump to your patch**.

    - If you are creating a new file, add the file to your patch using `git add`.
    - If you are updating an existing dump, be sure to include only the necessary changes to the dump file. You should manually copy these changes from your generated file to the existing file.
    - If the dump you need to update is gziped, ungzip the dump, apply your changes, and gzip the dump again. You **must** use `git diff --binary` to include the changes in the zipped file.

    Note that you can add tests for additional modules by using an existing full dump and creating a second file that contains only the data relevant to your module. For example, see [drupal-6.comments.database.php](http://drupalcode.org/project/drupal.git/blob/refs/heads/7.x:/modules/simpletest/tests/upgrade/drupal-6.comments.database.php). This dump relies on [drupal-6.filled.database.php](http://drupalcode.org/project/drupal.git/blob/refs/heads/7.x:/modules/simpletest/tests/upgrade/drupal-6.filled.database.php) to install Drupal, and then simply adds additional comment data for testing.

### Shell script for creating fresh database dumps

This shell script assumes you have [Drush](http://drupal.org/project/drush) available. Installation instructions are available in the Drush [README.txt](http://drupalcode.org/project/drush.git/blob/HEAD:/README.txt) file.

``` php
# Remove any previous installation of Drupal in the drupal-dumps directory. 
rm -rf drupal-dumps/drupal

# Download the latest D7, place it in 'drupal-dumps' directory,
# rename the downloaded directory 'drupal'.
drush dl drupal-7.x --destination=drupal-dumps --drupal-project-rename=drupal

cd drupal-dumps/drupal

# Install Drupal site using the standard profile
# and create an SQLite database.
drush site-install -y standard --account-name=admin --account-pass=drupal --db-url=sqlite:./.ht.drupal.sqlite

# enable all core modules
drush pml --core --status="not installed" --pipe | xargs drush en --yes

# Create a database dump of the empty Drupal site.
php scripts/dump-database-d7.sh > ../drupal-7.bare.database.php

# Generate content in the Drupal site.
php scripts/generate-d7-content.sh

# Create a database dump of the Drupal site.
php scripts/dump-database-d7.sh > ../drupal-7.filled.database.php
```

## Writing upgrade tests for 7.x

### Extending the test class from UpgradePathTestCase

To build on the existing utility functions (to make loading database dumps, running the update.php script, etc. easy), you should extend your test class from the base upgrade path class and provide the getInfo() method as usual like any other test class.

- For **major version upgrades** (e.g. Drupal 6 -\> Drupal 7), extend `UpgradePathTestCase`.
- For **minor version upgrades** (e.g. Drupal 7.0 -\> 7.x), extend `UpdatePathTestCase`.

Take this [upgrade.comment.test example from Drupal7](http://drupalcode.org/project/drupal.git/blob/refs/heads/7.x:/modules/simpletest/tests/upgrade/upgrade.comment.test):

``` php
/**
 * Tests the upgrade path for the Comment module.
 */
class CommentUpgradePathTestCase extends UpgradePathTestCase {
  public static function getInfo() {
    return array(
      'name'  => 'Comment upgrade path',
      'description'  => 'Comment upgrade path tests.',
      'group' => 'Upgrade path',
    );
  }

  // ...
}
```

### Writing the setUp() method for the upgrade test case

A test can use any one of the existing dumps and can even load a series of dumps to test the system with a more complex setup. As mentioned above, [upgrade.comment.test](http://drupalcode.org/project/drupal.git/blob/refs/heads/7.x:/modules/simpletest/tests/upgrade/upgrade.comment.test) loads both the filled database dump and its own comments database dump to prepare the environment:

``` php
  public function setUp() {
    // Path to the database dump files.
    $this->databaseDumpFiles = array(
      drupal_get_path('module', 'simpletest') . '/tests/upgrade/drupal-6.filled.database.php',
      drupal_get_path('module', 'simpletest') . '/tests/upgrade/drupal-6.comments.database.php',
    );
    parent::setUp();
   // ...
  }
```

### Adding test methods to the upgrade test case

Once the upgrade test's `setUp()` method imports its database dump from the dump PHP files, test methods can be written much the same as functional tests. However, make sure you perform the upgrade in your test function and/or make any data adjustments before the upgrade is performed as needed. There are plenty of examples in the [upgrade.locale.test](http://drupalcode.org/project/drupal.git/blob/refs/heads/7.x:/modules/simpletest/tests/upgrade/upgrade.locale.test) test.

``` php
  /**
   * Tests an upgrade with path-based negotiation.
   */
  public function testLocaleUpgradePathDefault() {
    // LANGUAGE_NEGOTIATION_PATH_DEFAULT.
    $this->variable_set('language_negotiation', 1);

    $this->assertTrue($this->performUpgrade(), 'The upgrade was completed successfully.');

    // The home page should be in French.
    $this->assertPageInLanguage('', 'fr');

    // The language switcher block should be displayed.
    $this->assertRaw('block-locale-language', 'The language switcher block is displayed.');

    // The French prefix should not be active because French is the default language.
    $this->drupalGet('fr');
    $this->assertResponse(404);

    // The English prefix should be active.
    $this->assertPageInLanguage('en', 'en');
  }
```

The \$this-\>performUpgrade() part is what is going to make the upgrade run, so you get an upgraded environment for your test method. Here we set a different negotiation setting before running the upgrade so we can test the upgrade against that.
