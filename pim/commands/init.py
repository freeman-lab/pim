import os
import click
import getpass
from clint.textui import puts, colored, indent, prompt, validators
from ..utils import write, retrieve

@click.command('init', short_help='initialize a project', options_metavar='<options>')
@click.option('--force/--no-force', default=False, help='Force overwrite existing files.')
def init(force):
    """
    Initialize a folder with typical contents for a python module.
    """
    puts('\nThis utility will help you set up a new python module for publishing on PyPi!\n')
    puts('After answering a few questions, it will create a few files.')
    puts('\nPress ^C at any time to bail!\n')

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
    # TODO add a package which is the name underscored
    d['entry'] = prompt.query('entry point:', default='main.py')
    d['description'] = prompt.query('description:', default='', validators=[])
    
    puts('\nReady to create the following files:')

    with indent(4, quote='  -'):
        puts('setup.py')
        puts('setup.cfg')
        puts('MANIFEST.in')
        puts(d['name'] + '/' + '__init__.py')
        puts(d['name'] + '/' + d['entry'] + '.py')
        puts('requirements.txt')

    finalize = prompt.yn('\nSound like a plan?', default='y')
    
    if finalize:
        # TODO use force
        write('requirements.txt')
        write('setup.py', fields=d)
        write('setup.cfg', fields=d, stringify=False)
        write('MANIFEST.in', fields=d, stringify=False)
        write('__init__.py', fields=d, folder=d['name'])
        write(d['entry'], folder=d['name'])