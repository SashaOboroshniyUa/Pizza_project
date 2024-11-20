from flask import Flask, render_template, request, abort
import sqlite3


app = Flask(__name__)

CAPTCHA = "abo123"
ADMIN_NAME = "Kostya_senior_ananas"
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


@app.get("/get_admin_panel/")
def get_admin_panel():
    return render_template("admin_panel.html")


@app.get("/login/")
def get_login():
    return render_template("index.html")


@app.post("/login/")
def post_login():
    user = request.form["name"].capitalize()
    print(user)
    if user in ban_name:
        print("ban_name")
        return abort(404)
    if user == ADMIN_NAME:
        print("admin_name")
        return render_template("admin_panel.html")
    else:
        print("wadw")
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


@app.get("/menu3/")
def special_offer():
    return render_template("menu3.html")


@app.get('/init/')
def create_pizza():
    try:
        sqlite_connection = sqlite3.connect('sql_admin.db')
        cursor = sqlite_connection.cursor()



        create_table_query = """
                    CREATE TABLE IF NOT EXISTS pizza_db (
                        name TEXT NOT NULL,
                        description TEXT UNIQUE,
                        price REAL
                    );
                    """

        cursor.execute(create_table_query)
    except sqlite3.Error as error:
        print("х", error)

    return render_template("login.html")


@app.post("/admin_panel/")
def add_pizza():
        name = request.form["name"]
        description = request.form["description"]
        price = request.form["price"]

        try:
            sqlite_connection = sqlite3.connect("sql_admin.db")
            cursor = sqlite_connection.cursor()
            insert_query = """INSERT INTO pizza_db
            (name, description, price) 
            VALUES (?, ?, ?);"""
            cursor.execute(insert_query, (name, description, int(price)))
            sqlite_connection.commit()
            print("Добавилось")
        except sqlite3.Error as error:
            print("Проблема: ", error)

        return render_template("index.html")


def get_pizzas():
    sqlite_connection = sqlite3.connect("sql_admin.db")
    try:
        cursor = sqlite_connection.cursor()
        cursor.execute("SELECT * FROM pizza_db")
        pizza = cursor.fetchall()
        return pizza

    except sqlite3.Error as error:
        print("Проблема при запуске меню пицц:", error)

    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Піца отримана")


@app.get("/menu/")
def display_menu():
    try:
        pizzas = get_pizzas()
        return render_template("menu1.html", pizzas=pizzas)
    except Exception as eror:
        print("Ошибка при отображении меню:", eror)
        abort(500)


if __name__ == "__main__":
    app.run(port=8080, debug=True)
