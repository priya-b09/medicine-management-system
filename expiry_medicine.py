print("Python file started successfully")

from datetime import datetime

from flask import Flask, request, send_file, Response, jsonify
from db import get_connection
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={
    r"/*": {
        "origins": [
            "http://127.0.0.1:5500",
            "http://localhost:5500"
        ]
    }
})

#app = Flask(__name__)


@app.route("/")
def home():
    return send_file("expiry_medicine.html")


@app.route("/expiry_medicine.js")
def javascript():
    with open("expiry_medicine.js", "r") as file:
        return Response(file.read(), mimetype="application/javascript")


@app.route("/expiry_medicine", methods=["GET"])
def expiry_medicine():

    print("expiry_medicine called")

    expdate = request.args.get("expdate")
    print("expdate:", expdate)

    try:

       # date_obj = datetime.strptime(expdate, "%d/%m/%Y")
       # sql_date = date_obj.strftime("%Y-%m-%d")

        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        query = """SELECT * FROM medicines WHERE expiry_date BETWEEN %s AND CURDATE() """
        cursor.execute(query, (expdate,))

        output = cursor.fetchall()

        print("Output:", output)

        return jsonify(output)

    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)}), 500

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()


if __name__ == "__main__":
    app.run(debug=True)