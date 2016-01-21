from pim.commands.init import _defaults, _make_package
from pim.commands.install import install
from pim.commands.uninstall import uninstall
from pim.commands.ls import ls
from click.testing import CliRunner

def _create_test_package():
    """
    Helper function to create a test package
    """
    d = _defaults()
    d['description'] = 'test package'
    _make_package(d, True)
    return d

def test_install_and_uninstall():
    """
    Round trip the install/uninstall functionality
    """
    pkg_to_install = 'nose'
    runner = CliRunner()
    with runner.isolated_filesystem():
        d = _create_test_package()
        result = runner.invoke(install, ['-g', pkg_to_install])

        # list the deps
        result = runner.invoke(ls)
        # make sure the package(s) listed in pkg_to_install is in the output
        assert pkg_to_install in result.output

        # uninstall
        result = runner.invoke(uninstall, ['-g', pkg_to_install])

        # list the deps
        result = runner.invoke(ls)
        # make sure the package(s) listed in pkg_to_install is in the output
        assert pkg_to_install not in result.output
