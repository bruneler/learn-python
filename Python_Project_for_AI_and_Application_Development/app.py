from flask import Flask

app = Flask("My first Application")


@app.route('/')
def hello():
    return "Hallo Welt"

if __name__ == "__main__":
    app.run(debug=True)

