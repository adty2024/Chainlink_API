from flask import Flask, send_file, jsonify
from flask_cors import CORS

# Create a Flask app
app = Flask(__name__)
CORS(app, origins=['http://127.0.0.1:5173', 'https://chainlinkapi-production.up.railway.app', 'https://chainlink-audio.onrender.com'])

@app.route("/<int:param>", methods=["GET"])
def predict(param):
    try:
        if param == 8:
            return send_file("output pdf 8.mp3", mimetype="audio/mpeg")
        elif param == 9:
            return send_file("output pdf 9.mp3", mimetype="audio/mpeg")
        elif param == 11:
            return send_file("output pdf 11.mp3", mimetype="audio/mpeg")
    except Exception as e:
        return jsonify({"error": str(e)})
    

@app.route('/favicon.ico')
def favicon():
    return send_file('/favi_ico.png')

if __name__ == "__main__":
    app.run()
