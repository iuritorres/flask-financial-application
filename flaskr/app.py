"""TEST"""


from flask import Flask, render_template

app = Flask(
    import_name=__name__,
    template_folder='templates'
)


@app.get("/")
def home():
    """Return home page element"""

    return render_template("home.html")


@app.get("/about/<name>")
def about(name=None):
    """Return home page element"""

    print(name)
    return render_template("about.html")


# @app.route("/stocks/<stock_id>")
# def stock(stock_id):
#     pass


if __name__ == "__main__":
    app.run()
