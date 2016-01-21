# pim

`pim` is a light-weight command-line interface that makes it easy to initialize and publish Python packages. Under the hood, it wraps the standard python installation tool `pip`, but hopefully makes it easier to use.

Why? In javascript, managing `node` packages with the command-line tool `npm` is incredibly easy, which encourages modularity. In contrast, writing new Python packages and publishing them is kind of a pain, involving lots of boilerplate and configuration and  tooling. The hope is that streamlining this process will encourage more people to publish resuable code!

## example

Initialize a project
```shell
mkdir my-project
cd my-project
pim init
```

You'll be prompted with a set of questions, most of which will be pre-filled with sensible defaults, e.g.

```shell
name: [my-project]
version: [1.0.0]
author: [your-git-name]
email: [your-git-email]
repository: [https://github.com/your-git-name/my-project]
readme: [README.md]
license: [MIT]
entry point: [pim.py]
```

## commands

####`pim init <options>`

Initializes a package by asking you some questions, and then creating the appropriate files, including `setup.py`, `setup.cfg`, `requirements.txt`, and a basic module layout.

Options
- `--force/--no-force` whether to overwrite existing files

#####`pim publish <options>`
Publish the package to PyPi. Will deal with any one-time configuration if neccessary.

#####`pim install <package> --save`
Add this package to your project's `requirements.txt` file if not already present (doesn't call `pip`)

#####`pim install <package> --global`
Install globally (equivalent to a `pip` install)

## Thanks

The idea for this initially came from Winthrop Gillis (@wingillis), and evolved through a discussion with @danielballan and @ericdill and others at PyData 2016.
