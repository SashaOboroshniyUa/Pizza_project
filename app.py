from flask import Flask, render_template, request


app = Flask(__name__)

CAPTCHA = "abo123"
max_score = 100
rabs = [
  {"name": "Aboba", "score": 100},
  {"name": "aboba_mini", "score": 78},
  {"name": "stager", "score": -1},
]


@app.route('/results/')
def results():
    context = {
        "title": "Results",
        "rabs": rabs,
        "max_score": max_score
    }
    return render_template("rabs_results.html", **context)


@app.get("/")
def get_captcha():
    return render_template("captcha.html", captcha="Captcha")


@app.post("/index/")
def post_captcha():
    captcha_input = request.form.get("captcha")
    if captcha_input == CAPTCHA:
        return render_template("index.html")
    else:
        return render_template("captcha_failed.html")


@app.get("/about/")
def about():
    return render_template("about.html")


@app.get("/secret_pizza/")
def secret_pizza():
    return render_template("secret_pizza.html")


if __name__ == "__main__":
    app.run(port=5001, debug=True)
