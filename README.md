# Smart Deal Tracker

A Python-based application to track product prices, monitor target prices and send email alerts when prices reach the desired amount.

## Features

* Add, view, update and delete products
* Track current product prices
* Check whether the target price has been reached
* Maintain price history
* Filter and sort products by price and status
* Generate product reports
* Send email alerts when target prices are reached
* Scrape prices using BeautifulSoup and Selenium
* Secure API endpoints using API key authentication
* Tkinter graphical user interface

## Technologies Used

* Python
* Flask
* BeautifulSoup
* Selenium
* Pandas
* Tkinter
* Requests
* Pytest

## Installation

1. Clone or download the project.

2. Create and activate a virtual environment.

3. Install dependencies:

   `pip install -r requirements.txt`

4. Create a `.env` file using `.env.example` as a reference.

5. Add your API key and email credentials to `.env`.

## Running the Application

Run the Flask server:

`python main.py`

Run the Tkinter application:

`python gui\app.py`


## API Endpoints

All API requests require the `X-API-Key` header.

### Get all products

`GET /products`

Supports filtering and sorting:

- `status`
- `min_price`
- `max_price`
- `sort_by=price`
- `order=asc` or `order=desc`

Example:

`GET /products?sort_by=price&order=desc`

### Add a product

`POST /products`

Adds a new product and checks its current price.

### Get a product

`GET /products/<product_id>`

Returns a specific product.

### Update a product

`PUT /products/<product_id>`

Updates product information such as the target price.

### Delete a product

`DELETE /products/<product_id>`

Deletes a product.

### Check product price

`POST /products/<product_id>/check-price`

Checks the current price and updates price history.

### Get price history

`GET /products/<product_id>/history`

Returns the product's price history.

### Generate report

`GET /report`

Generates a product report.
## Running Tests

`python -m pytest -v`
