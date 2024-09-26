from http import HTTPStatus


def test_read_root_deve_retornar_ok_e_olar_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olár mundo!'}


def test_read_html_deve_retornar_codigo_html_com_sucesso(client):
    response = client.get('/html')

    assert response.status_code == HTTPStatus.OK
    assert '<h1>Olá mundo!</h1>' in response.text


def test_create_user(client):
    response = client.post(
        '/users',
        json={
            'username': 'testeusername',
            'email': 'teste@test.com',
            'password': 'passw0rd',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'testeusername',
        'email': 'teste@test.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'testeusername',
                'email': 'teste@test.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'testeusername2',
            'email': 'teste@test.com',
            'password': 'passw0rd',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'testeusername2',
        'email': 'teste@test.com',
        'id': 1,
    }


def test_update_user_not_found(client):
    response = client.put(
        '/users/154684',
        json={
            'username': 'testeusernamenotfound',
            'email': 'teste@test.com',
            'password': 'passw0rd',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {
        'detail': 'User not found',
    }


def test_read_single_user(client):
    response = client.get('/user/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'testeusername2',
        'email': 'teste@test.com',
        'id': 1,
    }


def test_read_single_user_not_found(client):
    response = client.get('/user/1123214')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {
        'detail': 'User not found',
    }


def test_delete_user(client):
    response = client.delete('/user/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'message': 'User deleted',
    }


def test_delete_user_not_found(client):
    response = client.delete('/user/1123214')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {
        'detail': 'User not found',
    }
