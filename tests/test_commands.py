from pim.commands.init import _defaults, _make_package
from pim.commands.install import install
from pim.commands.uninstall import uninstall

from click.testing import CliRunner

def _create_test_package():
    """Helper function to create a test package"""
    d = _defaults()
    d['description'] = 'test package'
    _make_package(d, True)
    return d

def test_install_and_uninstall():
    """Round trip the install/uninstall functionality"""
    pkg_to_install = 'nose'
    runner = CliRunner()
    with runner.isolated_filesystem():
        d = _create_test_package()
        result = runner.invoke(install, ['-g', pkg_to_install])
        # _install([pkg_to_install], globally=True)
        with open('requirements.txt', 'r') as f:
            lines = f.readlines()
        assert pkg_to_install in lines

        result = runner.invoke(uninstall, ['-g', pkg_to_install])
        with open('requirements.txt', 'r') as f:
            lines = f.readlines()
        assert pkg_to_install not in lines
