import pytest

from app.models import User, Post


@pytest.fixture(scope='module')
def new_user():
    user = User(username='viagostini', email='vini@teste.com', password='senha')
    return user


@pytest.fixture(scope='module')
def new_post():
    post = Post(body='post exemplo')
    return post
