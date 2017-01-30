import click
import subprocess

@click.command()
@click.option('-ip/-regular', default=True)
def cli(ip):
    """Start manage.py runserver with options."""
    if ip:
        click.echo('Starting Dev Server with local ip')
        subprocess.call(" python manage.py runserver 0.0.0.0:8000", shell=True)
    else:
        click.echo('Starting Dev Server')
        subprocess.call(" python manage.py runserver", shell=True)
