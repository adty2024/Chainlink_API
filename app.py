from flask import Flask, send_file, jsonify
from flask_cors import CORS

# Create a Flask app
app = Flask(__name__)
CORS(app)

@app.route("/<string:char_param>/<int:param>", methods=["GET"])
def predict(char_param, param):
    try:
        if char_param == 'e':
            if param == 1:
                return send_file("e1.mp3", mimetype="audio/mpeg")
            elif param == 2:
                return send_file("e2.mp3", mimetype="audio/mpeg")
            elif param == 3:
                return send_file("e3.mp3", mimetype="audio/mpeg")
            elif param == 4:
                return send_file("e4.mp3", mimetype="audio/mpeg")
            elif param == 5:
                return send_file("e5.mp3", mimetype="audio/mpeg")
        elif char_param == 'h':
            if param == 1:
                return send_file("h1.mp3", mimetype="audio/mpeg")
            elif param == 2:
                return send_file("h2.mp3", mimetype="audio/mpeg")
            elif param == 3:
                return send_file("h3.mp3", mimetype="audio/mpeg")
            elif param == 4:
                return send_file("h4.mp3", mimetype="audio/mpeg")
            elif param == 5:
                return send_file("h5.mp3", mimetype="audio/mpeg")
        else:
            if param == 1:
                return send_file("b1.mp3", mimetype="audio/mpeg")
            elif param == 2:
                return send_file("b2.mp3", mimetype="audio/mpeg")
            elif param == 3:
                return send_file("b3.mp3", mimetype="audio/mpeg")
            elif param == 4:
                return send_file("b4.mp3", mimetype="audio/mpeg")
            elif param == 5:
                return send_file("b5.mp3", mimetype="audio/mpeg")
    except Exception as e:
        return jsonify({"error": str(e)})


@app.route('/favicon.ico')
def favicon():
    return send_file('/favi_ico.png')

if __name__ == "__main__":
    app.run()
