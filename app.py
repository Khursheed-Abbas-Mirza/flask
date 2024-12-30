from flask import Flask,render_template,send_from_directory
app=Flask(__name__)
@app.route('/')
def func():
    return render_template("index.html")
# @app.route('/about')
# def about():
#     name="chotu"
#     return render_template('about.html',name="chotu")
# @app.route('/static/<path:filename>')
# def serve_static_file(filename):
#     print(filename)
#     return send_from_directory(app.static_folder, filename)
app.run(debug=True)