from flask import Flask, render_template

app = Flask(__name__)

# Dummy product data (normally DB lo untadi)
products = [
    {"name": "Mobile Phone", "price": "₹1hdgh9378340"},
    {"name": "Laptop", "price": "₹111,000"},
    {"name": "Headphones", "price": "₹2,000"}
]

@app.route("/")
def home():
    return render_template("index.html", products=products)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
