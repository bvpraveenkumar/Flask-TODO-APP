import pytest
from tinydb import TinyDB, Query
from tinydb.storages import MemoryStorage

import routes
from app import create_app


@pytest.fixture(autouse=True)
def in_memory_db():
    routes.db = TinyDB(storage=MemoryStorage)
    yield
    routes.db.close()


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()


def test_main_page_loads_successfully(client):
    response = client.get("/")

    assert response.status_code == 200


def test_new_task_can_be_added(client):
    response = client.post("/add", data={"title": "Buy milk"}, follow_redirects=True)

    assert response.status_code == 200
    assert any(task["title"] == "Buy milk" for task in routes.db.all())


def test_existing_task_can_be_deleted(client):
    routes.db.insert({"id": 1, "title": "Delete me", "complete": False})

    response = client.post("/delete/1", follow_redirects=True)

    assert response.status_code == 200
    todo = Query()
    assert routes.db.search(todo.id == 1) == []
