# import requests
#
# product = {
#     "name": "Test Product",
#     "url": "https://example.com",
#     "target_price": 1000,
#     "email": "test@gmail.com"
# }
#
# response = requests.post(
#     "http://127.0.0.1:5000/products",
#     json=product
# )
#
# print(response.status_code)
# print(response.json())
#
# product2 = {
#     "name": "iPhone",
#     "url": "https://example.com/iphone",
#     "target_price": 50000,
#     "email": "test@gmail.com"
# }
#
# requests.post(
#     "http://127.0.0.1:5000/products",
#     json=product2
# )
# print(response.status_code)
# print(response.json())
# #PUT UPDATED product
# updated_data = {
#     "target_price": 45000
# }
#
# response = requests.put(
#     "http://127.0.0.1:5000/products/2",
#     json=updated_data
# )
#
#
#
# print(response.status_code)
# print(response.json())

# import requests
# import os
# from dotenv import load_dotenv
#
# load_dotenv()
#
# api_key = os.getenv("API_KEY")
#
# response = requests.post("http://127.0.0.1:5000/products",headers={"X-API-Key": api_key},
#     json={
#         "name": "Test",
#         "url": "https://example.com",
#         "target_price": 100,
#         "email": "test@gmail.com"
#     }
# )
#
# print(response.status_code)
# print(response.json())

# import requests
#
# response = requests.get(
#     "http://127.0.0.1:5000/products/3"
# )
#
# print(response.status_code)
# print(response.json())

# import requests
# import os
# from dotenv import load_dotenv
#
# load_dotenv()
#
# api_key = os.getenv("API_KEY")
#
# response = requests.get(
#     "http://127.0.0.1:5000/products/3",
#     headers={
#         "X-API-Key": api_key
#     }
# )
#
# print(response.status_code)
# print(response.json())

# import requests
#
# updated_data = {
#     "target_price": 45000
# }
#
# response = requests.put(
#     "http://127.0.0.1:5000/products/2",
#     json=updated_data
# )
#
# print(response.status_code)
# print(response.json())

# import requests
# import os
# from dotenv import load_dotenv
#
# load_dotenv()
#
# api_key = os.getenv("API_KEY")
#
# updated_data = {
#     "target_price": 45000
# }
#
# response = requests.put(
#     "http://127.0.0.1:5000/products/2",
#     headers={
#         "X-API-Key": api_key
#     },
#     json=updated_data
# )
#
# print(response.status_code)
# print(response.json())

# import requests
#
# response = requests.delete(
#     "http://127.0.0.1:5000/products/3"
# )
#
# print(response.status_code)
# print(response.json())

import requests
import os
from dotenv import load_dotenv

# load_dotenv()
#
# api_key = os.getenv("API_KEY")
#
# response = requests.delete(
#     "http://127.0.0.1:5000/products/3",
#     headers={
#         "X-API-Key": api_key
#     }
# )
#
# print(response.status_code)
# print(response.json())
#
# import requests
# reponse=requests.post("http://127.0.0.1:5000/products/2/check-price")
# print(reponse.text)
# print(reponse.json())

# import requests
# import os
# from dotenv import load_dotenv
# load_dotenv()
# api_key=os.getenv("API_KEY")
# response=requests.post("http://127.0.0.1:5000/products/2/check-price",headers={"X-Api-Key":api_key})
# print(response.status_code)
# print(response.json())

# import requests
# response=requests.get("http://127.0.0.1:5000/report")
# print(response.status_code)
# print(response.json())

# import requests
# import os
# from dotenv import load_dotenv
# load_dotenv()
# api_key=os.getenv("API_KEY")
# response=requests.get("http://127.0.0.1:5000/report",
#     headers={"X-API-Key": api_key})
# print(response.status_code)
# print(response.json())

# import requests
# import os
# from dotenv import load_dotenv
#
# load_dotenv()
# api_key = os.getenv("API_KEY")
#
# response = requests.get(
#     "http://127.0.0.1:5000/products/2/history",
#     headers={"X-API-Key": api_key}
# )
#
# print(response.status_code)
# print(response.json())

# import requests
# print("POST TEST RUNNING")
# url = "http://127.0.0.1:5000/products"
#
# headers = {
#     "X-API-Key": "mysecret123"
# }
#
# data = {
#     "name": "Samsung Phone",
#     "url": "https://example.com/samsung",
#     "target_price": 30000,
#     "email": "menikaranakal@gmail.com",
#     "status": "Not checked",
#     "current_price": None
# }
#
# response = requests.post(url, headers=headers,json=data)
#
# print(response.status_code)
# print(response.json())

# import requests
#
# url = "http://127.0.0.1:5000/products/3"
#
# headers = {
#     "X-API-Key": "mysecret123"
# }
# data = {
#     "target_price": 28000
# }
# response = requests.put(url, headers=headers,json=data)
#
# print(response.status_code)
# print(response.json())

# import requests
#
# url = "http://127.0.0.1:5000/products/3"
#
# headers = {
#     "X-API-Key": "mysecret123"
# }
#
# response = requests.delete(url, headers=headers)
#
# print(response.status_code)
# print(response.json())

# import requests
#
# url = "http://127.0.0.1:5000/products/2/check-price"
#
# headers = {
#     "X-API-Key": "mysecret123"
# }
#
# response = requests.post(url, headers=headers)
#
# print(response.status_code)
# print(response.json())

# import requests
#
# url = "http://127.0.0.1:5000/products/2/history"
#
# headers = {
#     "X-API-Key": "mysecret123"
# }
#
# response = requests.get(url, headers=headers)
#
# print(response.status_code)
# print(response.json())

# import requests
#
# url = "http://127.0.0.1:5000/report"
#
# headers = {
#     "X-API-Key": "mysecret123"
# }
#
# response = requests.get(url, headers=headers)
#
# print(response.status_code)
# print(response.json())

# import requests
#
# url = "http://127.0.0.1:5000/products"
#
# response = requests.get(url)
#
# print(response.status_code)
# print(response.json())

# import requests
#
# url = "http://127.0.0.1:5000/products?sort_by=price&order=wrong"
#
# headers = {
#     "X-API-Key": "mysecret123"
# }
#
# response = requests.get(url, headers=headers)
#
# print(response.status_code)
# print(response.json())

# import requests
# url = "http://127.0.0.1:5000/report"
# headers = {
#     "X-API-Key": "mysecret123"
# }
#
# response = requests.get(url, headers=headers)
#
# print(response.status_code)
# print(response.json())

# import requests
# url = "http://127.0.0.1:5000/products/2/check-price"
# headers = {
#     "X-API-Key": "mysecret123"
# }
#
# response = requests.post(url, headers=headers)
#
# print(response.status_code)
# print(response.json())

# import requests
#
# url = "http://127.0.0.1:5000/products/999"
# headers = {
#     "X-API-Key": "mysecret123"
# }
# response = requests.get(url, headers=headers)
#
# print(response.status_code)
# print(response.json())

# import requests
# url = "http://127.0.0.1:5000/products/999"
# headers = {
#     "X-API-Key": "mysecret1234"
# }
#
# response = requests.put(url,json={"target_price": 1000},headers=headers)
#
# print(response.status_code)
# print(response.json())
#
# url = "http://127.0.0.1:5000/products/999"
#
# response = requests.delete(url, headers=headers)
#
# print(response.status_code)
# print(response.json())



##to check whether the email is perfect or name or url or else get error in terminal
# import requests
# headers = {
#     "X-API-Key": "mysecret1234"
# }
#
# data = {
#     "name": "Test Missing Target",
#     "url": "https://example.com/test",
#     "email": "menikaranakal@gmail.com"
# }
# response = requests.post(
#     "http://127.0.0.1:5000/products",
#     headers=headers, json=data
# )
#
# print(response.status_code)
# print(response.json())


####this is for the invalid product check
# import requests
#
# headers = {
#     "X-API-Key": "mysecret1234",
#     "Content-Type": "application/json"
# }
#
# response = requests.post(
#     "http://127.0.0.1:5000/products",
#     headers=headers,
#     data='["wrong", "format"]'
# )
#
# print(response.status_code)
# print(response.json())


##this is for api headers checking
# import requests
#
# data = {
#     "name": "Unauthorized Test",
#     "url": "https://example.com/test",
#     "target_price": 700,
#     "email": "menikaranakal@gmail.com"
# }
#
# response = requests.post(
#     "http://127.0.0.1:5000/products",
#     json=data
# )
#
# print(response.status_code)
# print(response.json())



# import requests
#
# headers = {
#     "X-API-Key": "wrong-key"
# }
#
# data = {
#     "name": "Unauthorized Test",
#     "url": "https://example.com/test",
#     "target_price": 700,
#     "email": "menikaranakal@gmail.com"
# }
#
# response = requests.post(
#     "http://127.0.0.1:5000/products",
#     headers=headers,
#     json=data
# )

# print(response.status_code)
# print(response.json())

# import requests
#
# headers = {
#     "X-API-Key": "mysecret1234"
# }
#
# response = requests.get(
#     "http://127.0.0.1:5000/products/9999",
#     headers=headers
# )
#
# print(response.status_code)
# print(response.json())

# import requests
#
# headers = {
#     "X-API-Key": "mysecret1234"
# }
#
# data = {
#     "target_price": 400
# }
#
# response = requests.put(
#     "http://127.0.0.1:5000/products/3",
#     headers=headers,
#     json=data
# )
#
# print(response.status_code)
# print(response.json())

import requests

headers = {
    "X-API-Key": "mysecret1234"
}

response = requests.delete(
    "http://127.0.0.1:5000/products/3",
    headers=headers
)

print(response.status_code)
print(response.json())