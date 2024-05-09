# from flask import Flask, jsonify, request

# app = Flask(__name__)

# @app.route('/backend/api', methods=['POST'])
# def write_user_age_to_db():
    # try:
        # data = request.json
        # user = data.get('user')
        # age = data.get('age')
        
        # # return jsonify(data)
    # except Exception as e:
        # # Return an error message if an exception occurred
        # return jsonify({"error": str(e)}), 500

# if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000)  # Run the Flask app on port 5000
    
    
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def write_user_age_to_db():
    try:
        data = request.json
        user = data.get('user')
        age = data.get('age')
        
        return jsonify(data)  # Return a response
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Return an error message