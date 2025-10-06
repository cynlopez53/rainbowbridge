from flask import Blueprint, render_template  # ✅ Import at the top

shop_bp = Blueprint('shop', __name__, url_prefix='/shop')  # ✅ Define blueprint

@shop_bp.route("/")  # ✅ Route for /shop
def shop_home():     # ✅ Function that handles the route
    return render_template("shop.html")  # ✅ Return a template
vent_posts = []

@shop_bp.route('/vent', methods=["GET", "POST"])
def vent():
    if request.method == "POST":
        story = request.form["story"]
        vent_posts.append(story)
        return redirect("/shop/vent")
    return render_template("vent.html", vent_posts=vent_posts)