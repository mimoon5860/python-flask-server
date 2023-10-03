from flask import Blueprint, request, jsonify

services = Blueprint('services', __name__)

# Define available ride options
ride_options = {
  'standard': {
    'name': 'Standard',
    'description': 'Economical option with basic features',
    'price_per_km': 0.2
  },
  'premium': {
    'name': 'Premium',
    'description': 'Luxury option with enhanced features',
    'price_per_km': 0.5
  }
}

@services.route('/get-ride-options', methods=['GET'])
def get_ride_options():
  return jsonify(ride_options)
