from flask import Flask

app = Flask(__name__)

@app.route("/")
def provar():
    return("<h1>aleluia</h1>")

@app.route("/aa")
def provado():
    return("<h1>Amem</h1>")

if __name__ == "__main__":

    app.run()
    