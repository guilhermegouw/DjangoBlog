import pytest
from typing import List
from blog.models import Post
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse
from model_bakery import baker
from pytest_django.asserts import assertTemplateUsed, assertContains, assertNotContains


@pytest.fixture
def user_sample():
    user = baker.make(User)
    return user


@pytest.fixture
def published_post_sample(user_sample):
    published_post_sample = baker.make(Post, status="published")
    return published_post_sample


@pytest.fixture
def published_posts():
    posts = baker.make(Post, status="published", _quantity=3)
    return posts


@pytest.fixture
def client_post_detail(client: Client, published_post_sample):
    year = published_post_sample.publish.year
    month = published_post_sample.publish.month
    day = published_post_sample.publish.day
    slug = published_post_sample.slug
    resp = client.get(f"/blog/{year}/{month}/{day}/{slug}/")
    return resp


@pytest.fixture
def client_post_share(client: Client, published_post_sample):
    post_id = published_post_sample.id
    resp = client.get(f"/blog/{post_id}/share/")
    return resp


@pytest.fixture
def client_post_list(client: Client):
    resp = client.get(reverse("blog:post_list"))
    return resp


@pytest.mark.django_db
def test_post_list_status_code(client_post_list):
    assert client_post_list.status_code == 200


@pytest.mark.django_db
def test_post_list_template(client_post_list):
    assertTemplateUsed(client_post_list, "blog/post/list.html")


@pytest.mark.django_db
def test_post_detail_status_code(client_post_detail):
    assert client_post_detail.status_code == 200


@pytest.mark.django_db
def test_post_detail_template(client_post_detail):
    assertTemplateUsed(client_post_detail, "blog/post/detail.html")


@pytest.mark.django_db
def test_post_share_status_code(client_post_share):
    assert client_post_share.status_code == 200
