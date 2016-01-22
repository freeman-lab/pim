import click
from pim.cli import cli

def test_import():
	assert isinstance(cli, click.core.Group)

def test_commands():
	assert set(list(cli.commands.keys())) == set(['init', 'ls', 'install', 'uninstall'])
