import click
from pim.cli import cli

def test_import():
	assert isinstance(cli, click.core.Group)

def test_commands():
	assert cli.commands.keys() == ['init', 'ls', 'install', 'uninstall']