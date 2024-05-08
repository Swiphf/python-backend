from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/backend/api', methods=['POST'])
def receive_data():
    try:
        # Get data from the request body
        data = request.json
        # Process the received data (you can perform any operations here)
        # For demonstration, we'll just echo back the received data
        return jsonify(data)
    except Exception as e:
        # Return an error message if an exception occurred
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Run the Flask app on port 5001