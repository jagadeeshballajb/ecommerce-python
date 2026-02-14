from flask import Flask, render_template

app = Flask(__name__)

# Dummy product data (normally DB lo untadi)
products = [
    {"name": "Mobile Phone", "price": "Buy one get one free"},
    {"name": "Laptop", "price": "Free"},
    {"name": "Charger", "price": "Free"}
    {"name": "TAB", "price": "Free"}
]

@app.route("/")
def home():
    return render_template("index.html", products=products)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
