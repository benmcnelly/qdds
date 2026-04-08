import os
import socket
from unittest import mock
from click.testing import CliRunner
from qdds.cli import main, get_local_ip, can_bind_port, check_manage_py

def test_help_command():
    runner = CliRunner()
    result = runner.invoke(main, ['--help'])
    assert result.exit_code == 0
    assert "Usage" in result.output

def test_get_local_ip():
    ip = get_local_ip()
    # It might return None if no network, but typically it returns a string like "192.168.X.X" or "10.X.X.X"
    if ip is not None:
        assert isinstance(ip, str)
        assert len(ip.split('.')) == 4

def test_can_bind_port():
    # Attempt to bind to a high, likely unused port
    assert can_bind_port(65534) in (True, False) # just making sure it runs and returns a boolean

@mock.patch('qdds.cli.check_manage_py')
@mock.patch('subprocess.run')
@mock.patch('click.launch')
def test_cli_localhost(mock_launch, mock_run, mock_check):
    runner = CliRunner()
    result = runner.invoke(main, ['--localhost', '--no-browser'])
    assert result.exit_code == 0
    assert '* Running on localhost only' in result.output
    # Check that subprocess.run was called with manage.py
    assert mock_run.called
    args = mock_run.call_args[0][0]
    assert "manage.py" in args
    assert "runserver" in args
    mock_launch.assert_not_called()

@mock.patch('qdds.cli.check_manage_py')
@mock.patch('subprocess.run')
@mock.patch('click.launch')
def test_cli_port_override(mock_launch, mock_run, mock_check):
    runner = CliRunner()
    result = runner.invoke(main, ['--port', '9090', '--no-browser'])
    assert result.exit_code == 0
    args = mock_run.call_args[0][0]
    assert "0.0.0.0:9090" in args

@mock.patch('qdds.cli.check_manage_py')
@mock.patch('subprocess.run')
@mock.patch('click.launch')
def test_cli_safe_override(mock_launch, mock_run, mock_check):
    runner = CliRunner()
    result = runner.invoke(main, ['--safe', '--no-browser'])
    assert result.exit_code == 0
    args = mock_run.call_args[0][0]
    assert "0.0.0.0:8000" in args
