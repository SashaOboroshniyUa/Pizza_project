from flask import Flask, render_template, request, abort


app = Flask(__name__)

CAPTCHA = "abo123"
max_score = 100
rabs = [
  {"name": "Aboba", "score": 100},
  {"name": "aboba_mini", "score": 78},
  {"name": "stager", "score": -1}
]
ban_name = ["Negr", "Gay", "Gomoseksual", "Gayporno", "Porno", "Niger", "Nige", "Nig"]


@app.get('/results/')
def results():
    context = {
        "title": "Results",
        "rabs": rabs,
        "max_score": max_score,
    }
    return render_template("rabs_results.html", **context)


@app.get("/")
def get_captcha():
    return render_template("captcha.html", captcha="Captcha")


@app.post("/index/")
def post_captcha():
    captcha_input = request.form.get("captcha")
    if captcha_input == CAPTCHA:
        return render_template("login.html")
    else:
        return abort(404)


@app.post("/login")
def post_login():
    user = request.form["name"].capitalize()
    if user in ban_name:
        return abort(404)
    else:
        return render_template("index.html", users=user)


@app.get("/about/")
def about():
    return render_template("about.html")


@app.get("/secret_pizza/")
def secret_pizza():
    return render_template("secret_pizza.html")


@app.get("/commands/")
def absolute_rabs():
    return render_template("rabs.html")


if __name__ == "__main__":
    app.run(port=8080, debug=True)
