import pytest

from app.models import User


def test_new_user_missing_arguments():
    with pytest.raises(TypeError):
        User(username='vini', email='vini@teste.com')
    with pytest.raises(TypeError):
        User(username='vini', password='senha')
    with pytest.raises(TypeError):
        User(email='vini@teste.com', password='senha')


def test_new_user(new_user):
    assert new_user.username == 'viagostini'
    assert new_user.email == 'vini@teste.com'
    assert new_user.password_hash != 'senha'
    assert new_user.check_password('senha')


def test_new_post(new_post):
    # TODO: make this test better
    assert new_post.body == 'post exemplo'