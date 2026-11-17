print("Python file started successfully")

from flask import Flask, request, send_file, Response, jsonify
from flask import Flask, request, jsonify
from flask_cors import CORS
from db import get_connection
#from flask import Flask, request, send_file, Response, jsonify
#from db import get_connection
app = Flask(__name__)

CORS(app, resources={
    r"/*": {
        "origins": "*"
    }
})


@app.route("/")
def home():
    return send_file("search_medicine.html")


@app.route("/search_medicine.js")
def javascript():
    with open("search_medicine.js", "r") as file:
        return Response(file.read(), mimetype="application/javascript")


@app.route("/search_medicine", methods=["GET"])
def search_medicine():

    print("search_medicine called")

    medicine_name = request.args.get("medicine_name")
    print("Medicine:", medicine_name)

    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        query = "SELECT * FROM medicines WHERE medicine_name = %s"
        cursor.execute(query, (medicine_name,))

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