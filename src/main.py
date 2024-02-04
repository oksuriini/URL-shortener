from flask import Flask, redirect
from urlshortener import logic
from flask import request

app = Flask(__name__)


@app.route("/")
def main_page():
    return "Hello, insert your url to be shortened TODO THIS PART"


@app.post("/short/")
def shorten_app():
    json = request.get_json()
    url = json["url"]
    return logic.shorten(url)


@app.get("/get/<hash>")
def get_url(hash):
    url = logic.get_link(hash)
    if url == "Link not found":
        return url
    redir = redirect(url, 302)
    return redir


app.run("0.0.0.0", 5050, True)
