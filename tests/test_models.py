from sqlalchemy import select

from fast_api.models import User


def test_create_user(session):
    user = User(username='test', email='test@test.com', password='secrettest')

    session.add(user)
    session.commit()

    session.scalar(select(User).where(User.email == 'test@test.com'))

    assert user.id == 1
    assert user.username == 'test'
