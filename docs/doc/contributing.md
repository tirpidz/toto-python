# Contributing

## Overview

There is many way to contribute, to a project, contributing is not just about creating new code lines. 

!!! warning
    Make sure to treat automation (scripts, documentation, examples, configurations, tests, etc...) with the same importance as you would good quality code.

## Be consistent

We value tidy codebase meant to be read & maintain by human being. Consistency is key, to `guarantee` consistency lets make sure we limit manual intervention and automate everything we can. In other words, **let's be lazy**.

## Contribute Documentation

This very documentation is part of our codebase this is probably the first thing users & other developers will see. Make sure it's accurate, precise up-to-date give documentation some love everyday. It could not be simpler, just edit some text `.md` file.

To see how to build this documentation see [Documentation](doc.md).

## Contribute Code

### Git usage

To keep git history clean and human readeable, we use as mush as possible `git rebase`.

Please take a moment to really understand what is happening with the rebase concept and the differences with classical merge.

Our main development branch is `main`, it is considered public, it is protected and will never be rebased !
The minimal setup you need to do is :

```bash
git config --global pull.rebase true
```

This will automatically rebase your changes in your branch when you pull (only happening if sharing a branch with a co-worker).
After that, the minimal workflow is the following :

```bash
# always start from the latest version of `dev` branch
git checkout dev
# fast forward to the latest version of dev
git pull origin dev
# create you branch (keep the name short and meaningful, not just issue number)
git checkout -b my-branch
git push origin my-branch
# click on the merge request link and start documenting what you intend to do (it will be in WIP mode automatically, life is beautiful)
...
# hack
git commit ...
git push ...
# hack
git commit ...
git push ...
# repeat
# when your work is ready or when you want to have your work "merge" with `dev`, do a little rebase
# again make sure you have the last version
git checkout dev
git pull origin dev
git checkout my-branch
git rebase dev
# it will reapply all you changes ontop of the lastest dev so you can test if everything is as you wish
```

Here is the minimal git 101 that everybody needs to understand before contributing: [git-guide](https://rogerdudler.github.io/git-guide/)
