import requests

def test_health_check():
    url = "http://localhost:5000/status/operation"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json() == {"health": "All systems operational"}
