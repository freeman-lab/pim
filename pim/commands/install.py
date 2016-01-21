import os
import getpass
import subprocess
import click
import time
from click import echo
from clint.textui import indent, puts, prompt, progress
from ..utils import write, retrieve, success, error, info, requirements, spinner

@click.argument('packages', nargs=-1, metavar='<package(s)>')
@click.command('install', short_help='add to requirements', options_metavar='<options>')
@click.option('--globally', '-g', is_flag=True, help='Install into your environment using pip.')
def install(packages, globally):
    required = requirements.load()

    for name in packages:
        if not name in required:
            required.add(name)

    if len(packages) == 0:
        packages = required

    if globally:
        installed = []
        response = 'No installation needed.'

        spin = spinner()
        spin.start()
        for name in packages:
            try:
                cmd = ['pip', 'install', name]
                output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
                if not output.startswith('Requirement already satisfied'):
                    installed += [name]
            except subprocess.CalledProcessError as e:
                spin.stop()
                echo('')
                error(e.output)
                response = 'No installation performed.'
        spin.stop()

        if len(installed) > 0:
            echo('\nInstalled packages: ')
            with indent(4, quote='  -'):
                for name in installed:
                    puts(name)
        else:
            echo('\n' + response)

    required.show()
