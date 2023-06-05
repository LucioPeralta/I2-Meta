from flask import Flask, render_template, url_for, request,redirect

app = Flask(__name__, static_folder='static')

@app.route("/", methods=['GET','POST'])
def Home():
    if request.method == "POST":
        nombre = request.form['input_url']
        return render_template('index.html', nombre=nombre)
    else:
        return render_template('index.html')
    

"""@app.route("/search", methods=["POST"])
def Search():
    if request.method == "POST":
        nombre = request.form['input_url']
        return render_template('index.html', nombre=nombre)
    else:
        return render_template('index.html',nombre)"""


if __name__ == '__main__':
    app.run(debug=True)