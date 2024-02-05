from flask import Flask, request, jsonify
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json 

uri = "mongodb+srv://manojkumarpichuka:ManojKumar@143@project.mfpwj33.mongodb.net/?retryWrites=true&w=majority"

mongo = MongoClient(uri)

app = Flask(__name__)

class ECommerce:
    def verify(data):
        collection = mongo.Ecommerce.users
        user_details  = collection.find_one(data)
        if user_details:
            return user_details
        else:
            return False
    
    def insert(data):
        collection = mongo.Ecommerce.users
        id  = collection.insert_one(data).inserted_id
        return jsonify(message="Document added successfully", id=str(id)), 201
    
    def place_order(data):
        collection = mongo.Ecommerce.orders
        id  = collection.insert_one(data).inserted_id
        return jsonify(message="Order created successfully", id=str(id)), 201

    def all_orders(data):
        collection = mongo.Ecommerce.orders
        orderss  = collection.find(data)
        orders_details = []
        for i in orderss:
            orders_details.append(i)
        return jsonify(message="orderss", data=str(orders_details)), 201
        
    def get_order_status(id):
        collection = mongo.Ecommerce.orders
        order_data  = collection.find_one(id)
        return jsonify(message="status", data=str(order_data['status'])), 201
        
    def update_order_status(orders_id, data):
        collection = mongo.Ecommerce.orders
        orders_id  = collection.update_one(orders_id, data)
        return jsonify(message="order status updated", id=str(orders_id)), 201
    
    def cancel_order(orders_id, data):
        collection = mongo.Ecommerce.orders 
        order_data  = collection.find_one(id)
        if order_data['status'] == 'cancel':
            return jsonify(message="order already canceled"), 201
        orders_id  = collection.update_one(orders_id, data)
        return jsonify(message="order canceled", id=str(orders_id)), 201

    def delete_user_id(user_id):
        collection = mongo.Ecommerce.users
        user_id  = collection.delete_one(user_id)
        return jsonify(message="Your account is deleted succesfully"), 201

