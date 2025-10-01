from flask import Flask, render_template
from shop.routes import shop_bp  # assuming shop/routes.py defines shop_bp

app = Flask(__name__)
app.register_blueprint(shop_bp)

@app.route("/")
def home():
    return "Rainbow Bridge is alive 🌈"

# 🔥 This goes at the very bottom
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)