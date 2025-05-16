import click
import subprocess
import socket

# Clear Screen
click.clear()

@click.command()
@click.option('--ip/--regular', default=True)
def main(ip):
    host_name = None
    host_ip = None

    # Get the IP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    host_ip = s.getsockname()[0]

    """Start manage.py runserver with options."""
    if ip:
        click.echo(click.style('======= STARTING DEV SERVER =======', bg='red', fg='white'))
        click.echo(click.style('-----------------------------------', bg='blue', fg='white'))
        click.echo(click.style('=========     d[-_-]b    ==========', bg='blue', fg='white'))
        click.echo(click.style('___________________________________', bg='blue', fg='white'))
        if host_ip:
            click.echo(click.style('* Available on network via http://' + host_ip , fg='green'))
            click.launch('http://' + host_ip + ':8000')
        subprocess.call(" python manage.py runserver 0.0.0.0:8000", shell=True)

    else:
        click.echo(click.style('======= Why did you do this? =======', bg='white', fg='red'))
        click.launch('http://localhost:8000')
        subprocess.call(" python manage.py runserver", shell=True)
