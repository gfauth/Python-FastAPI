from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_api.schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olár mundo!'}


@app.get('/html', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def read_html():
    return """
<html>
    <head>
    <style>
        body { background-color: #1e211f; }
        h1 { color: white }
    </style>
        <title>Nosso Olá mundo!</title>
    </head>
    <body>
        <h1>Olá mundo!</h1>
    </body>
</html>"""
