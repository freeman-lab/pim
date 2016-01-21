import os
import subprocess

def write(name, fields=None, stringify=True, folder=None):
    if folder:
        if not os.path.isdir('example/' + folder):
            os.mkdir('example/' + folder)
        location = os.path.join(folder, name)
    else:
        location = name
    with open('example/' + location, 'w+') as f:
        if fields:
            source = name + '.txt'
            filled = fill(source, fields, stringify)
            f.write(filled)

def tostring(s):
    return "'" + str(s) + "'"

def fill(source, fields, stringify=True):
    basedir = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(basedir, 'templates', source), 'r') as t:
        template = t.read()
        for k, v in fields.iteritems():
            v = tostring(v) if stringify else v
            template = template.replace('{{ ' + k + ' }}', v)
    return template

def retrieve(cmd, default=None):
    try:
        return subprocess.check_output(cmd, universal_newlines=True).strip()
    except subprocess.CalledProcessError:
        return default
