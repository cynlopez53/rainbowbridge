from flask import Blueprint, render_template  # ✅ Import at the top

shop_bp = Blueprint('shop', __name__, url_prefix='/shop')  # ✅ Define blueprint

@shop_bp.route("/")  # ✅ Route for /shop
def shop_home():     # ✅ Function that handles the route
    return render_template("shop.html")  # ✅ Return a template