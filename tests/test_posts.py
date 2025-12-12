from app.extensions import db
from app.posts.models import Post


def test_create_post(client):
    response = client.post(
        "/posts/create",
        data={
            "title": "Test title",
            "content": "Test content",
            "category": "news",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200

    post = db.session.scalar(
        db.select(Post).where(Post.title == "Test title")
    )
    assert post is not None
    assert post.content == "Test content"
    assert post.category.value == "news"


def test_list_posts(client):
    post = Post(
        title="List title",
        content="List content",
        category="tech",
    )
    db.session.add(post)
    db.session.commit()

    response = client.get("/posts/")
    assert response.status_code == 200
    assert b"List title" in response.data


def test_post_detail(client):
    post = Post(
        title="Detail title",
        content="Detail content",
        category="publication",
    )
    db.session.add(post)
    db.session.commit()

    response = client.get(f"/posts/{post.id}")
    assert response.status_code == 200
    assert b"Detail title" in response.data
    assert b"Detail content" in response.data


def test_update_post(client):
    post = Post(
        title="Old title",
        content="Old content",
        category="other",
    )
    db.session.add(post)
    db.session.commit()

    response = client.post(
        f"/posts/{post.id}/update",
        data={
            "title": "New title",
            "content": "New content",
            "category": "news",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200

    updated = db.session.get(Post, post.id)
    assert updated.title == "New title"
    assert updated.content == "New content"
    assert updated.category.value == "news"


def test_delete_post(client):
    post = Post(
        title="Delete title",
        content="Delete content",
        category="news",
    )
    db.session.add(post)
    db.session.commit()

    response = client.post(
        f"/posts/{post.id}/delete",
        follow_redirects=True,
    )

    assert response.status_code == 200

    deleted = db.session.get(Post, post.id)
    assert deleted is None


def test_404_page(client):
    response = client.get("/posts/999999")
    assert response.status_code == 404
