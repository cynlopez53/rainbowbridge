from flask import Blueprint, render_template, request, redirect

shop_bp = Blueprint('shop', __name__, url_prefix='/shop')

tributes = []

@shop_bp.route("/")
def shop_home():
    return render_template("shop.html")

@shop_bp.route('/tribute', methods=["GET", "POST"])
def tribute_wall():
    if request.method == "POST":
        name = request.form["name"]
        message = request.form["message"]
        tributes.append({"name": name, "message": message})
        return redirect("/shop/tribute")
    return render_template("tribute.html", tributes=tributes)
    vent_posts = []

@shop_bp.route('/vent', methods=["GET", "POST"])
def vent():
    if request.method == "POST":
        story = request.form["story"]
        vent_posts.append(story)
        return redirect("/shop/vent")
    return render_template("vent.html", vent_posts=vent_posts)