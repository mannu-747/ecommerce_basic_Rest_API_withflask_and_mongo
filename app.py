from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from db import ECommerce
import json 
from bson import ObjectId



app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'your-secret-key'
jwt = JWTManager(app)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']
    password = data['password']
    verify_details = {'email': email,'password': password}
    if ECommerce.verify(verify_details):
        return jsonify({'message': 'User already exists'}), 400
    user_id = ECommerce.insert({'first_name': first_name, 'last_name': last_name, 'email': email, 'password': password})
    return jsonify({'message': 'User registered successfully', 'user_id': str(user_id)}), 201


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']
    details = {'email': email, 'password': password}
    user = ECommerce.verify(details)
    if not user:
        return jsonify({'message': 'Invalid credentials'}), 401
    access_token = create_access_token(identity=str(user['_id']))
    return jsonify({'access_token': access_token}), 200


@app.route('/order', methods=['POST'])
@jwt_required()
def create_order():
    current_user = get_jwt_identity()
    data = request.get_json()
    data['customer_id'] = current_user
    return ECommerce.place_order(data)


@app.route('/order', methods=['GET'])
@jwt_required()
def get_all_orders():
    current_user = get_jwt_identity()
    data = {'customer_id': current_user} 
    return ECommerce.all_orders(data)

@app.route('/orders/status', methods=['GET'])
@jwt_required()
def get_order_status():
    order_id = request.args.get('order_id')
    order_id_json = {'_id': ObjectId(order_id)}
    order_data = ECommerce.get_order_status(order_id_json)
    return order_data

@app.route('/orders/update', methods=['PUT'])
@jwt_required()
def update_order_status():
    order_id = request.args.get('order_id')
    data = request.get_json()
    updated_data_json =   {
                '$set': {'status': data['status']}
                }
    order_id_json = {'_id': ObjectId(order_id)}
    return ECommerce.update_order_status(order_id_json, updated_data_json)
    
@app.route('/orders/cancel', methods=['PUT'])
@jwt_required()
def cancel_orders():
    current_user = get_jwt_identity()
    order_id = request.args.get('order_id')
    updated_data_json =   {
                '$set': {'status': 'cancel'}
                }
    order_id_json = {'_id': ObjectId(order_id)}
    return ECommerce.cancel_order(order_id_json,updated_data_json)
    
@app.route('/users/<user_id>', methods = ['DELETE'])
@jwt_required()
def delete_customer(user_id):
    user_id_json = {'_id': ObjectId(user_id)}
    return ECommerce.delete_user_id(user_id_json)

if __name__ == '__main__':
    app.run(debug=True)
