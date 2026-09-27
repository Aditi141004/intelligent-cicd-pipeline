from app import app


def test_home_page_returns_http_200():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200


def test_health_endpoint_returns_healthy_json():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.is_json
    assert response.get_json() == {"status": "healthy"}
