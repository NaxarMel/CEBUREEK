from flask import Blueprint, render_template, request, redirect, flash
from blueprints.utils import create_context, login_user, register_user

authorization_bp = Blueprint('authorization', __name__,
                     template_folder='templates',
                     static_folder='static')


@authorization_bp.route('/authorization', methods=['GET', 'POST'])
def authorization():

    context = create_context('Авторизація')

    if request.method == 'POST':
        if request.form.get('_method') == 'LOGIN':
            email = request.form.get('email')
            password = request.form.get('password')

            # Перевірка наявності користувача та пароля
            if email and password:
                if login_user(email, password):
                    # Успішний вхід
                    flash(f'Вітаємо друже!', 'success')  # Повідомлення про успішний вхід
                    return redirect('/menu')  # Перенаправлення на домашню сторінку
                else:
                    # Невдалий вхід
                    flash('Invalid username or password. Please try again.', 'error')
            else:
                flash('Please enter both username and password.', 'error')
        elif request.form.get('_method') == 'REGISTER':

            username = request.form.get('username')
            email = request.form.get('email')
            password = request.form.get('password')

            if username and email and password:
                try:
                    if register_user(username, email, password):
                        flash('Вітаємо друже!', 'success')
                        return redirect('/')
                except Exception as e:
                    context['error'] = str(e)

    return render_template('authorization.html', **context)
