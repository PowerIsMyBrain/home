from flask import Flask, render_template, redirect, url_for, flash, jsonify, session, request
from flask_wtf import FlaskForm
from flask_paginate import Pagination, get_page_args
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import secrets
from temp import users, daneDBList

"""
Aplikacja "Admin Panel" stanowi kompleksowe narzędzie do 
zarządzania wieloma witrynami internetowymi skupionymi 
pod marką DMD. Została stworzona w oparciu o framework 
Flask, co pozwala na łatwe dostosowywanie i obsługę. 
Aplikacja oferuje intuicyjny interfejs użytkownika,
umożliwiający administratorom efektywne zarządzanie 
różnymi aspektami stron.
"""
app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)
app.config['PER_PAGE'] = 10  # Określa liczbę elementów na stronie

class LoginForm(FlaskForm):
    username = StringField('Nazwa użytkownika', validators=[DataRequired()])
    password = PasswordField('Hasło', validators=[DataRequired()])
    submit = SubmitField('Zaloguj się')

@app.route('/')
def index():
    if 'username' in session:
        # username = session['username']
        return redirect(url_for('blog_management'))
    return render_template('gateway.html', form=LoginForm())

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('index'))
        else:
            flash('Błędne nazwa użytkownika lub hasło')

    return render_template('gateway.html', form=form)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/blog-managment')
def blog_management():
    """Strona z zarządzaniem blogiem."""
    # Sprawdzenie czy użytkownik jest zalogowany, jeśli nie - przekierowanie do strony głównej
    if 'username' not in session:
        return redirect(url_for('index'))

    # Wczytanie listy wszystkich postów z bazy danych i przypisanie jej do zmiennej posts
    all_posts = daneDBList

    # Ustawienia paginacji
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    total = len(all_posts)
    pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')

    # Pobierz tylko odpowiednią ilość postów na aktualnej stronie
    posts = all_posts[offset: offset + per_page]

    # Renderowanie szablonu blog-managment.html z danymi o postach (wszystkimi lub po jednym)
    return render_template("blog_management.html", posts=posts, username=session['username'], pagination=pagination)

if __name__ == '__main__':
    app.run(debug=True, port=8000)