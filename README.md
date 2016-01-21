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

## commands

###`pim init <options>`

Initializes a package by asking you some questions, and then creating the appropriate files, including `setup.py`, `setup.cfg`, `requirements.txt`, and a basic module layout.

Options
- `--force/--no-force` whether to overwrite existing files

###`pim publish <options>`
TODO Publish the package to PyPi. Will deal with any one-time configuration if neccessary.

###`pim install <package> --save`
TODO Add this package to your project's `requirements.txt` file if not already present (doesn't call `pip`)

###`pim install <package> --global`
TODO Install globally (equivalent to a `pip` install)

## Thanks

The idea for this initially came from Winthrop Gillis (@wingillis), and evolved through a discussion with @danielballan and @ericdill and others at PyData 2016.
