import hashlib

def shorten_url(url: str) -> str:
    h = hashlib.shake_256(str.encode(url))
    return h.hexdigest(10)