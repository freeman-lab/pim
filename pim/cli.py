import click

settings = dict(help_option_names=['-h', '--help'])
from .commands import init, install, ls, uninstall

@click.group(options_metavar='', subcommand_metavar='<command>', context_settings=settings)
def cli():
    """
    Hi! This is a small command line tool called `pim` for making it easy to publish Python packages.

    If you're just getting started with a new project, you'll want to call `pim init` 
    to initialize a project from inside a new folder.

    If you already have a project you want to publish, you'll want to call `pim publish`
    from inside the folder with your project (not yet implemented).
    """
    pass

cli.add_command(init)
cli.add_command(install)
cli.add_command(uninstall)
cli.add_command(ls)