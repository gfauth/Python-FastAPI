import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from fast_api.app import app
from fast_api.models import table_regitry


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def session():
    engine = create_engine('sqlite:///:memory:')
    table_regitry.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    table_regitry.metadata.drop_all(engine)
