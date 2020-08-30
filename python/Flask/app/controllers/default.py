from app import app


@app.route("/") # Define a rota da function (página) abaixo
def index():
    return "Hello World!"