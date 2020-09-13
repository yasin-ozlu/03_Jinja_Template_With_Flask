from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def head():
    return render_template("index.html", number1 = 32, number2 = 34)

@app.route("/about")
def second():
    return render_template("about.html", prepared_by = "Yasin")


if(__name__) == "__main__":
    app.run(debug=True)
