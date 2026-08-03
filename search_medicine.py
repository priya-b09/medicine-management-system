print("Python file started successfully")

from flask import Flask, request, send_file, Response,jsonify
from db import get_connection

app = Flask(__name__)
@app.route("/")
def home():
   return send_file("search_medicine.html")

@app.route("/search_medicine.js")
def javascript():
    with open("search_medicine.js", "r") as file:
        return Response(file.read(), mimetype="application/javascript")
    

@app.route("/search_medicine", methods=["GET"])
def search_medicine():


    medicine_name = request.args.get("medicine_name")
    conn = get_connection()
    cursor = conn.cursor()
    print("DB Connected",conn)
    
    query = """
    SELECT * FROM medicines
    WHERE medicine_name = %s
    """

        
    cursor.execute(query, (medicine_name,))
    output = cursor.fetchall()
    print(output)
    
    cursor.close()
    conn.close()
    
    return  jsonify(output)

    
    
if __name__ == "__main__":
        app.run(debug=True)