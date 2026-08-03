print("Python file started successfully")

from flask import Flask, request, send_file, Response
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
    print("search_medicine called")
    data = request.json

    medicine_name = data["medicine_name"]
    conn = get_connection()
    cursor = conn.cursor()
    print("DB Connected",conn)
    
    query = """
    SELECT * FROM medicines
    WHERE medicine_name = %s
    """
    print(output)

        
    cursor.execute(query, values)
    conn.commit()
    
    cursor.close()
    conn.close()
    
    return "Medicine Saved Successfully"
    
    
    if __name__ == "__main__":
        app.run(debug=True)