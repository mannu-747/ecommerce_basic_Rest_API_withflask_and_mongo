# ecommerce_endPoints_withflask_and_mongo
This project demonstrates the creation of a RESTful API for a basic e-commerce website using Flask and MongoDB, along with user authentication using JWT (JSON Web Token). The API has three endpoints for customer registration, customer login, and orders management.

Prerequisites

Python 3.x

Postman

MongoDB Atlas account (for free MongoDB hosting with 512MB size)

To connect to my MongoDB cluster we need to add your personal IP address to manojkumar mongodb database.

Setup

I have hosted my project using the render web service.

Please follow the below steps to access(response) the implemented endpoints.

1. First we need to register to login into the application so

use this URL to register: (https://rest-apis-for-basic-ecommerce-website.onrender.com/register), method = POST

Request Body: { "first_name": "manoj", "last_name": "ram", "email": "example@gmail.com", "password": "09876" }

Response: 201 { "message": "User registered successfully", "user_id": "(<Response 74 bytes [200 OK]>, 201)" }

2. After registering in the above step use the below URL to login.
Login URL: (https://rest-apis-for-basic-ecommerce-website.onrender.com/login) method =   POST

Request Body: { "email": "example@gmail.com", "password": "09876" }

Response: 200 { "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5NjU3MDY0MSwianRpIjoiMzhiMDY3MGQtM2FkNy00YzAyLTkxNWUtYjZiZTg3MmQ3MzhmIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjY1MWY5YzY2NDIyYzU1ZTdiZjIxZjlhMSIsIm5iZiI6MTY5NjU3MDY0MSwiZXhwIjoxNjk2NTcxNTQxfQ.C1M0RquGtnvwL1rMTIXK_qXThvkPMbXJOLToCedzvXs" }

Note: The above Responses are examples of actual responses (access token will expire after 15 mins.)

This access token is the authorization for all endpoints related to orders.
3. a For inserting a new order in the mongodb Orders table use the below URL

URL: (https://rest-apis-for-basic-ecommerce-website.onrender.com/order) Method:   POST
Headers: Json Copy code { 'Authorization': 'Bearer <access_token>', 'Accept': 'application/json', 'Content-Type': 'application/json' }

Request Body: json

{
    "type": "electronics",
    "products": "Phone",
    "Quantity": 3,
    "status": "In InProgress"
}

Response: 201

{
    "id": "65277a812b73bb530ad77307",
    "message": "Order created successfully"
}

3. b This endpoint gives all orders   of a customer with URL: https://rest-apis-for-basic-ecommerce-website.onrender.com/order) Method:   GET
Headers: json Copy code { 'Authorization': 'Bearer <access_token>', 'Accept': 'application/json', 'Content-Type': 'application/json' }

response = {
    "data": "[{'_id': ObjectId('65277a812b73bb530ad77307'), 'type': 'electronics', 'products': 'Phone', 'quantity': 3, 'status': 'In InProgress', 'customer_id': '65266e378d3b541634a8672c'}]",
    "message": "orders"
}

3. c This end point gives status of a order URL: (https://rest-apis-for-basic-ecommerce-website.onrender.com/orders/status) method: GET
     Headers: json Copy code { 'Authorization': 'Bearer <access_token>', 'Accept': 'application/json', 'Content-Type': 'application/json' }
     Params: order_id = 652655aeef5d42b8f95cfd98

   response = {
    "data": "IN PROGRESS",
    "message": "status"
    }
3. d This endpoint updates the status of a order URL: (https://rest-apis-for-basic-ecommerce-website.onrender.com/orders/update) method: PUT
     Headers: json Copy code { 'Authorization': 'Bearer <access_token>', 'Accept': 'application/json', 'Content-Type': 'application/json' }
     Params: order_id = 652655aeef5d42b8f95cfd98
     request Body:
                  {"status": "Shipped"}
     Note: status may {IN_PROGRESS,CANCELLED}
      response =
                 {
                      "id": "<pymongo.results.UpdateResult object at 0x7f727d1ec890>",
                      "message": "order status updated"
                  }
3. e This endpoint cancel the order as per the customer request. URL: (https://rest-apis-for-basic-ecommerce-website.onrender.com/orders/cancel) method: PUT
      Headers: json Copy code { 'Authorization': 'Bearer <access_token>', 'Accept': 'application/json', 'Content-Type': 'application/json' }
     Params: order_id = 652655aeef5d42b8f95cfd98
     response = {
                      "id": "<pymongo.results.UpdateResult object at 0x7f727d1ec890>",
                      "message": "order canceled"
                  }

4 This endpoint Deletes the customer from Database. URL: (https://rest-apis-for-basic-ecommerce-website.onrender.com/users/<user_id>) method: DELETE
    response = {
    "message": "Your account is deleted successfully"
    }
  
Note: For all endpoints elated to the order use the access token which we generated in the login endpoint.
