from fastapi.testclient import TestClient
import pytest
from api.controllers import ingredient as controller
from api.models import ingredient as model
from api.main import app

# CMD FROM <ROOT>: $env:PYTHONPATH="./"; pytest api/tests/test_ingredient.py

client = TestClient(app)

@pytest.fixture
def db_session(mocker):
     return mocker.Mock()
def test_create_ingredient(db_session):
    ingredient_data = {
        "name": "PyTest_Ingredient",
        "quantity": 100
    }
    ingredient_object = model.Ingredient(**ingredient_data)
    created_ingredient = controller.create(db_session, ingredient_object)

    assert created_ingredient is not None
    assert created_ingredient.name == "PyTest_Ingredient"
    assert created_ingredient.quantity == 100