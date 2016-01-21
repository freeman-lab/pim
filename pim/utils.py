import os
import subprocess
from click import echo, style
from clint.textui import indent, puts

def write(name, fields=None, stringify=True, folder=None, force=False):
    """
    Write a file after filling in template fields.
    """
    location = name
    if folder:
        if not os.path.isdir(folder):
            os.mkdir(folder)
        location = os.path.join(folder, location)
    exists = os.path.exists(location)
    if exists and not force:
        info('File %s already exists and will not be overwritten.' % location)
        return
    with open(location, 'w+') as f:
        if fields:
            source = name + '.txt'
            filled = fillin(source, fields, stringify)
            f.write(filled)

def tostring(s):
    """
    Convert to a string with quotes.
    """
    return "'" + str(s) + "'"

def fillin(source, fields, stringify=True):
    """
    Fill in templates of the form {{ key }} -> value using a dictionary.
    """
    basedir = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(basedir, 'templates', source), 'r') as t:
        template = t.read()
        for k, v in fields.iteritems():
            v = tostring(v) if stringify else v
            template = template.replace('{{ ' + k + ' }}', v)
    return template

def retrieve(cmd, default=None):
    """
    Retrieve a value from a subprocess call.
    """
    try:
        return subprocess.check_output(cmd, universal_newlines=True).strip()
    except subprocess.CalledProcessError:
        return default

def load_requirements():
    """
    Load requirements.txt file into a list.
    """
    with open('requirements.txt') as f:
        required = f.read().split('\n')
    if len(required) == 1 and required[0] == '':
        required = []
    return required

def save_requirements():
    """
    Save requirements.txt to file.
    """
    with open('requirements.txt','w') as f:
        f.write('\n'.join(sorted(required)))

def show_requirements():
    """
    Show contents of requirements.txt.
    """
    with open('requirements.txt') as f:
        required = f.read().split('\n')

    echo('\nInstalled packages: ')
    with indent(4, quote='  -'):
        for package in required:
            puts(package)

def warn(message):
    echo('[' + style('warning', fg='yellow') + '] ' + message)

def success(message):
    echo('[' + style('success', fg='green') + '] ' + message)

def info(message):
    echo('[' + style('info', fg='blue') + '] ' + message)

def failure(message):
    echo('[' + style('failure', fg='red') + '] ' + message)

class requirements(object):

    def __init__(self, required=None):
        self.required = self.load() if required is None else required

    def __iter__(self):
       for r in self.required:
          yield r

    def save(self):
        with open('requirements.txt','w') as f:
            f.write('\n'.join(sorted(self.required)))

    def add(self, name):
        self.required += [name]
        self.save()

    def remove(self, name):
        self.required = [r for r in self.required if not r == name]
        self.save()

    def show(self):
        echo('\nInstalled packages: ')
        with indent(4, quote='  -'):
            for package in self.required:
                puts(package)

    @staticmethod
    def load():
        with open('requirements.txt') as f:
            required = f.read().split('\n')
        if len(required) == 1 and required[0] == '':
            required = []
        return requirements(required)
