from tkinter import N
from turtle import color
from app import app 
from flask import render_template
from datetime import datetime

@app.route("/")
def index():
    return render_template("public/index.html")

@app.route("/about")
def about():
    return render_template("public/about.html")

@app.route("/jinja")
def jinja():
    #Strings
    my_name = "Julian"
    my_html = "<h1>This is some HTML</h1>"
    suspicious = "<script>alert('NEVER TRUST USER INPUT!')</script>"

    #Integers
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