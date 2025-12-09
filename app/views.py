# app/views.py
from flask import render_template
from app import app


@app.route("/")
def index():
    return render_template("base.html", title="Home")


@app.route("/resume")
def resume():
    return render_template("resume.html", title="Resume")


@app.route("/contact")
def contact():
    return render_template("contact.html", title="Contacts")
