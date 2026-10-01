import os
from flask import request, jsonify
from dotenv import load_dotenv
from functools import wraps

load_dotenv()


def require_api_key(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        api_key = request.headers.get("X-API-Key")

        if api_key != os.getenv("API_KEY"):
            return jsonify({"error": "Invalid or missing API key"}), 401

        return func(*args, **kwargs)

    return wrapper