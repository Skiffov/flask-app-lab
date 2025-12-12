from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.extensions import db
from .models import Post
from .forms import PostForm

bp = Blueprint("posts", __name__, url_prefix="/posts")


@bp.route("/")
def index():
    posts = Post.query.order_by(Post.posted.desc()).all()
    return render_template("posts/posts.html", posts=posts)

@bp.route("/<int:post_id>")
def detail_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("posts/detail_post.html", post=post)

@bp.route("/<int:post_id>/update", methods=["GET", "POST"])
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    form = PostForm(obj=post)

    if form.validate_on_submit():
        form.populate_obj(post)
        db.session.commit()
        return redirect(url_for("posts.detail_post", post_id=post.id))

    return render_template("posts/add_post.html", form=form, post=post)




@bp.route("/create", methods=["GET", "POST"])
def create_post():
    form = PostForm()

    if request.method == "POST":
        print("POST data:", request.form)
        print("Form.errors:", form.errors)

    if form.validate_on_submit():
        post = Post(
            title=form.title.data,
            content=form.content.data,
            category=form.category.data,
            enabled=form.enabled.data,
            author="anon"
        )
        db.session.add(post)
        db.session.commit()
        flash("Post created", "success")
        return redirect(url_for("posts.index"))

    return render_template("posts/add_post.html", form=form)



@bp.route("/<int:post_id>/delete", methods=["GET", "POST"])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if request.method == "POST":
        db.session.delete(post)
        db.session.commit()
        flash("Post deleted", "success")
        return redirect(url_for("posts.index"))
    return render_template("posts/delete_confirm.html", post=post)


