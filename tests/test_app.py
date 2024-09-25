from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_api.app import app


def test_read_root_deve_retornar_ok_e_olar_mundo():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olár mundo!'}


def test_read_html_deve_retornar_codigo_html_com_sucesso():
    client = TestClient(app)

    response = client.get('/html')

    assert response.status_code == HTTPStatus.OK
    assert '<h1>Olá mundo!</h1>' in response.text
