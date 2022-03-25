import json
import re
from tkinter import N
from turtle import color
from app import app
from flask import render_template, request, redirect, jsonify, make_response
from datetime import datetime

# users data
users = {
    "mitsuhiko": {
        "name": "Armin Ronancher",
        "bio": "Creator of Flask framework",
        "twitter_handle": "@mitsuhiko"
    },
    "gvanrossum": {
        "name": "Guido Van Rossum",
        "bio": "Creator of Python programming",
        "twitter_handle": "@gvanrossum"
    },
    "elonmusk": {
        "name": "Elon Musk",
        "bio": "technology entrepreneur, investor and engineer",
        "twitter_handle": "@elonmusk"
    }
}


@app.route("/")
def index():
    return render_template("public/index.html")


@app.route("/about")
def about():
    return render_template("public/about.html")


@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        req = request.form
        missing = list()

        for k, v in req.items():
            if v == "":
                missing.append(k)

        if missing:
            feedback = f"Missing fields for {', '.join(missing)}"
            return render_template("public/sign_up.html", feedback=feedback)
        # username = req.get("username")
        # email = req["email"]
        # password = request.form["password"]

        # password = request.form.get("password")

        return redirect(request.url)

    return render_template("public/sign_up.html")


@app.route("/profile/<username>")
def profile(username):
    user = None
    if username in users:
        user = users[username]

    return render_template("public/profile.html", username=username, user=user)


@app.route("/multiple/<foo>/<bar>/<baz>")
def multiple(foo, bar, baz):
    print(f"foo is {foo}")
    print(f"bar is {bar}")
    print(f"baz is {baz}")

    return f"foo is {foo}, bar is {bar}, baz is {baz}"

# Guestbook


@app.route("/guestbook")
def guestbook():
    return render_template("public/guestbook.html")


@app.route("/guestbook/create-entry", methods=["POST"])
def create_entry():
    req = request.get_json()
    print(req)

    res = make_response(jsonify(req), 200)

    return res


# JSON example
@app.route("/json", methods=["POST"])
def json_example():

    if request.is_json:
        # parse json into python dictionary
        req = request.get_json()

        response_body = {
            "message": "JSON received!",
            "sender": req.get("name")
        }

        res = make_response(jsonify(response_body), 200)

        return res

    else:
        return make_response(jsonify({"message": "Request body must be JSON"}), 400)


# Jinja examples
@app.route("/jinja")
def jinja():
    # Strings
    my_name = "Julian"
    my_html = "<h1>This is some HTML</h1>"
    suspicious = "<script>alert('NEVER TRUST USER INPUT!')</script>"

    # Integers
    my_age = 30

    # Lists
    langs = ["Python", "JavaScript", "Bash", "Ruby", "C", "Rust"]

    # Dictionaries
    friends = {
        "Tony": 43,
        "Cody": 28,
        "Amy": 26,
        "Clarissa": 23,
        "Wendell": 39
    }

    # Tuples
    colors = ("red", "blue")

    # Booleans
    cool = True

    # Classes
    class GitRemote:
        def __init__(self, name, description, domain):
            self.name = name
            self.description = description
            self.domain = domain

        def pull(self):
            return f"Pulling repo '{self.name}'"

        def clone(self, repo):
            return f"Cloning into {repo}"

    my_remote = GitRemote(
        name="Learning Flask",
        description="Learn the Flask Web Framework for Python",
        domain="https://github.com"
    )

    # Functions
    def repeat(x, qty=1):
        return x * qty

    date = datetime.utcnow()

    return render_template("public/jinja.html", my_name=my_name, my_age=my_age, langs=langs,
                           friends=friends, colors=colors, cool=cool, GitRemote=GitRemote, my_remote=my_remote,
                           repeat=repeat, date=date, my_html=my_html, suspicious=suspicious)


@app.template_filter("clean_date")
def clean_date(dt):
    return dt.strftime("%d %b %Y")
