import pytest

from django.utils import timezone
from django.contrib.auth.models import User

from blog.models import Post


@pytest.fixture
def user_test():
    user = User.objects.create_user('John', 'lennon@thebeatles.com', 'johnpassword')
    return user


@pytest.mark.django_db
def test_post_create(user_test):
    Post.objects.create(
        title='First title', author=user_test,
        body='Body full of information', status='published'
    )
    assert Post.objects.count() == 1
