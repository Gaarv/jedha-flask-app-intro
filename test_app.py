from flask import Flask


def test_hello_text_route(app: Flask):
    """
    GIVEN a Flask application
    WHEN route /hello/text is requested
    THEN response is valid
    """
    client = app.test_client()
    url = "/hello/text"
    response = client.get(url)
    assert response.status_code == 200
    assert response.get_data() == b"Hello, World!"


def test_hello_json_route(app: Flask):
    """
    GIVEN a Flask application
    WHEN route /hello/json is requested
    THEN response is valid
    """
    client = app.test_client()
    url = "/hello/json"
    response = client.get(url)
    assert response.status_code == 200
    assert response.get_json() == {"text": "Hello, World!"}
