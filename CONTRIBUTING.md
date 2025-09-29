# Contributing to xCloud MCP Server

First off, thank you for considering contributing. It's people like you that make the open source community such a great place.

## Where do I go from here?

If you've noticed a bug or have a feature request, [make one](https://github.com/PageCloudv1/xcloud-mcp/issues/new)! It's generally best if you get confirmation of your bug or approval for your feature request this way before starting to code.

### Fork & create a branch

If this is something you think you can fix, then [fork xCloud MCP Server](https://github.com/PageCloudv1/xcloud-mcp/fork) and create a branch with a descriptive name.

A good branch name would be (where issue #325 is the ticket you're working on):

```sh
git checkout -b 325-add-japanese-translations
```

### Get the test suite running

Make sure you're running the tests before you start making changes.

### Implement your fix or feature

At this point, you're ready to make your changes! Feel free to ask for help; everyone is a beginner at first 😸

### Make a Pull Request

At this point, you should switch back to your master branch and make sure it's up to date with xCloud MCP Server's master branch:

```sh
git remote add upstream git@github.com:PageCloudv1/xcloud-mcp.git
git checkout master
git pull upstream master
```

Then update your feature branch from your local copy of master, and push it!

```sh
git checkout 325-add-japanese-translations
git rebase master
git push --force-with-lease origin 325-add-japanese-translations
```

Finally, go to GitHub and [make a Pull Request](https://github.com/PageCloudv1/xcloud-mcp/compare)

### Keeping your Pull Request updated

If a maintainer asks you to "rebase" your PR, they're saying that a lot of code has changed, and that you need to update your branch so it's easier to merge.
