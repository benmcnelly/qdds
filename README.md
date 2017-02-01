# qdds

[![PyPI version](https://badge.fury.io/py/qdds.svg)](https://badge.fury.io/py/qdds)
[![Updates](https://pyup.io/repos/github/benmcnelly/qdds/shield.svg)](https://pyup.io/repos/github/benmcnelly/qdds/)
[![Python 3](https://pyup.io/repos/github/benmcnelly/qdds/python-3-shield.svg)](https://pyup.io/repos/github/benmcnelly/qdds/)

Quick Django Dev Server using [Click](https://github.com/pallets/click)

Install:

    $ pip install qdds

Using qdds:

    Inside your Django project folder where manage.py resides
    
    $ devserver
    
    This will start run the equivalent of
    
    $ ./manage.py runserver 0.0.0.0:8000
    
    This makes it run the dev server where it is listening on your IP:8000, and other people on the networks, or your phone on the WiFi can reach the server.
    
Options:

    You can also use the -regular option to use runserver normally
    
    $ devserver -regular
    
    but don't do this, its silly.
