from flask import Flask,render_template
app=Flask(__name__, static_folder="static", template_folder="templates")
@app.route('/')
def func():
    return render_template("index.html")

app.run(debug=True)