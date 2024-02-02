# URL shortener

## Quickstart:

Clone repo:

`git clone https://github.com/oksuriini/URL-shortener.git`

Create venv, activate it and install requirements:

`python -m venv .venv`

`. .venv/bin/activate`

`pip install -r requirements.txt`

Start MongoDB (docker):

`docker run --name url-mongo -p 27017:27017 -d mongo:latest`

Start program from root folder:

`python src/main.py`


You can insert URLs to endpoint "/short/" with POST requests, where the body holds JSON with key "url" and the url as its value to 

## 