from click.testing import CliRunner
from qdds.cli import main

def test_help_command():
    runner = CliRunner()
    result = runner.invoke(main, ['--help'])
    assert result.exit_code == 0
    assert "Usage" in result.output
