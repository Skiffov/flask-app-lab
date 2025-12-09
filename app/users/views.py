from flask import render_template, request, redirect, url_for
from app.users import users_bp


@users_bp.route("/hi/<name>")
def greetings(name):
    age = request.args.get("age")
    return render_template("users/hi.html", name=name, age=age)


@users_bp.route("/admin")
def admin():
    return redirect(url_for("users.greetings", name="ADMINISTRATOR", age=45))

