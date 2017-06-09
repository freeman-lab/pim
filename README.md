# pim

`pim` is a light-weight command-line interface for initializing and publishing Python packages, inspired by `npm`. Under the hood, it wraps the standard python installation tool `pip` along with `wheel` and `twine`, and hopefully makes it all easier to use, without inventing any new conventions.

Why? In javascript, managing `node` packages with the command-line tool `npm` is incredibly easy, which encourages modularity. In contrast, writing new Python packages and publishing them is kind of a pain. You have to remember lots of boilerplate and configuration and tooling, and redo it for every new package. The hope is that streamlining this process will encourage more people to publish resuable code! 

## example

Initialize a project
```
mkdir project
cd project
pim init
```

You'll be prompted with a set of questions, most of which will be pre-filled with sensible defaults, e.g.

```
name: [project]
version: [1.0.0]
author: [your-git-name]
email: [your-git-email]
repository: [https://github.com/your-git-name/project]
readme: [README.md]
license: [MIT]
entry point: [main.py]
```

Once it runs you'll have a folder layout that looks like:
```
project
├── project
│   ├── __init__.py
│   └── main.py
├── MANIFEST.in
├── requirements.txt
├── setup.cfg
└── setup.py
```

You can now add dependencies to your `requirements.txt` file (which will also be picked up by `setup.py`).

```
pim install boto requests
```

The `-g` flag will install the same package(s) into your environment using `pip`, which is convienient when you want the same package present in the same environment you are developing in.

You can similarly remove dependencies.

```
pim uninstall boto
```

Which will remove the package(s) from `requirements.txt`, and also uninstall from your environment with `-g`. With `install` and `uninstall`, you should never need to manually edit your `requirements.txt` file!

## commands

### `pim init --force[-f]`

Initializes a package by asking you some questions, and then creating the appropriate files, including `setup.py`, `setup.cfg`, `requirements.txt`, and a basic module layout.

Options
- `--force[-f]` whether to overwrite existing files

### `pim install <package(s)> --globally[-g]`

Add package(s) to your project's `requirements.txt` file, if not already present. With no arguments and the `-g` flag, will install everything in requirements into your environment.

Options
- `--globally[-g]` also install into your environment using `pip`

### `pim uninstall <package(s)> --globally[-g]`

Remove package(s) from your project's `requirements.txt` file, if it's present.

Options
- `--globally[-g]` also uninstall from your environment using `pip`

### `pim publish <options>`
TODO Publish the package to PyPi. Will deal with any one-time configuration if neccessary.

## credit

The idea for this initially came from Winthrop Gillis (@wingillis), and evolved through a discussion with @danielballan and @ericdill and others at PyData 2016. See the [list of collaborators](collaborators.md).

## license

[MIT](LICENSE)
