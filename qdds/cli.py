import click
import subprocess
import socket

click.clear()

@click.command()
@click.option('--safe', is_flag=True, help="Use safer port 8000 instead of 80.")
@click.option('--ip/--regular', default=True, help="Run on local network IP or default localhost.")
def main(safe, ip):
    host_ip = None
    port = "8000" if safe else "80"

    # Get the local IP address
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        host_ip = s.getsockname()[0]
    finally:
        s.close()

    if ip:
        click.echo(click.style('======= STARTING DEV SERVER =======', bg='red', fg='white'))
        click.echo(click.style('-----------------------------------', bg='blue', fg='white'))
        click.echo(click.style('=========     d[-_-]b    ==========', bg='blue', fg='white'))
        click.echo(click.style('___________________________________', bg='blue', fg='white'))
        if host_ip:
            click.echo(click.style(f'* Available on network via http://{host_ip}:{port}', fg='green'))
            click.launch(f'http://{host_ip}:{port}')
        subprocess.call(f"python manage.py runserver 0.0.0.0:{port}", shell=True)

    else:
        click.echo(click.style('======= Why did you do this? =======', bg='white', fg='red'))
        click.launch(f'http://localhost:{port}')
        subprocess.call(f"python manage.py runserver", shell=True)
