print("Python file started successfully")

from flask import Flask, request, send_file, Response
from db import get_connection

app = Flask(__name__)
@app.route("/")
def home():
   return send_file("add_medicine.html")

@app.route("/add_medicine.js")
def javascript():
    with open("add_medicine.js", "r") as file:
        return Response(file.read(), mimetype="application/javascript")
    

@app.route("/save_medicine", methods=["POST"])
def save_medicine():
    print("save_medi called")
    data = request.json

    medicine_name = data["medicine_name"]
    company_name = data["company_name"]
    category = data["category"]
    mfg_date = data["mfg_date"]
    print(mfg_date)
    exp_date = data["exp_date"]
    price = data["price"]
    description = data["description"]
    quantity = data["quantity"]
    batch_no = data["batch_no"]


    conn = get_connection()
    cursor = conn.cursor()
    print("DB Connected",conn)

    query = """
    INSERT INTO medicines
    (
        medicine_name,
        company_name,
        category,
        manufacturing_date,
        expiry_date,
        price,
        description,
        quantity,
        batch_no
    )
    VALUES
    (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """
    values = (
        medicine_name,
        company_name,
        category,
        mfg_date,
        exp_date,
        price,
        description,
        quantity,
        batch_no
    )
    cursor.execute(query, values)
    conn.commit()

    cursor.close()
    conn.close()

    return "Medicine Saved Successfully"


if __name__ == "__main__":
    app.run(debug=True)