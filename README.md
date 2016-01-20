# pim

Managing `node` packages with `npm` is incredibly easy, which encourages modularity. In contrast, writing new `python` packages and publishing them with `pip` is kind of a pain, involving lots of boilerplate and configuration. 

`pim` is a light-weight CLI offering `npm`-like commands, but wrapping `pip` under the hood. Credit for this idea goes to Winthrop Gillis (@wingillis).

(doesn't do anything yet)

## API

####`init`
Initialize a package by answering some questions, will create the appropriate `setup.py` file.

####`publish`
Publish the package to PyPi. Will deal with any one-time configuration if neccessary.

####`install <package> --save`
Add this package to your project's `requirements.txt` file if not already present (doesn't call `pip`)

####`install <package> --global`
Install globally (equivalent to a `pip` install)

####`search <package>`
Search for a package on PyPi.
