# test_app.py
import pytest
from app import app  

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_vote(client):
    # Simuler un vote pour l'option A
    response = client.post('/vote', data={'vote': 'A'})
    assert response.status_code == 200
    assert b'Merci pour votre vote!' in response.data  
