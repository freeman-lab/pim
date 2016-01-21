import os
import getpass
import click
import subprocess
from click import echo
from clint.textui import indent, puts, prompt
from ..utils import write, retrieve, success, error, info, requirements, spinner

@click.argument('packages', nargs=-1, metavar='<package(s)>', required=True)
@click.command('uninstall', short_help='remove from requirements', options_metavar='<options>')
@click.option('--globally', '-g', is_flag=True, help='Uninstall from your environment using pip.')
def uninstall(packages, globally):
    required = requirements.load()
    
    for name in packages:
        if name in required:
            required.remove(name)

    if globally:
        uninstalled = []
        response = 'No uninstallation needed.'
        
        spin = spinner()
        spin.start()
        for name in packages:
            try:
                cmd = ['pip', 'uninstall', name, '-y']
                output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
                uninstalled += [name]
            except subprocess.CalledProcessError as e:
                notinstalled = 'Cannot uninstall requirement %s, not installed' % name
                if not e.output.startswith(notinstalled):
                    error(e.output)
                    response = 'No uninstallation performed.'
        spin.stop()
        
        if len(uninstalled) > 0:
            echo('\nUninstalled packages: ')
            with indent(4, quote='  -'):
                for name in uninstalled:
                    puts(name)
        else:
            echo('\n' + response)

    required.show()