print("Python file started successfully")

from flask import Flask, request, send_file, Response
from db import get_connection
from flask_cors import CORS


app = Flask(__name__)
CORS(app)



@app.route("/")
def home():
    return send_file("sell_medicine.html")


@app.route("/sell_medicine.js")
def javascript():
    with open("sell_medicine.js", "r") as file:
        return Response(file.read(), mimetype="application/javascript")


@app.route("/sell_medicine", methods=["PUT"])
def sell_medicine():

    print("sell_medicine called")

    data = request.json
    print("received data:", data)

    medicine_name = data["medicine_name"]
    quantity = data["quantity"]

    conn = get_connection()
    cursor = conn.cursor()

    print("DB Connected", conn)

    query = """
    UPDATE medicines
    SET
        quantity = quantity - %s
    WHERE medicine_name = %s
    """

    values = (
        quantity,
        medicine_name
    )

    cursor.execute(query, values)

    conn.commit()
    print("Rows updated:", cursor.rowcount)

    cursor.close()
    conn.close()

    return "Medicine Sold Successfully"


if __name__ == "__main__":
    app.run(debug=True)
