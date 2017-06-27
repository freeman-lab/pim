import os
import getpass
import click
from click import echo
from clint.textui import indent, puts, prompt
from ..utils import write, retrieve, success
from collections import OrderedDict
@click.command('init', short_help='initialize a project', options_metavar='<options>')
@click.option('--force', '-f', is_flag=True, help='Force overwrite existing files.')
def init(force):
    """
    This command initializes a folder with the typical contents of a Python package.
    After running this and writing your code, you should be ready to publish your package.
    """
    echo('\nThis utility will help you set up a new python module for publishing on PyPi!\n')
    echo('After answering a few questions, it will create a few files.')
    echo('\nPress ^C at any time to bail!\n')

    remap = {
        'entry': 'entry point',
        'package': 'package name'
    }
    d = _defaults()
    for k, v in d.items():
        d[k] = prompt.query('%s:' % remap.get(k, k), default=v)

    echo('\nReady to create the following files:')

    with indent(4, quote='  -'):
        puts('setup.py')
        puts('setup.cfg')
        puts('MANIFEST.in')
        puts(d['package'] + '/' + '__init__.py')
        puts(d['package'] + '/' + d['entry'])
        puts('requirements.txt')

    finalize = prompt.yn('\nSound like a plan?', default='y')

    if finalize:
        echo('')
        _make_package(d, force)
        echo('')

    success('Your package is initialized!')


def _defaults():
    """
    Get info from the host system and construct some reasonable defaults

    Returns
    -------
    dict
        A dictionary containing sensible defaults for the creation of a new
        package.  Keys are 'name', 'version', 'author', 'email', 'repository',
        'readme', 'license', 'package', 'entry', and 'description'
    """
    name = os.getcwd().split('/')[-1]
    author = retrieve(['git', 'config', '--get', 'user.name'], default=getpass.getuser())
    email = retrieve(['git', 'config', '--get', 'user.email'], default=getpass.getuser() + '@gmail.com')
    return OrderedDict([
        ('name', name),
        ('version', '1.0.0'),
        ('author', author),
        ('email', email),
        ('repository', 'https://github.com/' + author + '/' + name),
        ('readme', 'README.md'),
        ('license', 'MIT'),
        ('package', name.replace('-','_')),
        ('entry', 'main.py'),
        ('description', ' '),
    ])

def _make_package(d, force=False):
    """
    Make the actual package in the current directory

    Parameters
    ----------
    d : dict
        Dictionary containing the info needed to initialize the package
    force : bool, optional
        Overwrite files that already exist.
        Defaults to False.
    """
    write('requirements.txt', force=force)
    write('setup.py', fields=d, force=force)
    write('setup.cfg', fields=d, stringify=False, force=force)
    write('MANIFEST.in', fields=d, stringify=False, force=force)
    write('__init__.py', fields=d, folder=d['package'], force=force)
    write(d['entry'], folder=d['package'], force=force)
