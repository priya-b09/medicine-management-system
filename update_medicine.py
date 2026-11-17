print("Python file started successfully")

from flask import Flask, request, send_file, Response
from db import get_connection

app = Flask(__name__)


@app.route("/")
def home():
    return send_file("update_medicine.html")


@app.route("/update_medicine.js")
def javascript():
    with open("update_medicine.js", "r") as file:
        return Response(file.read(), mimetype="application/javascript")


@app.route("/update_medicine", methods=["PUT"])
def update_medicine():

    print("update_medicine called")

    data = request.json
    print("received data:",data)

    medicine_name = data["medicine_name"]
    company_name = data["company_name"]
    category = data["category"]
    mfg_date = data["mfg_date"]
    exp_date = data["exp_date"]
    price = data["price"]
    description = data["description"]
    quantity = data["quantity"]
    batch_no = data["batch_no"]

    conn = get_connection()
    cursor = conn.cursor()

    print("DB Connected", conn)

    query = """
    UPDATE medicines
    SET
    
        company_name = %s,
        category = %s,
        manufacturing_date = %s,
        expiry_date = %s,
        price = %s,
        description = %s,
        quantity = %s,
        batch_no = %s
    WHERE medicine_name = %s
    """

    values = (
        company_name,
        category,
        mfg_date,
        exp_date,
        price,
        description,
        quantity,
        batch_no,
         medicine_name
    )

    cursor.execute(query, values)

    conn.commit()
    print("Rows updated:", cursor.rowcount)

    cursor.close()
    conn.close()

    return "Medicine Updated Successfully"


if __name__ == "__main__":
    app.run(debug=True)