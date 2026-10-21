---
title: "Migrating from static HTMLs with i18n"
source_url: "https://www.drupal.org/docs/7/migrating-to-drupal/migrating-from-static-htmls-with-i18n"
page_type: page
last_updated: "Last updated on 21 November 2016"
published: "2014-10-11T15:03:04+00:00"
modified: "2016-11-21T20:40:14+00:00"
breadcrumb: ["Drupal 7", "Migrating to Drupal 7"]
fetched: "2026-10-21T06:55:04Z"
raw: "raw/docs/7/migrating-to-drupal/migrating-from-static-htmls-with-i18n.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Migrating from static HTMLs with i18n

Some key points in migrating static HTML pages to Drupal 7 with the full i18n (Internationalization) features incorporated are described.

Drupal's i18n feature is powerful and has great flexibility. However the flip-side of the coin is it is not that easy to understand how it works, partly because it heavily depends on your configuration. Also, it may not match well the suffix-based language negotiation by the Apache server for the static HTML pages, and so the migration of such static HTML sites to Drupal is not quite straightforward.

This document describes the general concepts and points to be aware of for building the i18n site on the emphasis of migration from the static HTMLs to Drupal.

Having said that, this is not a general description about the topic — the i18n features in Drupal vary greatly, depending on the configuration and preferences of site builders. Above all, I am rather a qualified novice of Drupal! On the other hand, some points beginners may often find hard to understand are likely to be explained, because, well, I have experienced a bucket load of those and banged wall countless times out of frustration, before making it right.

First, the migration module, `migrate_goo`, I have used is available from  
<https://github.com/masasakano/migrate_goo>  
`README.txt` in the repository explains all about it. Also, there are extensive comments written in the codes, particularly in the main code `allbutbook.inc.php`

It is by no means the generic module — or, there is no generic module for migration, nor generic i18n feature, after all, given how varied developers' demands are… But if migration to Drupal or i18n in Drupal is new to you as was to me, you can use it as a template and it may help you! At least I had experienced great difficulties, before I finally made it about right…

This document does not contain any code. Instead, it describes the points to be aware of, and the strategy to tackle with the problems on migration of HTMLs with i18n. For a specific example code, please have a look at [my code in Github](https://github.com/masasakano/migrate_goo).

## Which module should I use to migrate static HTMLs to Drupal?

In a word, anything that works for you!

As I understand, there are 3 major modules for migration:

- [import_html](https://www.drupal.org/project/import_html "import_html")
- [Feeds](https://www.drupal.org/project/feeds "Feeds")
- [Migrate](https://www.drupal.org/project/migrate "Migrate")

[import_html](https://www.drupal.org/project/import_html "import_html") is specialized for importing HTMLs, and is quite simple. [Migrate](https://www.drupal.org/project/migrate "Migrate") is the other end of the spectrum and offers a greatest flexibility, but with the price of somewhat complicated setup — in short you have to write your own child module, inherited from Migrate.

However, as I found out, the [import_html](https://www.drupal.org/project/import_html "import_html") module does not work well for the nodes that contain UTF-8 characters, hence for those international sites, it is not an option; See  
<https://www.drupal.org/node/2339097>

Besides, if you want to deal with the i18n properly, I am afraid there is no short-cut, you have to bite a bullet and tackle with the Migrate module. But don't worry, it is still a lot easier than the fully manual import! Among many features in Migrate, the rollback capability stands out; basically you can undo what you have done any time in just a few key-strokes. I suppose it is pretty common to repeat perhaps many trial-and-errors in developing/migrating the i18n-featured site. This rollback feature is what I found a blessing.

This document explains how to deal with it, using [Migrate](https://www.drupal.org/project/migrate "Migrate"), for one sample case. During my migration, I have inevitably tried out many other choices; even though they didn't work out well for me, some of them may suit your need, so I will describe about them whenever I can.

## <span id="What_features_import_static">Features to import from the static HTMLs</span>

The following is the list I have aimed and achieved.

- Import the main body. (Of course!)
- Preserve the creation/modification times.
- Preserve all the legacy URIs.
- Natural-language paths, as opposed to the node number, should be displayed as the URI.
- All the internal links between the imported files should work.
- Reproduce the i18n (internationalization) structure the original had, so the imported ones have a proper language code, as well as the Drupal language switcher incorporated.
- Make more modern-style URIs as default, while keeping the legacy ones with redirections.
- Preserve most Meta-tags and Link-tags information written in the header.
- Introduce an taxonomy, based on the top directory name.
- The original \<h1\> tag is deleted, with the element imported as the page title.
- Email addresses in the body are truncated.

## Modules required to be enabled

The following modules were essential to achieve the above-mentioned goals *for me*:

- path (core in Drupal 7)
- i18n (core; Internationalization, Field translation, Translation redirect)
- Taxonomy (core)
- [QueryPath](https://www.drupal.org/project/querypath "querypath module") module (A PHP Library to deal with the HTML tags)
- [Redirect](https://www.drupal.org/project/redirect "redirect module"): Essential to preserve the legacy URIs
- [Metatag](https://www.drupal.org/project/metatag "metatag module"): To hold the Meta-tag information
- [Link](https://www.drupal.org/project/link "link module"): To hold the Link-tag information
- [Context](https://www.drupal.org/project/context "context module"): To control the language-switcher for i18n
- [langnonecontext](https://github.com/masasakano/langnonecontext "langnonecontext module"): To add a custom context related to the language-switcher for the Context module, which I have ended up developing for this purpose.

What you need is entirely up to your demand! You may need a lot more or lot less or lot different.

## Other set-ups required before the migration

I set up as follows. In particular the i18n setting can vary a lot, depending on your demands. And I am afraid, if your setting is quite different from mine, my way of the migration may not work for you. But my template code is up for grabs anyway, so you can adjust as you like!

### Taxonomy

I prepared a new taxonomy for the imported HTMLs, so that it will be easy for me to categorize those nodes of HTML-files in Drupal after they are imported. The path of each HTML-file is anyway preserved, so this can be just redundant.

### Content type

I set up a new content type for the imported HTMLs. Obviously you can use an existing one, be it your custom one or standard one like Basic Page.

I can think of two major advantages to create the new content types.

1.  You can distinguish and handle those imported-HTMLs, based on the content type, separated from other contents in your Drupal site, when you need any post-migration adjustment or development,
2.  You can add any custom field. In my case, I added four:
    - Taxonomy field
    - Original Title: I set the node title with the original H1 header element, so I store the original title element here. I may use it in the future or not, but I think I had better keep it for now than lose it entirely, as I can delete them any time if needed, whereas it would be hard to regain once lost.
    - Original Filename: partially for debugging purpose,
    - Editor's Note: Comment and message during import, for debugging.

Whether you use a custom content type or existing one, make sure the language you are trying to import is defined and allowed for the content type. In particular if the language-neutral is set to be not allowed for the content type, you must set a language for every single node you are importing.

### <span id="Any_setup_need_before__i18n">i18n</span>

In `/admin/config/regional/language/configure` for the detection methods of languages, I have done the followings:

1.  Tick "URL" at least, or preferably all of them,
2.  For the "URL", set it as the path (directory), and not the domain,
3.  The weight (priority) for the "URL" must be the highest,
4.  For all the languages, including the default language, explicitly set the language code for the path, *e.g.*, "en" for English.

This is where people's preference vary… But my module is written on the basis of these settings.

### <span id="Any_setup_need_before__Permissions">Permissions</span>

Which user are you going to assign for the newly imported HTML-based nodes? The administrator (uid=1) is the easiest (as I chose), as whatever you do, none of your actions will be prevented due to the permission, though to be fair, it would be a double-edged sword. In my case, I needed a small piece of PHP code (to achieve one of the i18n features in Drupal) to be embedded in some HTMLs; that is not permitted to any user but the administrator in default.

If you assign any other user for creating the new node, make sure the user have a right permission for your job. Or, alternatively you can complete the job of migration as the administrator and later change the ownership of those imported nodes to a particular user, if you wish.

### Clean-up of the importing HTMLs

This is quite important.

Legacy HTMLs could have all sorts of cock-ups, particularly if they were hand-written, or edited by more than one person or software. Also, it is not uncommon they have a dirty rendering with the table tag etc or they have hard-coded navigation-bar type stuffs or even adverts. Another important point is the character code. Contents, particularly those in non US-English language, can have all sorts of character code, and they may not be even self-consistent, that is, the character code its HTML header declares may be different from the actual one. Even US-English contents could easily have some Windows-specific characters, which could break down the things in importing/migrating.

Personally I have preprocessed all the HTML-files with a separate script, and at the end of the script I ran the handy command-line tool `tidy` to guarantee the input HTMLs are legitimate, while converting the character code into UTF-8 and preserving the modification times of the files.

During migration/import you can do the clean-up job to some extent, or maybe to a great extent, in the php code of your migration module. But at least you may as well be aware if the character code is different from what you assumed, PHP may not behave as you expect.

The detail is beyond the scope of this document. I hope your files are not too evil…

## The i18n feature before and after

In my case, the following is the situation of i18n for the static HTML, which is basically based on the suffix-based language-negotiation of the Apache server. My aim is to reproduce the i18n feature in the Drupal-powered site after migration.

### Before (the static HTML-files)

- The main language of the site is Japanese.
- All the files are HTMLs.
- Most files are in Japanese only, but some have an English counterpart.
- There is no *orphan* English file, that is, English file without Japanese counterpart.
- The `lang` attribute of the `html` tag may or may not exist.
- English HTMLs have a suffix of either `.en.html` or `.en.us.html` without exception.
- Japanese HTMLs have a suffix of either `.jis.html` or `.jp.jis.html` or simply `.html` without exception.
- Index files may have in both Japanese and English, or Japanese only. There is no duplication of the filenames or directory names for the index files, that is, when there is a directory of `./info/`, there is no `./info.html` etc.
- Some files contain hard-coded language-switchers, namely hyper-link anchors, to another (internal) file in the other language.

### <span id="i18n_feature_before_after__After_Drupal_powered">After (in the Drupal-powered site)</span>

- The main language of the site is English, though have some Japanese contents.
- Imported HTMLs will consist of the main Japanese sections in the site, which are mostly independent of the English sections, but will merge into the English one gradually in the future. In other words, Japanese and English sections are not completely independent, and visitors can switch to view the versions in either language or section easily via the built-in language-switcher.
- The path aliases are enabled. Hence the nominal path is not a `/node/12345` type, but like `/info/foobaa.html`.
- The language-related suffix in the original HTML path is eliminated from the default path: *e.g.*, `info/foo.en.html` → `info/foo.html`.  
  The original path is redirected to the new one, if they differ.
- The defined (primary) paths for Japanese and English HTML files for the same content are identical, *e.g.*, both `info/foo.jis.html` and `info/foo.en.html` have the same path name of `info/foo.html`.
- The above means when a user accesses `/info/foo.html` in Japanese or English environment, the path s/he sees on the browser's address bar will be `/ja/info/foo.html` and `/en/info/foo.html`, respectively (the standard i18n behavior in Drupal, in the path-prefix preferred language-detection configuration).
- The directory is redirected to its index file: *e.g.*, `info` → `info/index.html`.
- The top directory in the legacy HTML-page site is transferred to the top directory in the new (Drupal) site. For example, `http://old.example.com/info/baa.en.html` will become `http://new.example.com/info/baa.html`. There is no crash of the names between the imported and existing top directories.
- The legacy home page for the HTML-page site is discarded, and a new one is created.
- The language of the imported node is set to be Neutral in default. However, if the node (of a Japanese page) has an English counterpart, the language is set to be *ja*, accordingly. The same goes for English pages (*en*).
- The language for the body is always set appropriately (*ja* or *en*), regardless of the language of the node.
- The (default Drupal) language-switcher is shown on a block (side-bar) whenever the node has a counterpart in the other language. If not, the language-switcher must not be shown. So, viewers can tell straightaway if the other language is available for the content or not.
- The hard-coded language switchers must work properly as they used to.

## <span id="Technical_flow_chart">Technical flow-chart</span>

Here is the outline (flow-chart) of the migration (importing) of the static HTML-files to Drupal 7 with the i18n feature, while preserving the legacy paths. I am sure there are other ways, and maybe ever better ways, but the following works (or worked for me).

I assume you have a basic understanding how the process of migration with the [Migrate](https://www.drupal.org/project/migrate "Migrate") module works.

1.  The migration is done in 2 steps (necessary to construct the i18n structure):
    1.  Process Japanese HTMLs class first, then
    2.  English ones class.
2.  Use `MigrateSourceList` class to define the HTML files to import.
3.  In `prepareRow()` the path of each file (aka row) is passed. With this:
    - gets all the required information from the header (manually coded, using `QueryPath` library),
    - gets the \<body\> element (again manually coded — easy one line with `QueryPath`!),
    - At the same time the hard-coded language-switchers in the HTMLs are replaced with the appropriate PHP code (that is I think the best way to achieve it).
    - also checks if the translation is available, based on the filename.
    - `tnid` (Translation Node-ID) is left undefined, aka language-neutral, in Japanese HTMLs at the time of processing of the Japanese HTMLs class.
    - `tnid` of Japanese nodes is set in `prepare()` while processing the English HTMLs class, where the relation between translation and source nodes is set.
4.  In `complete()` at the stage of processing each of the Japanese and English HTMLs classes, the redirection of the legacy URIs is set.

## <span id="Drupal_path_module">Drupal path module</span>

The path and i18n features, both of which are a part the core modules in Drupal 7, are heavily related to each other. First, let me recap how the Drupal path module works. If you already understand it well, skip this section to [the next one](#Drupal_i18n_features_path).

The default path to access a content in Drupal is via its unique node-ID with the URI like  
`http://example.com/node/12345`  
(hereafter referred to this type of the path as "**node-type path**", usually written without the domain part).

The node-type paths are very machine-like. Also, it is bad for the SEO (Search-Engine Optimization), which is not surprising, given this type of paths can well be one of a horde of machine-generated pages. Another potential downside is, it is less portable, because potential migration to any (CMS) system, including another Drupal system, can be problematic.

For the nodes of imported HTMLs, the node-type paths are even worse, because most internal hyper-links to a relative path hard-coded in the anchor tag in the HTML would not work if the node is called with the node-type paths like `/node/12345` . For example, when the hard-coded relative path is `./baa.html`, the browser interpret it as `/node/baa.html`. However, obviously there is no node with the path `/node/baa.html`, as any node-ID is by definition a number. Hence those links break (dead links).  
(There are exceptional cases where the relative path can work. Can you guess? — a little, if pointless, quiz for you.)

That is where the path module comes in handy. If the path module is enabled, you can set a more human-readable path of your preference for each node, such as, `/doc/about/about_myself` and open the node with the path. In this case,  
`http://example.com/doc/about/about_myself`  
(I hereafter refer to this type of paths as "**primary-path**", usually written without the domain part. The standard term for it in Drupal is "URL Alias", but in this case, where we also use `redirect` module, I thought this term might be a little confusing).

Note in setting the primary-path (aka URL Alias in the editing panel of a node), you should not insert the forward-slash at the beginning; for example, input  
`info/foo`  
as opposed to  
`/info/foo`  
The latter doesn't do any harm practically, apart from the fact the path will have a duplicated forward-slash. More importantly, do not include a trailing forward-slash at the end, as the path would not work.

I should note the original way of the node-type path like `/node/12345` is still valid, even after you set the primary-path, and is sometimes even useful for debugging purposes. Although the existence of multiple URIs for the same content can be penalised by search-engines, unless you make a hyperlink to those node-type paths from one of the public pages, the rest of the world, including search-engines, would not know its existence, so it has no impact for the rating by search-engines.

For your general information, the `pathauto` module is recommended, if you haven't installed and enabled it. It automatically generates a human-readable primary-path, when a new node is created, unless you specify your own. Hence, in many cases it saves a bit of your work. In our migration, you don't need it, as the primary-path for each node must be set, based on the directory and filename of its original HTML file.

## <span id="Drupal_i18n_features_path">Drupal i18n features with the path module</span>

Now, let's move on to a more complicated one, the i18n module.

I think the complication is not because Drupal's i18n feature is designed badly or something, but simply because the i18n is inherently complicated, as the site builders' preferences vary so widely! In particular, the i18n feature in Drupal may not well match the traditional suffix-based language negotiation system in the Apache server. So, if you are used to the Apache server's way for the static HTML-files, it may not be straightforward to grasp what Drupal does, and can be frustrating (as I experienced…). I am not knowledgeable enough to judge whether the Drupal's i18n feature is the best design or not. However I do understand why it is designed so as the generic module to satisfy the wide-range demands by different site builders.

To understand how the Drupal i18n module works is essential to make your site right, then to consider how you migrate the HTMLs to Drupal. In this section I explain it and how to work around in our migration.

Throughout this section, <span id="Drupal_path_i18n_features__Basic_i18n_module">I assume node-ID of 111 and 222</span> have the contents of English and Japanese, respectively. In Drupal, the node-ID is unique for each content page, and a translation of a node has always a separate ID from the original one (**source-language**; explained in detail in [the later section](#Drupal_path_i18n_features___information_translation)). So, to use a node-ID is the least confusing way to refer as to what content/node I am talking about.

### <span id="Drupal_i18n_features_path__What_language_website">What is the "language" of a website?</span>

The language of a page in a website has 2 meanings (at least):

- Language for the interface, like a menu bar,
- Language of the main content and information directly related to it, such as, the title.

In Drupal, the default language switcher changes both of the above, as long as the translation of the node is available.

### Language Neutral in Drupal

ISO 639 defines all the official language codes, which consist of the family part and optional sub-code. For example, the code for English is `en` and it can have a sub-code like `en-GB` and `en-US`. Drupal seems (at least from a user's point of view) not to distinguish the family but treats each of those language-codes as a different one; *e.g.*, `en-US` and `en-GB` are treated as entirely different languages, rather than varieties in the same family.

In addition to all those language codes, Drupal accepts the *language neutral*. In fact it is usually a default language, unless explicitly banned in the configurations, such as one in Content-Type. In practice, the *language neutral* in Drupal means all the languages or any language (though its constant variable name is `LANGUAGE_NONE`, which would in literal sense imply no language, as opposed to any language!).

In Drupal, every node has a property of a single language, which can be Neutral. Optionally (by enabling it in the i18n configuration), each field in a node can also have its own translation (I think...). But it is basically unrelated with the language of the node.

Also note the language of the node has nothing to do with the character set of the content, and can be set arbitrarily. It is possible (if confusing to any one) to set the language of a node as English, where the main content uses only Japanese characters, and vice versa.

### Language-dependent access

Here I assume the detection methods of languages (in `/admin/config/regional/language/configure`) is configured as described [in a previous section](#Any_setup_need_before__i18n). What you see when you access a path depends on what the Drupal server determines as the language to show, and it depends on the configuration, hence the following description may not be applicable partially or almost entirely, if the i18n configuration of your site is different.

#### Access via a node-type path

First, a node is always viewable via the node-type path like `/node/222` (Japanese, [as assumed above](#Drupal_path_i18n_features__Basic_i18n_module)). The language for the interface can be different, determined with the configurations and environments of both the site and visitors. If the node is accessed with the language-code prefix like `/ja/node/222`, the language of the interface will follow the prefix — Japanese (ja) in this example (again, providing the configuration is [set as described](#Any_setup_need_before__i18n)).

#### <span id="Drupal_i18n_features_path___Access_language_neutral">Access to a language-neutral node</span>

Now, if the language of a node is set to be neutral, the node can be accessed and viewed with the primary-path (say, `/info/foo_neutral.html`) in any (language) environment. When a user accesses a language-netural node like `/info/foo_neutral.html`, the (Drupal default) language-switcher, if provided, shows the following characteristics:

- hyperlinks to any other language except for the current one look active (though you can click even the current language),
- by clicking a language link, the language-prefix is added to the head of the path, and
- the language of the interface like a menu bar changes accordingly.

#### <span id="Drupal_i18n_features_path___Access_specific">Access to a specific-language node via the primary-path</span>

On the other hand, if the language of a node is set to be a specific one, like English or Japanese, how does it behave? When you access such a node with the primary-path, **HTTP 404 ("Page not found") will be returned** if the language of the node does not match what the Drupal server determines as your language (and if the node does not have the translations as explained in the following subsections).

This is one of the essential points in the Drupal i18n, and may surprise the uninitiated. If a visitor has been navigated to that page by following the internal links in your site, then as long as you have carefully constructed your website, taking care of the consistency of the language across the site, s/he either sees the page without trouble (as the language setting is right), or would not come to the page in the first place (due to the different language). No problem.

However, if some one visits the same page directly from outside, maybe from a search engine, or through the URI you have advertised somewhere, they may encounter the HTTP 404, depending on their language setting (which they themselves may not be even aware of!). Site-builders of Drupal i18n websites had better be careful on this point.

Now, if such a node is opened successfully, the entire language-setting will be the language of the node, including the interface (*n.b.*, in contrast, in the case of language-neutral, the language of the content can be different from that of the interface). If the default language-switcher is provided, the hyperlinks to the other languages are *struck* down, and are not available (to click).

#### <span id="Drupal_i18n_features_path___Access_translated">Access to a translated specific-language node via the unique primary-path</span>

Next, a story is getting a little more complicated, though this is unavoidable given you have the same contents in more than one language…

In Drupal, each node can have its counterparts in another language(s) registered (the detailed internal mechanism explained in [the later section](#Drupal_path_i18n_features___information_translation)). Those counterparts are called *translation(s)* in Drupal. Note the Drupal of course does not check whether the contents are a valid *translation* or not — it is up to you (or any *eligible* user) who decides which node is the translation of which. The *translation* can be a completely unrelated article, if you want.

Suppose you have two nodes in English and Japanese, each of which is the translation of the other, as registered to your Drupal server, and suppose they have their own primary-path set as,

- Node 111 (English): `/info/foo_en.html`
- Node 222 (Japanese): `/info/baa_ja.html`

When you access a node via its primary-path (say, `/info/baa_ja.html`), if the language of the node (Japanese in this case) agrees with what Drupal determines as your language, the node is shown as expected. If a default language-switcher is provided, and if the translation of the node is available, visitors can switch to the translation of the node, which also changes the language of the interface, the same as in [the previous section](#Drupal_i18n_features_path___Access_specific).

However, if the language of the node (Japanese in the case above) does not agree with what Drupal determines as your language, **HTTP 404 ("Page not found") will be returned**, because the node is not available in the language. If a default language-switcher is provided, it does show the hyperlink to the translation, so it is possible for the user to navigate to the translation, if s/he wants so and notices(!) the switcher.

If the hyperlink is embedded (hard-coded) in the body of the node, how it works may surprise you, though it is perfectly consistent, if you think how Drupal and browsers work. In short, it depends how the hyperlink is written, namely whether absolute or relative path, in the HTML source.

Suppose you are viewing a page at `/ja/other/index_ja.html`, the language of the node of which is Japanese. If the hard-coded anchor points to `/info/baa_ja.html`, it is the same as the above — it can return HTTP 404, depending what Drupal determines as your language. However, if the hard-coded anchor points to `../info/baa_ja.html` (remember the page you are viewing is under `/ja/other/` path), you will be guided to `/ja/info/baa_ja.html`, hence you are guaranteed to be able to view the page!

I should note one would never see the same (Japanese) page at the path of `/other/index_ja.html`, unless the site-default language is Japanese and the language-code prefix for the path for the default language is set to be null. It is different from the configuration I assume here, so I will skip that (you can guess what would happen, if interested — I leave it to you).

#### <span id="Drupal_path_i18n_features___Access_primary">Access to a primary-path shared with more than one language</span>

The next case to look at is that a primary-path is shared with multiple nodes, each of which has a different language and is registered as the *translation* in the Drupal server. This is actually very realistic to encounter in the migration of i18n static HTML sites.

In a word, it works exactly as the case in the [previous subsection](#Drupal_i18n_features_path___Access_translated), providing all the (default) options to detect the language with the default priority are set as [mentioned above](#Any_setup_need_before__i18n).

As an example, suppose the primary-path is set to be `/info/foo.html` for the nodes Node=111 and Node=222, and both of them are registered as the *translation* to each other. Then, each of them can be respectively accessed via,

- `/en/info/foo.html` (for English)
- `/ja/info/foo.html` (for Japanese)

When an user accesses `/info/foo.html`, which language-version is shown depends what Drupal determines about your language. Whether Drupal determines your language to be English or Japanese, it will not return HTTP 404. Also, the language-switcher, if shown, provides the way to navigate around the different language versions.

As a note, when setting the primary-path, the path should not include the language-code prefix; *e.g.*, **not** `ja/info/foo.html` but `info/foo.html` (for a Japanese node). If the former is set, it will break down in some cases, particularly when it is called from a hard-coded hyperlink in a node — the language-code can be duplicated in the path like `/ja/ja/info/foo.html` and accordingly **HTTP 404** will be returned in some cases.

### <span id="Drupal_path_i18n_features___information_translation">How Drupal holds the information about the "translation" of each node</span>

It actually depends on the context, for example, the mechanism for the translation of a node is different from that of a taxonomy. Here I explain only the former.

Whenever a node has a translation(s), one of them is defined as the source node for any translation. You can choose any language for the source-node among those registered in your Drupal site; it does not have to match the default language of the site (the node may not be available in the site-default language anyway!).

The single parameter to hold the relation of translation between the nodes is `tnid` (Translation Node ID?). It can be either 0, the node number `nid` of itself or of another node, as follows:

- **tnid=0** (`LANGUAGE_NONE`): Language-neutral (*und*).
- **tnid=nid (of itself)**: It is the source-node for the translation.
- **tnid=nid (of the source-node)**: It is a child-node for the translation.

### Note for the different i18n configurations

I have repeatedly mentioned the description is applied only when the i18n environment is configured as [mentioned above](#Any_setup_need_before__i18n). My choice of the i18n configuration was of course not a priori even for me, and there is a justification for me to have chosen it. Here I am describing some of the points for the different i18n configurations I understand. Which configuration suits you the best is entirely up to you and your preference/objective. I am just providing some selected information, which may be of some help for you in choosing the configuration.

#### No language code for the default language

In default, English is the default language of Drupal, and the language code for the path is undefined. It is understandable, because when visitors view those default-setting sites in the site-default language, there is no language-prefix at the head of the path, which you might feel is ugly. Indeed, for those who do not need the i18n feature, the language-code is of course unnecessary, and if they in the future enable the i18n module as the site develops, the null string for the default language-code will guarantee no breakage in the existing contents and features of the site.

However, this default setting with the null-string for the site-default language can lead to a confusing situation for developers (it took a long time for me to figure it out…). Here I explain why, and why I chose to set it explicitly in the end, that is, setting "en" for my site-default language, English.

Suppose the same situation as the subsection "[Access to a primary-path shared with more than one language](#Drupal_path_i18n_features___Access_primary)", that is, the primary-path is set to be `/info/foo.html` for the nodes Node=111 (English) and Node=222 (Japanese), and both of them are registered as the translation to each other. Then, they are respectively accessed via,

- `/info/foo.html` (for English)
- `/ja/info/foo.html` (for Japanese)

when the language-code for the path for the former (English) is undefined.

The Japanese version is exactly the same as the case that the language-code for the site-default language is defined. However, the case for English is different. In other words, there is an asymmetry between the languages. When a user accesses `/info/foo.html`, it will be always the English version and no HTTP 404, no matter what her/his preferred language in the browser preference is, because `/info/foo.html` is the proper (and sole, apart from the node-type) path for the English version.

Any other trick to try to display the Japanese version with the path of `/info/foo.html`, such as, adding the session parameter of `?language=ja`, would not work, either, because the URI-based method is set to be given the highest priority in determining the user's language.

If the hyperlink to that path is included in one of the Japanese pages as a relative path, the hyperlink works well, because the user must have opened the page with the path prefixed with `/ja/`, hence the hyperlink to that path naturally follows that with the top directory of `/ja/`, hence clicking the hyperlink will bring up `/ja/info/foo.html`, which is probably the expected behaviour (Go back and read the subsection "[Access to a translated specific-language node via the unique primary-path](#Drupal_i18n_features_path___Access_translated)" if you are unsure why).

In particular, this can cause a serious trouble in migrating the legacy HTMLs, which depended on the Apache language-negotiation, as explained below.

Suppose the legacy static HTML site is configured to use the standard suffix-based language negotiation of the Apache server; when a user requests a path (file), the server will return the version of the file in what the server guesses is the user's preferred language, providing there are more than one version of the languages available for the path. For example, when a user requests `/info/foo.html`, whereas there are both `/info/foo.html.en` (English) and `/info/foo.html.ja` (Japanese) in the server, either of English or Japanese version of the page will appear, depending on the environment. Now you have imported those two files to Drupal, and defined the relation between the two files as the translations. If the language-code for the site-default language (English in this case) is null, `/info/foo.html` will never bring up the Japanese version. In other words, the migration fails to reproduce the feature in the original legacy site.

You can perhaps set the site-default language as Japanese and nullify its language-code for the path, ignoring the potential effect for the rest of your (English) site. Then, the visitors, whose preferred language of their browser is Japanese, will see the Japanese version of the page when they access `/info/foo.html`. But of course, English-preferring visitors would not get the English page, when they access `/info/foo.html`, which used to work fine in the legacy HTML site.

In short, if you want to reproduce the i18n structure of the legacy HTML sites as described above, you should not leave asymmetry between the languages in the Drupal site, but had better set the language-code path prefix for all the languages.

Then, `/info/foo.html` does not belong to the particular language any more, and so when a user accesses it, the language will be determined with the subsequent parameters set in the i18n configuration, that is, Session, User, Browser in this order in default.

#### Disabling the URL-based language determination

You can disable the language selection by Drupal based on the URL prefix entirely. For example, Google.com seems to decide the language of the page, depending on the user's browser's preference and where the accessed IP is located geographically (the latter is not included in the default Drupal i18n functionality). That is another way for sure.

Note that showing different contents for the same URI, just depending on user's setting or session parameters, can be bad for SEO, and be penalised in the rating by search engines, allegedly (though that is exactly what Google.com is doing!).

There is a bug in Drupal i18n reported at drupal.org:  
"[Language detection based on session doesn't work with URL aliases](https://www.drupal.org/node/1294946)".  
If you access a path with the session parameter, the URL aliases of the path module do not work as of October 2014. For example, if you access to `/info/foo.html?language=ja` it will bring up a path like `/node/222` .

## <span id="Drupal_i18n_migration_HTMLs">Drupal i18n and migration of HTMLs</span>

Finally!

Here I am describing how I have done that. There must be countless preferences for the i18n settings and how you migrate. So, this is just an example.

### Which language to be set for nodes?

As summarised in the list in a [previous section](#i18n_feature_before_after__After_Drupal_powered), I set the language of the imported node as Neutral in default, but if the node has the translation, the language of the node is set to be so accordingly.

To set the language appropriately for the nodes with translation, as well as to register their relation as translation, is mandatory to activate the i18n feature in Drupal. However if the language of a node is set to be something specific (like Japanese), and if the node does not have a translation to another language (say, English), the page will not show up and return HTTP 404, when English-preferring visitors access the generic URI of the Japanese node without the language-code path prefix. I have no reason to prevent (or make awkeard) those English-preferring visitors from viewing my Japanese contents, particularly given they are anyway very likely to know the contents will be in Japanese before accessing the node (as that is how the legacy HTML site was built).

The way to prevent those annoying HTTP 404 is to make the node language-neutral.

This means the code in my migration module must set the language of each node, judging whether the translation exists or not.

### How to set tnid during migration from the static HTMLs

The most important thing in i18n is to register the translations between the created nodes, imported from the HTML files, to Drupal, that is, to set `tnid` of each node appropriately.

It is not quite straightforward, because you don't know the node-ID of each node (HTML-file) before importing. It is possible to assign a specific node-number to each HTML-file in migration and to have a total control over node-ID and `tnid`, if you want. But if you do that, you must be aware of potential crash of node-numbers with existing nodes, and moreover, your code must somehow remember the relation between each node-number and HTML-file. A fairly complicated stuff.

Unlike migration from a database (for a CMS), one thing the migration from the static HTML does not care is a node-ID number. Then you may as well leave the job of numbering of node-IDs to Drupal, unless you are planning some post-migration processing based on the node-IDs.

One of the ways to assign `tnid` is,

1.  Migrate the HTMLs in the source language first, Drupal assigning a node-ID to each of them,
2.  Migrate the translation HTMLs then, where
    - setting the `tnid` of those, referring to the node-ID of the source-language HTMLs in your Drupal database,
    - modifying the `tnid` of the source-language nodes that have a translation, to point to its own node-ID.

More detail is explained in the [Technical flow-chart](#Technical_flow_chart) section, and the [full-source code of my case](https://github.com/masasakano/migrate_goo) is available at GitHub.

### (Drupal default) Language-switcher

A language-switcher block is available in default in Drupal (or, there are other user-contributing modules for it as well). The default one is fairly basic, but does I think a good job. It provides the hyperlink to the translation of the node to another language(s), if available. If not, the word of the unavailable language is struck so the users know there is no translation available. Nice.

So I decided to show the language-switcher in the imported pages (in a side-bar). The legacy HTML pages have some hard-coded anchors to the translation when available. But the default language-switcher block would give more unified taste and convenience across the site. Nice.

A thing is, the language in the website has at least two meanings, as explained in the [previous section](#Drupal_i18n_features_path__What_language_website), namely that of the interface and of main body of the node.

In my case of migration, the language of all the imported nodes that have no translation is set to be neutral. That means practically, in all the imported pages, both the languages (English and Japanese) look available in the language-switcher. Because, when the language of the node is neutral, the hyperlink to the other language merely changes the language of the interface (see [a previous section](#Drupal_i18n_features_path___Access_language_neutral) for detail), whereas when the node has a translation, the hyperlink to the other language is the link to the translation. It is no good. The language-switcher has a double meaning in this case. And, users could not tell if the translation is available or not before they click the hyperlink to the other language in the language switcher (and most likely find no success, as a vast majority of the imported nodes have no translation).

A solution would be to find a, or develop my own, language-switcher, which clearly distinguishes the two meanings of the languages of the site. Another (easier) way is simply to disable (not show) the language-switcher in those language-neutral nodes; then users can tell if the translation (or strictly speaking, the content of the same context in the other language) is available or not for the node they are browsing.

I took the latter approach; I used the two-tier system to implement the feature, configuring as follows (I am using the default Block module of Drupal 7):

1.  **Block**: Language-switcher is enabled in default except for the paths for the nodes of the imported HTMLs,
2.  **Context**: Language-switcher block is added, when the language of the node is **not** neutral.

Unfortunately, the context for "not language-neutral" is unavailable in default (See [https://www.drupal.org/node/2351335](http://www.drupal.org/node/2351335)). So I have developed the little module (`langnonecontext`) for it, and used the implemented context in the [context](https://www.drupal.org/project/context "context module") module:  
<http://github.com/masasakano/langnonecontext>

### <span id="Drupal_i18n_migration_HTMLs__Language_switcher_anchors">Language-switcher anchors hard-coded in HTMLs</span>

In the suffix-based language-negotiation system in the Apache server, when a user request a full filename, like `index.html.en`, the web server returns the node in the language specified. This path (filename) can be used as an anchor from any of the HTML files.

The default Drupal i18n configuration (as [mentioned above](#Any_setup_need_before__i18n)) is similar, except the language-code is the prefix as the root path.

Unfortunately they don't match well. Think of the case the anchor points to the translation as the relative path in a HTML; *e.g.*, the anchor to `./index.html.en` embedded in the file `/info/uk/index.html.ja`. If the anchor is in the form of an absolute path, it is simpler, but still needs rewriting of the path to switch the language in Drupal.

To make the long story short, I have solved this problem by replacing all those anchor tags that points to a relative URI of a file in the different language with a small PHP code, which on the fly create the absolute path with the language-code prefix. For the absolute path, the language-code prefix is added at the head of the hard-coded path. My migration script does these during the processing, when it reads each HTML and extracts the required information from it.

Note the user (author) assigned to those imported nodes must be [given a permission](#Any_setup_need_before__Permissions) to include the PHP code in the body of the node.

See my code in [my module](https://github.com/masasakano/migrate_goo) for detail; the corresponding part is commented well.

### <span id="Drupal_i18n_migration_HTMLs__Redirection_i18n">Redirection and i18n</span>

To keep some legacy URIs in the Drupal site, I use the [Redirect](https://www.drupal.org/project/redirect "redirect module") module to redirect those legacy URIs to the corresnpoinding primary-path. I have introduced the more modern style URI as the primary-path. In short, the language-related suffix in the original HTML path (*e.g.*, `/ja`) should be eliminated and the directory-type paths be redirected to their corresponding index file, as summarised in [a previous section](#i18n_feature_before_after__After_Drupal_powered).

An example of the latter is, `/info` → `/info/index.html`. I should note the other way around (*e.g.*, `/info/index.html` → `/info`) would not work well. The following explains why.

Suppose the primary-path is defined as `info/uk` (for the original filename of `/info/uk/index.html`). Note a trailing forward-slash must not be included as the primary-path. Then, a hyperlink anchored from `/info/uk` (*i.e.*, `/info/uk/index.html` in the legacy site) with a relative path of, say, `./baa.html`, is recognised by the users' browsers as `/info/baa.html`, as opposed to the correct `/info/uk/baa.html`. Therefore if a user tries to open the link by clicking the anchor, the browser sends a request of `/info/baa.html`, which will cause HTTP 404 — dead link. It is the correct interpretation for the browser. If the original path was `/info/uk/`, it would work as expected, but it is not the case in Drupal (path module).

To summarise the settings of the (primary-)path and redirections, the file like `/info/index.jis.html` (Japanese) requires the following three settings:

1.  **Primary-path**: `info/index.html`
2.  **Redirect 1**: `info/index.jis.html` → `info/index.html`
3.  **Redirect 2**: `info` → `info/index.html`

It is the same for the file `/info/index.en.html` (English), except in practice "Redirect 2" is not set while processing the file, because it would have been already set while processing `/info/index.jis.html`.

The other files than index files do not need the "Redirect 2". If the original file does not contain the language-related suffix, like `/info/france.html`, the "Redirect 1" is not needed, either, and the primary-path is all it needs.

[As discussed](#Drupal_path_i18n_features___Access_primary), the primary-path should never include the language-code prefix, and so should not the redirection. Also, the node-type path should not be used anywhere, including the redirection, [as discussed separately](#Drupal_path_module). That is why `info/index.jis.html` can not be set as a direct redirection to the Japanese version of the node like `/ja/info/index.html` or `/node/222`.

#### Summary of how the URI request works

A request to the URI of `info/index.jis.html` (Japanese index), where `info/index.en.html` (English index) also existed in the legacy HTMLs, works as follows:

1.  <span id="Drupal_i18n_migration_HTMLs__Redirection_i18n___summary__List1_1">If it is a direct request of the URI</span>,  
    *i.e.*, `http://example.com/info/index.jis.html`
    1.  Redirected to `http://example.com/info/index.html`
    2.  Redirected to either of the following two, depending on other factors, such as user's preference of the language,
        - `http://example.com/en/info/index.html` (English)
        - `http://example.com/ja/info/index.html` (Japanese)
2.  If it is an embedded anchor as a relative path in the body of the node,
    1.  <span id="Drupal_i18n_migration_HTMLs__Redirection_i18n___summary__List2_1">If the language of the current node is Japanese</span>  
        (*e.g.*, `http://example.com/ja/doc/gear.html`)
        1.  Interpreted by the browser as  
            `http://example.com/ja/info/index.jis.html`
        2.  Redirected to `http://example.com/ja/info/index.html` (Japanese)
    2.  If the language of the current node is English  
        (*e.g.*, `http://example.com/en/doc/gear.html`)
        - The anchor in the body must have been [replaced with a PHP code](#Drupal_i18n_migration_HTMLs__Language_switcher_anchors), which produces the hyperlink of the absolute path, `http://example.com/ja/info/index.jis.html`
        - Redirected to `http://example.com/ja/info/index.html` (Japanese)
    3.  If the language of the current node is language-neutral and
        1.  if the current path contains the language-code prefix, which must be `/ja/`, such as, `http://example.com/ja/doc/links.html`, (*n.b.*, this is expected, as long as the user has followed the internal links to come to the current path),
            - The same as [the case of a Japanese node](#Drupal_i18n_migration_HTMLs__Redirection_i18n___summary__List2_1), namely, the Japanese page is returned.

        2.  if the current path does not contain the language-code prefix (*e.g.*, `http://example.com/doc/links.html`),

            - The same as [the first item](#Drupal_i18n_migration_HTMLs__Redirection_i18n___summary__1), namely, either English or Japanese.

            *n.b.*, this is a fairly unlikely situation — the user must have somehow directly opened the URI of the current path, or jumped here directly from an external site.
