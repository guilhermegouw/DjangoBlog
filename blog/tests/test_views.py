import pytest
from django.test import Client
from pytest_django.asserts import assertTemplateUsed


def test_post_list_status_code(client: Client):
    resp = client.get('/blog/')
    assert resp.status_code == 200

def test_post_list_template(client: Client):
    resp = client.get('/blog/')
    assertTemplateUsed(resp, 'blog/post/list.html')
