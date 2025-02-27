from flask import Blueprint, jsonify

test = Blueprint('test', __name__)

@test.route('/test', methods=['GET'])
def example_endpoint():
    return jsonify({"success": "Hello from Flask!"})