import click

settings = dict(help_option_names=['-h', '--help'])
from .commands import init

@click.group(options_metavar='', subcommand_metavar='<command>', context_settings=settings)
def cli():
    pass

cli.add_command(init)