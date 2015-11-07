# ppm

Managing packages with `npm` is incredibly easy, which encourages modularity. In contrast, writing new packages and publishing them with `pip` is kind of a pain, involving lots of boilerplate and configuration.

`ppm` is a light-weight CLI offering `npm`-like commands, but wrapping `pip` under the hood.

(DDAY - doesn't do anything yet)

## API

####`init`
Initialize a package by answering some questions, will create the appropriate `setup.py` file inside your package.

####`publish`
Publish the package to PyPi. Will deal with any one-time configuration if neccessary.

####`install <package> --save`
Add this package to your project's `requirements.txt` file

###`install <package> -g`
Install globally by calling `pip`

####`search <package>`
Search for a package on PyPi.
