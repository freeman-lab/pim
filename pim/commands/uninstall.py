import os
import getpass
import click
from click import echo
from clint.textui import indent, puts, prompt
from ..utils import write, retrieve, success, info, requirements

@click.argument('name', metavar='<name>')
@click.command('uninstall', short_help='remove a package from requirements', options_metavar='<options>')
def uninstall(name):
	required = requirements.load()
	if name in required:
		required.remove(name)
	required.show()