from flask import Flask,render_template,request,flash,redirect,url_for

app = Flask(__name__)
app.secret_key = "key"


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/gallery')
def gallery():
    return render_template("gallery.html")

@app.route('/register',methods=["GET","POST"])
def register():
    if request.method == "POST":
        name = request.form["jina"]
        email = request.form["arafa"]
        password = request.form["siri"]
        receivedData = name+" | "+email+" | "+password
        flash(receivedData)
        return redirect(url_for("register"))
    return render_template("register.html")


if __name__ == '__main__':
    app.run()
