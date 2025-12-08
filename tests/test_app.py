import pytest
from app.app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home(client):
    """Test the home page."""
    rv = client.get("/")
    assert rv.status_code == 200


def test_predict(client):
    """Test the predict endpoint."""
    data = {
        'college': '3',
        'city': '1',
        'previous_ctc': '55000',
        'previous_job_change': '2',
        'graduation_marks': '75',
        'exp_months': '24',
        'role': '1'
    }
    rv = client.post("/predict", data=data)
    assert rv.status_code == 200
    assert b'Predicted Monthly Salary' in rv.data