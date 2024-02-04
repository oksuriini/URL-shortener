import socket
import os
from urlshortener.dbfunc import dbprocess
from urlshortener.shorten import shorten_url

HOSTNAME = socket.gethostname()
IP = socket.gethostbyaddr(HOSTNAME)
PUBLIC_IP_ADDRESS = os.getenv("PUBLIC_IP_ADDRESS")
PORT = 5050


def shorten(url: str):
    hashi = shorten_url(url)
    res = dbprocess.insert_url_info(hashi, url)
    if res:
        return f"URL now available from http://{HOSTNAME}:{PORT}/get/{hashi}"
    else:
        return "Url could not be inserted"


def get_link(hash: str):
    link = dbprocess.seek_url(hash)
    if link:
        url = link["url"]
        return url
    else:
        return "Link not found"
