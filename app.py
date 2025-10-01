from flask import Flask, render_template
from shop.routes import shop_bp  # assuming shop/routes.py defines shop_bp

app = Flask(__name__)
app.register_blueprint(shop_bp)

@app.route("/")
def home():
    "return "
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
