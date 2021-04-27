import pytest

from django.utils import timezone
from django.contrib.auth.models import User
from model_bakery import baker

from blog.models import Post, Comment


@pytest.fixture
def user_sample():
    user = baker.make(User)
    return user


@pytest.fixture
def published_post_sample(user_sample):
    published_post_sample = baker.make(Post, status="published")
    return published_post_sample


@pytest.fixture
def unpublished_post_sample(user_sample):
    unpublished_post_sample = baker.make(Post, status="draft")
    return unpublished_post_sample


@pytest.mark.django_db
def test_post_create(user_sample):
    Post.objects.create(
        title="First title",
        author=user_sample,
        body="Body full of information",
        status="published",
    )
    assert Post.objects.count() == 1


@pytest.mark.django_db
def test_published_manager_published_sample(published_post_sample):
    output = Post.published.all()
    assert published_post_sample in output


@pytest.mark.django_db
def test_published_manager_unpublished_sample(unpublished_post_sample):
    output = Post.published.all()
    assert unpublished_post_sample not in output


@pytest.mark.django_db
def test_comment_create(published_post_sample):
    Comment.objects.create(
        post=published_post_sample,
        name="Guilherme",
        email="guilherme@email.com",
        body="This is the body of a comment.",
    )
    assert Comment.objects.count() == 1
