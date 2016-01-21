import os
import getpass
import click
from click import echo
from clint.textui import indent, puts, prompt
from ..utils import write, retrieve, success, info, requirements

@click.argument('name', metavar='<name>')
@click.command('install', short_help='add a package to requirements', options_metavar='<options>')
def install(name):
	required = requirements.load()
	if not name in required:
		required.add(name)
	required.show()
