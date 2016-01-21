import os
import getpass
import click
from click import echo
from clint.textui import indent, puts, prompt
from ..utils import write, retrieve, success, info, requirements

@click.command('ls', short_help='list packages in requirements', options_metavar='<options>')
def ls():
    required = requirements.load()
    required.show()
