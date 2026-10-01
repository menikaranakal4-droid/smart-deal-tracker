import requests
response=requests.post("http://127.0.0.1:5000/products/2/check-price")
print(response.status_code)
print(response.json())
