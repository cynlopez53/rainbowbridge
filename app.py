from flask import Flask, render_template, request

app = Flask(__name__)

# Temporary in-memory storage
tributes = []
shop_items = [
    {"name": "Virtual Candle", "price": "2", "category": "Memorial"},
    {"name": "Pet Tribute Poster", "price": "5", "category": "Digital Keepsake"},
    {"name": "RainbowBridge Wallpaper", "price": None, "category": "Free Gift"}
]

@app.route('/', methods=['GET', 'POST'])
def tribute_wall():
    if request.method == 'POST':
        pet_name = request.form.get('pet_name')
        message = request.form.get('message')
        if pet_name and message:
            tributes.append({'pet_name': pet_name, 'message': message})
    return render_template('index.html', tributes=tributes)

@app.route('/shop')
def shop():
    return render_template('shop.html', items=shop_items)

if __name__ == '__main__':
    app.run(debug=True)

