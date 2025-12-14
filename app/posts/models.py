from datetime import datetime
import enum
from sqlalchemy import Enum as SQLAlchemyEnum
from app.extensions import db

post_tags = db.Table(
    "post_tags",
    db.Column("post_id", db.Integer, db.ForeignKey("posts.id"), primary_key=True),
    db.Column("tag_id", db.Integer, db.ForeignKey("tags.id"), primary_key=True),
)

class Tag(db.Model):
    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    posts = db.relationship(
        "Post",
        secondary=post_tags,
        back_populates="tags"
    )

class PostCategory(enum.Enum):
    news = "news"
    publication = "publication"
    tech = "tech"
    other = "other"
    life = "life"

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    category = db.Column(SQLAlchemyEnum(PostCategory), default=PostCategory.news)
    enabled = db.Column(db.Boolean, default=True)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = db.relationship("User", back_populates="posts")

    tags = db.relationship(
        "Tag",
        secondary=post_tags,
        back_populates="posts"
    )
