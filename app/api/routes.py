
from app.storage.storage import load_products, save_products
from app.services.price_service import check_price
from flask import Flask, jsonify, request
from app.services.report_service import create_report
from app.api.auth import require_api_key
import requests
from app.utils.validators import (validate_product_name,validate_url,validate_target_price,validate_email)
from app.scraper.beautifulsoup_scraper import scrape_price
from app.scraper.selenium_scraper import scrape_price_selenium


app = Flask(__name__)


@app.route("/products/<int:product_id>", methods=["GET"])
@require_api_key
def get_product(product_id):
    products = load_products()

    for product in products:
        if product["id"] == product_id:
            return jsonify(product)

    return jsonify({"error": "product not found"}), 404


@app.route("/products/<int:product_id>", methods=["PUT"])
@require_api_key
def update_product(product_id):
    products = load_products()
    updated_data = request.get_json()
    if not isinstance(updated_data, dict):
        return jsonify({"error": "Invalid product data"}), 400

    for product in products:
        if product["id"] == product_id:
            product.update(updated_data)
            save_products(products)
            return jsonify(product)

    return jsonify({"error": "product not found"}), 404


@app.route("/products/<int:product_id>", methods=["DELETE"])
@require_api_key
def delete_product(product_id):
    products = load_products()

    for product in products:
        if product["id"] == product_id:
            products.remove(product)
            save_products(products)
            return jsonify({"message": "product deleted"})

    return jsonify({"error": "product not found"}), 404


@app.route("/products", methods=["GET", "POST"])
@require_api_key
def products():
    products = load_products()

    if request.method == "GET":
        status = request.args.get("status")
        min_price = request.args.get("min_price", type=float)
        max_price = request.args.get("max_price", type=float)
        sort_by = request.args.get("sort_by")
        order = request.args.get("order", "asc")

        if order not in ["asc", "desc"]:
            return jsonify({"error": "Invalid sort order"}), 400

        filtered_products = products

        if status:
            filtered_products = [
                product for product in filtered_products
                if product.get("status") == status
            ]

        if min_price is not None:
            filtered_products = [
                product for product in filtered_products
                if product.get("current_price") is not None
                and product.get("current_price") >= min_price
            ]

        if max_price is not None:
            filtered_products = [
                product for product in filtered_products
                if product.get("current_price") is not None
                and product.get("current_price") <= max_price
            ]

        if sort_by == "price":
            priced_products = [
                product for product in filtered_products
                if product.get("current_price") is not None
            ]

            unpriced_products = [
                product for product in filtered_products
                if product.get("current_price") is None
            ]

            priced_products = sorted(
                priced_products,
                key=lambda product: product["current_price"],
                reverse=(order == "desc")
            )

            filtered_products = priced_products + unpriced_products

        return jsonify(filtered_products)

    # This part runs only for POST requests.

    # This part runs only for POST requests.
    product = request.get_json()

    if not isinstance(product, dict):
        return jsonify({"error": "Invalid product data"}), 400

    name = product.get("name")
    url = product.get("url")
    target_price = product.get("target_price")
    email = product.get("email")

    if not validate_product_name(name):

        return jsonify({"error": "Product name is required"}), 400

    if not validate_url(url):
        return jsonify({"error": "Invalid product URL"}), 400

    if not validate_target_price(target_price):
        return jsonify({"error": "Target price must be a positive number"}), 400

    if not validate_email(email):
        return jsonify({"error": "Invalid email address"}), 400

    product["target_price"] = float(target_price)

    product["id"] = max(
        (p.get("id", 0) for p in products),
        default=0
    ) + 1

    try:
        current_price, status = check_price(product)

        product["current_price"] = current_price
        product["status"] = status
    except (ValueError, requests.RequestException) as error:
        print("POST ERROR:", error)
        return jsonify({"error": str(error)}), 400

    products.append(product)
    save_products(products)

    return jsonify(product), 201






@app.route("/products/<int:product_id>/check-price",methods=["POST"])
@require_api_key
def check_product_price(product_id):
    products = load_products()

    for product in products:
        if product["id"] == product_id:
            try:
                current_price, status = check_price(product)
            except ValueError as error:
                return jsonify({"error": str(error)}), 400
            except Exception:
                return jsonify({"error": "Price check failed"}), 500


            product["current_price"] = current_price
            product["status"] = status

            save_products(products)

            return jsonify({
                "product": product,
                "current_price": current_price,
                "status": status
            })

    return jsonify({"error": "product not found"}), 404


@app.route( "/products/<int:product_id>/history",methods=["GET"])
@require_api_key
def get_price_history(product_id):
    products = load_products()

    for product in products:
        if product["id"] == product_id:
            return jsonify(product.get("price_history", []))

    return jsonify({"error": "product not found"}), 404


@app.route("/report", methods=["GET"])
@require_api_key
def get_report():
    df = create_report()
    return df.to_json(orient="records")


