import pytest
from django.test import Client


def test_post_list_status_code(client: Client):
    resp = client.get('/blog/')
    assert resp.status_code == 200
