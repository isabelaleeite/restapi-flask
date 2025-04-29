import pytest
from application import create_app


class TesteApplication():

    @pytest.fixture
    def client():
        app = create_app('config.MockConfig')
        yield app.test_client()

    def test_get_users(self, client):
        response = client.get('/users')
        assert response.status_code == 201
