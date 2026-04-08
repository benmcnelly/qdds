import click
import subprocess
import socket
import sys
import os

def check_manage_py():
    """Ensure we are in a Django project directory."""
    if not os.path.exists("manage.py"):
        click.echo(click.style("Error: manage.py not found. Are you in a Django project directory?", fg="red"))
        sys.exit(1)

def get_local_ip():
    """Attempt to find the local IP address."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except Exception:
        return None
    finally:
        s.close()

def can_bind_port(port):
    """Check if we can bind to the specified port."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind(("0.0.0.0", int(port)))
        return True
    except Exception:
        return False
    finally:
        s.close()


@click.command()
@click.option('--port', type=int, help="Specify a port explicitly.")
@click.option('--no-browser', is_flag=True, help="Do not open the browser automatically.")
@click.option('--localhost', 'mode', flag_value='localhost', help="Run on localhost only.")
@click.option('--regular', 'mode', flag_value='localhost', hidden=True, help="Alias for --localhost.")
@click.option('--ip', 'mode', flag_value='ip', default=True, help="Run on local network IP (default).")
@click.option('--safe', is_flag=True, help="Legacy option to force port 8000.")
def main(port, no_browser, mode, safe):
    click.clear()
    check_manage_py()

    host_ip = None

    if safe:
        port = 8000

    if port is None:
        if can_bind_port(80):
            port = 80
        else:
            port = 8000

    is_localhost_only = (mode == 'localhost')

    click.echo(click.style('======= STARTING DEV SERVER =======', bg='blue', fg='white'))
    click.echo(click.style('=========     d[-_-]b    ==========', fg='cyan'))

    if is_localhost_only:
        host_ip = "127.0.0.1"
        click.echo(click.style(f'* Running on localhost only: http://127.0.0.1:{port}', fg='yellow'))
        cmd = [sys.executable, "manage.py", "runserver", str(port)]
    else:
        host_ip = get_local_ip()
        if host_ip:
            click.echo(click.style(f'* Available on network via: http://{host_ip}{f":{port}" if port != 80 else ""}', fg='green'))
        else:
            host_ip = "127.0.0.1"
            click.echo(click.style(f'* Warning: Could not detect local IP. Falling back to localhost.', fg='yellow'))
        cmd = [sys.executable, "manage.py", "runserver", f"0.0.0.0:{port}"]

    click.echo(click.style('___________________________________', bg='blue', fg='white'))

    if not no_browser:
        try:
            url = f'http://{host_ip}{f":{port}" if port != 80 else ""}'
            click.launch(url)
        except Exception:
            pass

    try:
        subprocess.run(cmd)
    except KeyboardInterrupt:
        click.echo("\nServer stopped.")
