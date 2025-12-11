from flask import (
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash
)
from app.users import users_bp
from app.users.forms import LoginForm

# Заглушка для авторизації (можеш замінити на БД пізніше)
VALID_USERNAME = "admin"
VALID_PASSWORD = "1234"


@users_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    # POST + валідна форма → обробка
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember = form.remember.data

        # Перевірка правильності логіну та паролю
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            # Створюємо сесію користувача
            session["user"] = username
            session["remember"] = remember

            # Для пункту 8* — збережемо дані у сесію
            session["form_data"] = {
                "username": username,
                "remember": remember
            }

            flash(f"Успішний вхід користувача {username}. Запам'ятати: {remember}", "success")
            return redirect(url_for("users.login"))  # PRG
        else:
            flash("Невірний логін або пароль", "error")
            return redirect(url_for("users.login"))  # PRG

    # GET-запит → можливо повертаємось після PRG
    data = session.pop("form_data", None)
    return render_template("users/login.html", form=form, data=data)


@users_bp.route("/profile")
def profile():
    username = session.get("user")
    if not username:
        flash("Спочатку увійдіть у систему", "error")
        return redirect(url_for("users.login"))

    return render_template("users/profile.html", username=username)


@users_bp.route("/logout", methods=["POST"])
def logout():
    session.pop("user", None)
    flash("Ви вийшли з системи", "info")
    return redirect(url_for("users.login"))


# ==== Налаштування cookie-теми =====

@users_bp.route("/set-theme/<theme>")
def set_theme(theme):
    if theme not in ["light", "dark"]:
        flash("Невідома тема", "error")
        return redirect(url_for("users.profile"))

    resp = redirect(url_for("users.profile"))
    resp.set_cookie("theme", theme, max_age=60*60*24*30)  # 30 днів

    flash(f"Тема змінена на {theme}", "success")
    return resp


# ==== Cookie інструменти (залишаю, бо є в проєкті й не заважає) =====

@users_bp.route("/set-cookie", methods=["POST"])
def set_cookie():
    if "user" not in session:
        flash("Спочатку увійди", "error")
        return redirect(url_for("users.login"))

    key = request.form.get("key")
    value = request.form.get("value")
    max_age = request.form.get("max_age")

    resp = redirect(url_for("users.profile"))

    if key and value:
        if max_age:
            resp.set_cookie(key, value, max_age=int(max_age))
        else:
            resp.set_cookie(key, value)
        flash(f"Cookie '{key}' додано", "success")
    else:
        flash("Порожні поля", "error")

    return resp


@users_bp.route("/delete-cookie/<name>", methods=["POST"])
def delete_cookie(name):
    if "user" not in session:
        flash("Спочатку увійди", "error")
        return redirect(url_for("users.login"))

    resp = redirect(url_for("users.profile"))
    resp.delete_cookie(name)
    flash(f"Cookie '{name}' видалено", "info")
    return resp


@users_bp.route("/delete-cookies", methods=["POST"])
def delete_cookies():
    if "user" not in session:
        flash("Спочатку увійди", "error")
        return redirect(url_for("users.login"))

    resp = redirect(url_for("users.profile"))

    for k in request.cookies.keys():
        resp.delete_cookie(k)

    flash("Всі cookies очищено", "info")
    return resp
