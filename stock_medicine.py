print("Python file started successfully")

from flask import Flask, request, send_file, Response, jsonify
from db import get_connection

app = Flask(__name__)


@app.route("/")
def home():
    return send_file("stock_medicine.html")


@app.route("/stock_medicine.js")
def javascript():
    with open("stock_medicine.js", "r") as file:
        return Response(file.read(), mimetype="application/javascript")


@app.route("/stock_medicine")
def stock_medicine():

    print("stock_medicine  called")

    #medicine_name = request.args.get("medicine_name")

    #print("Medicine Name:", medicine_name)

    conn = get_connection()

    if conn is None:
        return jsonify({"error": "Database connection failed"}), 500

    print("DB Connected")

    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT * FROM medicines"""

    cursor.execute(query)

    output = cursor.fetchall()

    cursor.close()
    conn.close()

    print("Result:", output)

    return jsonify(output)


if __name__ == "__main__":
    app.run(debug=True)