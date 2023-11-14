# test_app.py
import pytest
from app import app  # Importez votre application Flask ici

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_vote(client):
    # Simuler un vote pour l'option A
    response = client.post('/vote', data={'vote': 'A'})
    assert response.status_code == 200
    assert b'Merci pour votre vote!' in response.data  # Vérifiez la réponse de votre application

# Cette fonction pourrait vérifier l'état de la base de données ou tout autre
# résultat attendu de l'action de vote, selon la logique de votre application.
