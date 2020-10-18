# How to contribute

globd is Apache 2.0 licensed and accepts contributions via Github pull requests. This document outlines some of the conventions on commit message formatting, contact points for developers and other resources to make getting your contribution into globd easier.  Portions of this document are an excerpt from the [etcd contribution guide](https://github.com/coreos/etcd/blob/master/CONTRIBUTING.md).

## Getting started

- Fork the repository on GitHub
- Read the README.md for instructions

## Contribution flow

This is a rough outline of what a contributor's workflow looks like:

- Create a topic branch from where you want to base your work. This is usually
  `main`.
- Make commits of logical units.
- Make sure your commit messages are in the proper format (see below).
- Push your changes to a topic branch in your fork of the repository.
- Submit a pull request to sag47/globd.

Thanks for your contributions!

### Code style

The coding style suggested by the Python community is used in globd.  See [Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008) for details.

Please follow this style to make globd easy to review, maintain, and develop.

### Format of the Commit Message

We follow a rough convention for commit messages that is designed to answer two
questions: what changed and why. The subject line should feature the what and
the body of the commit should describe the why.

```
scripts: add the test-cluster command

this uses tmux to setup a test cluster that you can easily kill and
start for debugging.

Fixes #38
```

The format can be described more formally as follows:

```
<subsystem>: <what changed>
<BLANK LINE>
<why this change was made>
<BLANK LINE>
<footer>
```

The first line is the subject and should be no longer than 70 characters, the
second line is always blank, and other lines should be wrapped at 80 characters.
This allows the message to be easier to read on GitHub as well as in various
git tools.
