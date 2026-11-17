print("Medicine Management System started successfully")

from flask import Flask, request, send_file, Response, jsonify
from flask_cors import CORS
from db import get_connection

app = Flask(__name__)

# Allow requests from local HTML files and localhost/Live Server
CORS(app, resources={
    r"/*": {
        "origins": "*"
    }
})


# ============================================================
# SEARCH MEDICINE
# ============================================================

@app.route("/search_medicine.js")
def search_medicine_js():
    with open("search_medicine.js", "r") as file:
        return Response(
            file.read(),
            mimetype="application/javascript"
        )


@app.route("/search_medicine", methods=["GET"])
def search_medicine():

    print("search_medicine called")

    medicine_name = request.args.get("medicine_name")

    print("Medicine:", medicine_name)

    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
            SELECT *
            FROM medicines
            WHERE medicine_name = %s
        """

        cursor.execute(query, (medicine_name,))

        output = cursor.fetchall()

        print("Output:", output)

        return jsonify(output)

    except Exception as e:

        print("Search Error:", e)

        return jsonify({
            "error": str(e)
        }), 500

    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()


# ============================================================
# EXPIRY MEDICINE
# ============================================================

@app.route("/expiry_medicine.js")
def expiry_medicine_js():
    with open("expiry_medicine.js", "r") as file:
        return Response(
            file.read(),
            mimetype="application/javascript"
        )


@app.route("/expiry_medicine", methods=["GET"])
def expiry_medicine():

    print("expiry_medicine called")

    expdate = request.args.get("expdate")

    print("expdate:", expdate)

    conn = None
    cursor = None

    try:

        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
            SELECT *
            FROM medicines
            WHERE expiry_date BETWEEN %s AND CURDATE()
        """

        cursor.execute(query, (expdate,))

        output = cursor.fetchall()

        print("Output:", output)

        return jsonify(output)

    except Exception as e:

        print("Expiry Error:", e)

        return jsonify({
            "error": str(e)
        }), 500

    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()



            
# ============================================================
#CHECK STOCK 
# ============================================================


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







# ============================================================
# ADD MEDICINE
# ============================================================


@app.route("/add_medicine.js")
def add_medicine_js():
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
    print("DB Connected", conn)

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

    return "Medicine saved successfully"



# ============================================================
# UPDATE MEDICINE
# ============================================================

@app.route("/update_medicine.js")
def update_medicine_js():
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



# ============================================================
# DELETE  MEDICINE
# ============================================================

@app.route("/delete_medicine.js")
def delete_medicine_js():
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


#============================================================
# Sell medicine
# ============================================================


#@app.route("/sell_medicine.js")
def dearPriya():
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


# ============================================================
# START ONE FLASK SERVER
# ============================================================

if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )

