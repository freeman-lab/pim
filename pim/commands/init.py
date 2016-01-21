import os
import getpass
import click
from click import echo
from clint.textui import indent, puts, prompt
from ..utils import write, retrieve, success

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

    d = {}
    d['name'] = prompt.query('name:', default=os.getcwd().split('/')[-1])
    d['version'] = prompt.query('version:', default='1.0.0')
    gitauthor = retrieve(['git', 'config', '--get', 'user.username'], default=getpass.getuser())
    gitemail = retrieve(['git', 'config', '--get', 'user.email'], default=getpass.getuser() + '@gmail.com')
    d['author'] = prompt.query('author:', default=gitauthor)
    d['email'] = prompt.query('email:', default=gitemail)
    gitrepo = 'https://github.com/' + d['author'] + '/' + d['name']
    d['repository'] = prompt.query('repository:', default=gitrepo, validators=[])
    d['readme'] = prompt.query('readme:', default='README.md')
    d['license'] = prompt.query('license:', default='MIT')
    d['package'] = prompt.query('package name:', default=d['name'].replace('-','_'))
    d['entry'] = prompt.query('entry point:', default='main.py')
    d['description'] = prompt.query('description:', default='', validators=[])
    
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
        write('requirements.txt', force=force)
        write('setup.py', fields=d, force=force)
        write('setup.cfg', fields=d, stringify=False, force=force)
        write('MANIFEST.in', fields=d, stringify=False, force=force)
        write('__init__.py', fields=d, folder=d['package'], force=force)
        write(d['entry'], folder=d['package'], force=force)
        echo('')

    success('Your package is initialized!')