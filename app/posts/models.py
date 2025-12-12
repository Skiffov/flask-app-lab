import enum
from datetime import datetime
from app.extensions import db
from sqlalchemy import Enum as SQLAlchemyEnum

class PostCategory(enum.Enum):
    news = "news"
    publication = "publication"
    tech = "tech"
    other = "other"
    life = "life"  # нова категорія

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    category = db.Column(SQLAlchemyEnum(PostCategory), default=PostCategory.news)
    enabled = db.Column(db.Boolean, default=True)
    author = db.Column(db.String(20), default="Anonymous")
