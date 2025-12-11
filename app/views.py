# app/views.py
from flask import render_template, request, flash, redirect, url_for
from app import app
from app.forms import ContactForm

import logging
from pathlib import Path

log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

logger = logging.getLogger("contact")
if not logger.handlers:
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler(log_dir / "contact.log", encoding="utf-8")
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )
    fh.setFormatter(formatter)
    logger.addHandler(fh)

@app.route("/")
def index():
    return render_template("base.html", title="Home")


@app.route("/resume")
def resume():
    return render_template("resume.html", title="Resume")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        data = {
            "name": form.name.data,
            "email": form.email.data,
            "phone": form.phone.data,
            "subject": form.subject.data,
            "message": form.message.data,
            "ip": request.remote_addr,
        }

        logger.info("Contact form submitted: %s", data)

        flash(f"Повідомлення від {form.name.data} <{form.email.data}> успішно надіслано.", "success")
        return redirect(url_for("contact"))

    return render_template("contact.html", form=form)


