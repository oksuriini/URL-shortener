import os
from flask import Flask, redirect, render_template
from urlshortener import logic
from flask import request

app = Flask(__name__)

templates = os.path.dirname(__file__)

if os.getenv("FLASK_HOST"):
    HOST = os.getenv("FLASK_HOST")
else:
    HOST = "0.0.0.0"


@app.route("/")
def main_page():
    return render_template("index.html")


@app.route("/short/")
def shorten_app():
    if request.args.get("url"):
        url = request.args.get("url")
    else:
        url = ""
    print(url)
    return logic.shorten(url)


@app.get("/get/<hash>")
def get_url(hash):
    url = logic.get_link(hash)
    if url == "Link not found":
        return url
    redir = redirect(url, 302)
    return redir


app.run(f"{HOST}", logic.PORT, True)
