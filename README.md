# URL shortener

Simple program that shortens given URL and then saves it into MongoDB as hash.

Program's API has two endpoints:

`/short/`:
Shortens given URL from requests body and saves it and formed hash into MongoDB.

`/get/<hash>`:
Gets URL from given hash and redirects to it.

Program has also "/" endpoint which serves static index.html where users can input their shortening requests and post it by pressing button.

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

You can insert URLs to endpoint "/short/" with POST requests, where the body holds JSON values with key "url" being the url that is to be shortened.

You can get shortened URLs through endpoint "/get/<hash>" with GET requests, where the parameter "hash" holds the hash value of URL that has been shortened. If there is no URL for that hash, then returns an error.

## Docker compose:

For very quick test run the docker compose file in the repo

