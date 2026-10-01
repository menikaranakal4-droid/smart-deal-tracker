import pytest
from app.api.routes import app
import app.storage.storage as storage
import app.api.routes as routes


@pytest.fixture(autouse=True)
def use_test_data(tmp_path, monkeypatch):
    test_file = tmp_path / "products.json"

    test_file.write_text("[]")

    monkeypatch.setattr(storage, "DATA_FILE", test_file)


def test_home_or_unknown_route():
    client = app.test_client()

    response = client.get("/unknown")

    assert response.status_code == 404


def test_get_products_without_api_key():
        client = app.test_client()

        response = client.get("/products")

        assert response.status_code == 401


def test_get_products_with_api_key():
    client = app.test_client()

    response = client.get(
        "/products",
        headers={"X-API-Key": "mysecret1234"}
    )

    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_add_product(monkeypatch):
    def fake_check_price(product):
        return 500, "Target price not reached"

    monkeypatch.setattr(routes, "check_price", fake_check_price)
    client = app.test_client()

    product = {
        "name": "Pytest Product",
        "url": "https://example.com",
        "target_price": 1000,
        "email": "test@example.com",
        # "scraper": "beautifulsoup"
    }

    response = client.post(
        "/products",
        json=product,
        headers={"X-API-Key": "mysecret1234"}
    )

    assert response.status_code == 201
    assert response.json["name"] == "Pytest Product"
    assert response.json["target_price"] == 1000


def test_add_invalid_product():
    client = app.test_client()

    product = "invalid data"

    response = client.post(
        "/products",
        json=product,
        headers={"X-API-Key": "mysecret1234"}
    )

    assert response.status_code == 400
    assert response.json["error"] == "Invalid product data"


def test_get_product_by_id(monkeypatch):
    def fake_check_price(product):
        return 500, "Target price not reached"

    monkeypatch.setattr(routes, "check_price", fake_check_price)

    client = app.test_client()

    # First, add a product
    product = {
        "name": "Get Test Product",
        "url": "https://example.com",
        "target_price": 2000,
        "email": "test@example.com"
    }

    add_response = client.post(
        "/products",
        json=product,
        headers={"X-API-Key": "mysecret1234"}
    )

    product_id = add_response.json["id"]

    # Now, retrieve that product
    response = client.get(
        f"/products/{product_id}",
        headers={"X-API-Key": "mysecret1234"}
    )

    assert response.status_code == 200
    assert response.json["name"] == "Get Test Product"


def test_update_product(monkeypatch):
    from app.api import routes

    def fake_check_price(product):
        return 500, "Target price not reached"

    monkeypatch.setattr(routes, "check_price", fake_check_price)

    client = app.test_client()
    headers = {"X-API-Key": "mysecret1234"}

    # Create a product
    product = {
        "name": "Update Test Product",
        "url": "https://example.com",
        "target_price": 2000,
        "email": "test@example.com"
    }

    add_response = client.post(
        "/products",
        json=product,
        headers=headers
    )

    product_id = add_response.json["id"]

    # Update the product
    updated_data = {
        "name": "Updated Product",
        "target_price": 1500
    }

    response = client.put(
        f"/products/{product_id}",
        json=updated_data,
        headers=headers
    )

    assert response.status_code == 200
    assert response.json["name"] == "Updated Product"
    assert response.json["target_price"] == 1500


def test_delete_product(monkeypatch):
    def fake_check_price(product):
        return 500, "Target price not reached"

    monkeypatch.setattr(routes, "check_price", fake_check_price)

    client = app.test_client()
    headers = {"X-API-Key": "mysecret1234"}

    # Create a product
    product = {
        "name": "Delete Test Product",
        "url": "https://example.com",
        "target_price": 1000,
        "email": "test@example.com"
    }

    add_response = client.post(
        "/products",
        json=product,
        headers=headers
    )

    product_id = add_response.json["id"]

    # Delete the product
    response = client.delete(
        f"/products/{product_id}",
        headers=headers
    )

    assert response.status_code == 200
    assert response.json["message"] == "product deleted"

    # Verify that the product no longer exists
    get_response = client.get(
        f"/products/{product_id}",
        headers=headers
    )

    assert get_response.status_code == 404


def test_check_product_price(monkeypatch):
    from app.api import routes
    def fake_check_price(product):
        return 500, "Target price not reached"

    monkeypatch.setattr(routes, "check_price", fake_check_price)
    from app.api import routes

    client = app.test_client()
    headers = {"X-API-Key": "mysecret1234"}

    product = {
        "name": "Price Test Product",
        "url": "http://example.com",
        "target_price": 50000,
        "email": "test@example.com"
    }

    add_response = client.post(
        "/products",
        json=product,
        headers=headers
    )
    product_id = add_response.json["id"]

    # Replace the real price checker with a predictable test result
    monkeypatch.setattr(
        routes,
        "check_price",
        lambda product: (45000.0, "Target price reached")
    )

    response = client.post(
        f"/products/{product_id}/check-price",
        headers=headers
    )

    assert response.status_code == 200
    assert response.json["current_price"] == 45000.0
    assert response.json["status"] == "Target price reached"


def test_get_price_history(monkeypatch):
    def fake_check_price(product):
        return 500, "Target price not reached"

    monkeypatch.setattr(routes, "check_price", fake_check_price)

    client = app.test_client()

    headers = {"X-API-Key": "mysecret1234"}

    # Create a product with price history
    product = {
        "name": "History Test Product",
        "url": "https://example.com",
        "target_price": 1000,
        "email": "test@example.com",
        "price_history": [
            {
                "price": 900,
                "timestamp": "2026-09-29T10:00:00"
            },
            {
                "price": 800,
                "timestamp": "2026-09-29T11:00:00"
            }
        ]
    }

    add_response = client.post(
        "/products",
        json=product,
        headers=headers
    )

    product_id = add_response.json["id"]

    # Retrieve price history
    response = client.get(
        f"/products/{product_id}/history",
        headers=headers
    )

    assert response.status_code == 200
    assert len(response.json) == 2
    assert response.json[0]["price"] == 900
    assert response.json[1]["price"] == 800

def test_update_invalid_product():
    client = app.test_client()
    headers = {"X-API-Key": "mysecret1234"}

    response = client.put(
        "/products/1",
        json="invalid data",
        headers=headers
    )

    assert response.status_code == 400

def test_filter_products_by_status():
    client = app.test_client()
    headers = {"X-API-Key": "mysecret1234"}

    response = client.get(
        "/products?status=Target%20price%20reached",
        headers=headers
    )

    assert response.status_code == 200

    for product in response.json:
        assert product["status"] == "Target price reached"

def test_filter_products_by_price():
    client = app.test_client()
    headers = {"X-API-Key": "mysecret1234"}

    response = client.get(
        "/products?min_price=40000&max_price=50000",
        headers=headers
    )

    assert response.status_code == 200

    for product in response.json:
        assert product["current_price"] is not None
        assert 40000 <= product["current_price"] <= 50000

def test_sort_products_by_price():
    client = app.test_client()
    headers = {"X-API-Key": "mysecret1234"}

    response = client.get(
        "/products?sort_by=price&order=desc",
        headers=headers
    )

    assert response.status_code == 200

    products = response.json

    prices = [
        product.get("current_price")
        for product in products
        if product.get("current_price") is not None
    ]

    assert prices == sorted(prices, reverse=True)