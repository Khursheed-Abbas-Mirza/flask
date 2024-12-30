from flask import Flask,render_template
app=Flask(__name__, static_folder="static", template_folder="templates")
@app.route('/',methods=["GET"])
def func():
    return render_template("index.html")
if(__name__=="__main__"):
    try:
      app.run()
    except RuntimeError as error:
      print(error)
    