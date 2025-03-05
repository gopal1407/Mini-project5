from flask import request, jsonify
from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "Welcome to the E-commerce API!"

from app.models import Customer, CustomerAccount, Product, Order, OrderItem  # ❌ May cause circular import

# Create a new customer
@app.route('/customer', methods=['POST'])
def add_customer():
    from app.models import Customer  # ✅ Import inside function to avoid circular imports
    data = request.get_json()
    new_customer = Customer(name=data['name'], email=data['email'], phone=data['phone'])
    db.session.add(new_customer)
    db.session.commit()
    return jsonify({"message": "Customer added successfully"}), 201

# Retrieve a customer
@app.route('/customer/<int:id>', methods=['GET'])
def get_customer(id):
    customer = Customer.query.get(id)
    if customer:
        return jsonify({"id": customer.id, "name": customer.name, "email": customer.email, "phone": customer.phone})
    return jsonify({"error": "Customer not found"}), 404



