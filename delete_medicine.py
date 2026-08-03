print("Python file started successfully")

from flask import Flask, request, send_file, Response
from db import get_connection

app = Flask(__name__)

@app.route("/")
def home():
    return send_file("delete_medicine.html")

@app.route("/delete_medicine.js")
def javascript():
    with open("delete_medicine.js", "r") as file:
        return Response(file.read(), mimetype="application/javascript")


@app.route("/delete_medicine", methods=["DELETE"])
def delete_medicine():

    data = request.get_json()
    medicine_name = data["medicine_name"]

    conn = get_connection()
    cursor = conn.cursor()
    print("DB Connected", conn)

    query = """
    DELETE FROM medicines
    WHERE medicine_name = %s
    """

    cursor.execute(query, (medicine_name,))
    conn.commit()

    cursor.close()
    conn.close()

    return "Medicine Deleted Successfully"


if __name__ == "__main__":
    app.run(debug=True)