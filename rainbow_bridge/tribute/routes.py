from flask import Blueprint, render_template, request, redirect

tribute_bp = Blueprint('tribute', __name__)

tributes = []

@tribute_bp.route('/tribute', methods=['GET', 'POST'])
def tribute_wall():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        tributes.append({'name': name, 'message': message})
        return redirect('/tribute')
    return render_template('tribute.html', tributes=tributes)