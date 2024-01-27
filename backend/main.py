from flask import Flask,redirect,render_template

# mydatabase connectionn

local_server=True
app=Flask(__name__)
app.secret_key="abdulkhadar"

@app.route("/")
def home():
    return render_template("../frontend/index.html")
app.run(debug=True)