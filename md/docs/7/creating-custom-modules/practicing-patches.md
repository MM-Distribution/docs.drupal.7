---
title: "Practicing patches"
source_url: "https://www.drupal.org/docs/7/creating-custom-modules/practicing-patches"
page_type: page
last_updated: "Last updated on 21 September 2016"
published: "2011-04-21T17:31:10+00:00"
modified: "2016-09-21T18:04:23+00:00"
breadcrumb: ["Drupal 7", "Creating custom modules in Drupal 7"]
fetched: "2026-10-21T07:26:08Z"
raw: "raw/docs/7/creating-custom-modules/practicing-patches.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Practicing patches

**Main topic described: *Git***

So now you can write a simple Drupal module with tests. Congratulations! However, in the real world, it's rarely necessary to write your own Drupal module from scratch. In almost all cases, there's already a module that does what you need or close to it. If you develop new functionality for an existing module, or correct a problem, you'll want to make that available to the community.

In this section of the tutorial, you will have the opportunity to practice submitting a patch of your own and reviewing someone else's patch for a version of the module you have been writing. Let's say the module was published without the 'More' link, and you can offer that functionality. We'll use a special version of the module called 'Current content' instead of 'Current posts'. You can add it to the `http://example.com/sites/all/modules` folder in your development site without conflict with the 'Current posts' module you have been writing.

The task is to use Git, drupal.org's version control system, to clone the repository, make a branch, and after adding the 'More link' functionality, to roll a patch. If you come up with something beyond the 'More' link, add that, too. Then post your patch in the 'Current content' issue queue. Next, review one of the other patches in the queue on a different Git branch. If it works right, mark it Reviewed & Tested by the Community (RTBC). (For major patches, this status is hard to obtain, so be careful with it outside this sandbox.) If everyone that contributes a patch also reviews one, then your patch will be reviewed as well.

### Git access

The Drupal development community uses Git to manage all the revisions of every file that makes up the Drupal system. If you are not familiar with Git, you can read through some excellent documentation available on drupal.org, starting with the [Introduction to Git](http://drupal.org/node/991716). You'll need to have access to Git on your computer as well; see [Installing Git](http://drupal.org/node/1010894).

To use Git on drupal.org, you must have an account with the site and accept the 'Git access agreement', located in the 'Edit' tab of your user account in the tab, 'Git access.' See [Obtaining Git access](http://drupal.org/node/1047190) for detailed instructions, then proceed to [Identifying yourself to Git](http://drupal.org/node/1022156) to complete your setup.

### Cloning the repository

Now to get started making patches. First, visit the [Current content](http://drupal.org/project/current_content) sandbox. Follow the link at the top to the 'Version control', then fire up your terminal and enter the commands to clone the repository. (Instructions in this tutorial will be for command line access. If you are using a GUI, you'll have to convert these commands as needed.) If you clone the code into your `http://example.com/sites/all/modules` folder, you can check the functionality and run the tests.

### Make the patch

With Git, you can often find several somewhat different paths to end up at this same place. This is true of making patches. If you already have your own process and just want to practice, feel free to follow your own workflow. Here, we'll use branches so that we can both create and review patches without affecting the original cloned repo on master. If you have trouble with any of these instructions, see below for other options.

Create a new issue in the ['Current content' queue](http://drupal.org/project/issues/1128576?categories=All), in the category 'feature request'. Note the issue number, which is the final number in the issue's URL. Make a Git branch with the command:

``` php
git checkout -b more_patch-[issue-number]
```

`checkout` tells Git you are changing branches. `-b` means this is a new branch you are creating with this command, given the name that follows. You can call the branch whatever you like, but best practice suggests using the issue number to make sure you don't confuse it with other issues. We're including the word 'patch' here to distinguish this branch from the one you will make for review.

Now you can go to work on the .module file, using your editor of choice. As long as you are on the branch, you won't affect the code you cloned in the master branch. Add the 'More' link, along with the changes to the menu function, the page function, and `theme_item_list` in the block view function, just as you did in [Adding a 'More' link](http://drupal.org/node/1128278). Check them out in your development site. You can run the 'Current content' tests with the changes, and all should pass.

When you are satisfied with the changes, it's time to commit. Back in the terminal (or Git GUI), enter the following command:

``` php
git status
```

The status command should show that you are still on the branch with 'patch' in the name. It should also tell you that your .module file has changed and has not been staged. The next command:

``` php
git diff
```

This command serves as a final check of your changes. Make sure everything you wanted to include is there. If you have inadvertently included whitespace, Git will highlight it for you. Be sure you delete these spaces. Try to get everything right before you go to the next step. The goal is to get all your changes into a single commit.

When you are ready, stage your changes. The -A flag below will stage all new files, modified files, and deleted files:

``` php
git add -A
```

If you run `git status` now, it will list your file under 'Changes to be committed'. Now commit:

``` php
git commit -m "Issue #[issue number] by [your drupal.org username]: Added a 'More' link"
```

The commit message follows drupal.org's guidelines; see [Commit messages - providing history and credit](http://drupal.org/node/52287) for the full explanation. Next get the latest code in case something has changed:

``` php
git fetch origin
```

Git will give you messages that it is fetching and unpacking the objects from the 'Current content' repo on drupal.org. Next apply your changes over what you just fetched:

``` php
git rebase origin/master
```

You'll get messages about Git rewinding to HEAD and applying your changes. Now you are ready to make your patch file.

### Create the patch file

There are two ways you can roll the patch:

1.  **Only one commit.** If you completed all your changes in only one commit, you can use the `git format-patch` command to make a patch that will include your author information:  
    `git format-patch origin/master --stdout > added_more_link-[issue number]-[comment number].patch`Be sure not to use a hash mark (#) in the filename, or the testbot will not acknowledge the patch. (There may not be a testbot on the practice queue, but there will be if you make patches for core.)
2.  **Multiple commits.** If you made more than one commit, you can use `git diff`:  
    `git diff origin/master > added_more_link-[issue number]-[comment number].patch`

Of course, you can change the patch name if you like. And if you are writing patches for core, the version we use here, master, will be a core version number. For another module, it might also be different. If you make the patch before you create the comment, you can estimate the comment number.

Once you hit return on this command, Git will make the patch with no onscreen messages. You can find the file in the root directory of your current local Git repository. (This repo has only one directory, but if you patch against a repo with subdirectories, the patch will save in the top one.) Open it and inspect your work. If you used `git format-patch`, the patch will begin with 4 lines that include the commit hash, the name and email address of the person who made the patch, the date, and the commit message. If you used `git diff`, the patch will begin with the diff itself. If you made all the changes for the "More" link, you patch will include three sections, each beginning with line numbers and function names for the changes that follow.

Now return to the issue queue for 'Current content', upload your patch, and mark the issue 'Needs review.'

If you run `git status` now in the branch, you'll see the patch file is included. So that you won't accidentally including the patch file in future commits, remove it now with the Unix rm command:

`rm added_more_link-[issue number]-[comment number].patch `

### Reviewing a patch

Now that you have made a patch, time to review one for someone else. First choose a patch and click on its name-link to look at it. Make a note of the issue number.

Now return to your terminal and the `current_content` directory. Check the status:

`git status`

If you are not on the master branch, go there:

`git checkout master`

Next make sure you are still using the most recent version of the code:  
`git pull`

Make a branch for reviewing the patch:

`git checkout -b more_review-[issue number]`

There are several ways to download and apply the patch. If you want to use curl, see [Advanced patch contributor guide](http://drupal.org/node/1054616) under 'Reviewing patches'. We'll go with the Unix command `wget`:

``` php
wget http://drupal.org/files/issues/[patchname].patch
git apply -v [patchname].patch
```

Copy and paste the patch URL to make the download command painless. You'll get a lot of data when you download the patch. When you use the -v flag, you'll get a message telling whether or not the patch applied cleanly.

If you run `git status` now, you'll see the patch file is included. So that you won't accidentally including the patch file in future commits, remove it now with the Unix rm command:

`rm [patchname].patch `

View the code changes:

`git diff`

You can also view the altered file by opening it in an editor.

Now check out the patch. Since sandboxes do not include the testbot functionality, run the SimpleTest tests in your own site. Note what you tried, what did or didn't work, and write it up in the issue you chose. For details on how to review patches, see [Reviewing patches](http://drupal.org/patch/review).

If something went wrong while checking out the patch, change the issue status to 'Needs work'. If it worked right, change it to RTBC. **Note**: in a real issue queue, RTBC requires two or more people approving the patch. See [Status settings for an issue](http://drupal.org/node/156119) for details about when it's appropriate to change those status settings.

### Conclusion

Whew! You made it all the way to the end of this tutorial. If you have worked your way here from the beginning, you are now familiar with the hook system, block system, menu system, database system, form system, render arrays, page functions, several drupal functions, SimpleTest, and patching through Git.

Where to go from here? Explore what interests you in [Working with the Drupal API](http://drupal.org/developing/api) and the [Examples for Developers](http://drupal.org/project/examples).

### See also

- [Current content project](http://drupal.org/project/current_content)

- [Introduction to Git](http://drupal.org/node/991716)

- [Installing Git](http://drupal.org/node/1010894)

- [Obtaining Git access](http://drupal.org/node/1047190)

- [Identifying yourself to Git](http://drupal.org/node/1022156)

- Patch instructions

- - [Version control instructions for the 'Current content' repo](http://drupal.org/project/current_content/git-instructions)
  - [Patch workflows](http://drupal.org/node/707484)
  - [Advanced patch contributor guide](http://drupal.org/node/1054616)

- [Commit messages - providing history and credit](http://drupal.org/node/52287)

- [Reviewing patches](http://drupal.org/patch/review)

- [Status settings for an issue](http://drupal.org/node/156119)

- [Working with the Drupal API](http://drupal.org/developing/api)

- [Examples for Developers](http://drupal.org/project/examples)
