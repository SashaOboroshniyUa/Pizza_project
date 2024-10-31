from flask import Flask, render_template, request, abort


app = Flask(__name__)

CAPTCHA = "abo123"
max_score = 100
rabs = [
  {"name": "Aboba", "score": 100},
  {"name": "aboba_mini", "score": 78},
  {"name": "stager", "score": -1}
]
menu = [
    {"name": "Pepperoni", "description": "mozzarella, champignons, salami, pesto sauce, tomato sauce, oregano", "price": 60},
    {"name": "Pizza BBQ", "description": "Chicken fillet, smoked brisket, onion, hunting sausages, suluguni, parsley, mozzarella, sauce", "price": 69},
    {"name": "4 Cheeses", "description": "mozzarella cheese, ripe tomatoes and fresh basil leaves", "price": 50},
    {"name": "Diablo", "description": "sausages (Bavarian, Vienna, pepperoni), soft mozzarella cheese, mushrooms, bell pepper", "price": 80}
]
ban_name = ["Negr", "Gay", "Gomoseksual", "Gayporno", "Porno", "Niger", "Nige", "Nig"]
secret_key = "I big love JavaScript & TailWind🥵 and nenavishu React! Please ocenit my project and pashalko!"


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


@app.post("/login/")
def post_login():
    user = request.form["name"].capitalize()
    if user in ban_name:
        return abort(404)
    else:
        return render_template("index.html", users=user)


@app.get("/secret_pizza/")
def secret_pizza():
    return render_template("secret_pizza.html")


@app.post("/secret_pizza/")
def secret_promokod():
    secret_key_input = request.form.get("key")
    if secret_key_input == secret_key:
        return render_template("promokod.html")
    else:
        return abort(404)


@app.get("/menu2/")
def menu2():
    menu_item = {
        "menu": menu
    }
    return render_template("menu2.html", **menu_item)


@app.get("/menu1/")
def menu1():
    menu_item = {
        "menu": menu
    }
    return render_template("menu1.html", **menu_item)


@app.get("/menu3/")
def special_offer():
    return render_template("menu3.html")


if __name__ == "__main__":
    app.run(port=8080, debug=True)
