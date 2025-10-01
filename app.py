from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__, template_folder="templates", static_folder="templates/static")

# Home route
@app.route("/")
def home():
    return render_template("tribute_wall.html")

# Shop route
@app.route("/shop")
def shop():
    return render_template("shop.html")

# Example route for handling purchases (expand later with Stripe or Google Play)
@app.route("/purchase", methods=["POST"])
def purchase():
    item = request.form.get("item")
    # Placeholder logic — replace with real payment integration
    return f"Thank you for purchasing {item}!"

# Health check route (optional for Render)
@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)