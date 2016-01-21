# pim

`pim` is a light-weight command-line interface that makes it easy to initialize and publish Python packages. Under the hood, it wraps the standard python installation tool `pip`, but hopefully makes it easier to use.

Why? In javascript, managing `node` packages with the command-line tool `npm` is incredibly easy, which encourages modularity. In contrast, writing new Python packages and publishing them is kind of a pain, involving lots of boilerplate and configuration, and people often struggle to cobble together the neccessary info. The hope is that streamlining this process will encourage more people to publish resuable code!

## commands

###`pim init <options>`

Initializes a package by asking you some questions, and then creating

Options
- `--force/--no-force` whether to overwrite existing files

####`pim publish <options>`
Publish the package to PyPi. Will deal with any one-time configuration if neccessary.

####`pim install <package> --save`
Add this package to your project's `requirements.txt` file if not already present (doesn't call `pip`)

####`pim install <package> --global`
Install globally (equivalent to a `pip` install)

## Thanks

The idea for this initially came from Winthrop Gillis (@wingillis), and evolved through a discussion with @danielballan and @ericdill and others at PyData 2016.
