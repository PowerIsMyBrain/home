from flask import Flask, render_template, redirect, url_for, flash, jsonify, session, request
from flask_wtf import FlaskForm
from flask_paginate import Pagination, get_page_args
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from werkzeug.utils import secure_filename
import secrets
import app.utils.passwordSalt as hash
from temp import usersDB, daneDBList, subsDataDB, userDataDB
import time

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
app.config['PER_PAGE'] = 2  # Określa liczbę elementów na stronie

class LoginForm(FlaskForm):
    username = StringField('Nazwa użytkownika', validators=[DataRequired()])
    password = PasswordField('Hasło', validators=[DataRequired()])
    submit = SubmitField('Zaloguj się')

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif', 'webp'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    if 'username' in session:
        # username = session['username']
        return redirect(url_for('home'))
    return render_template('gateway.html', form=LoginForm())

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        usersTempDict = {}
        permTempDict = {}
        users_data = {}
        for un in userDataDB: 
            usersTempDict[un['username']] = {
                'hashed_password': un['password'],
                'salt': un['salt']
            }
            permTempDict[un['username']] = un['uprawnienia']
            users_data[un['username']] = {
                'id': un['uprawnienia'], 
                'username': un['username'],  
                'email': un['email'],
                'name': un['name'], 
                'stanowisko': un['stanowisko'],
                'opis': un['opis'],
                'status': un['status'],
                'avatar': un['avatar']
            }

        # weryfikacja danych użytkownika
        if username in usersTempDict and \
            hash.hash_password(
                password, usersTempDict[username]['salt']
                ) == usersTempDict[username]['hashed_password']:
            session['username'] = username
            session['userperm'] = permTempDict[username]
            session['user_data'] = users_data[username]

            return redirect(url_for('index'))
        else:
            flash('Błędne nazwa użytkownika lub hasło')

    return render_template('gateway.html', form=form)

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('userperm', None)
    session.pop('user_data', None)

    return redirect(url_for('index'))

@app.route('/home')
def home():
    """Strona główna."""
    # Sprawdzenie czy użytkownik jest zalogowany, jeśli nie - przekierowanie do strony głównej    
    if 'username' not in session:
        return redirect(url_for('index'))
    
    try:
        users_data = users(False)[0]
    except Exception as e:
        flash(f"Błąd! {e}", "error")
        return redirect(url_for('blog'))
    print(session['username'])
    return render_template("home.html", userperm=session['userperm'], username=session['username'], users_data=session['user_data'])

@app.route('/blog')
def blog(router=True):
    """Strona z zarządzaniem blogiem."""
    # Sprawdzenie czy użytkownik jest zalogowany, jeśli nie - przekierowanie do strony głównej
    if 'username' not in session or 'userperm' not in session:
        return redirect(url_for('index'))
    
    if session['userperm']['blog'] == 0:
        flash('Nie masz uprawnień do zarządzania tymi zasobami. Skontaktuj sie z administratorem!')
        return redirect(url_for('index'))
    
    # Wczytanie listy wszystkich postów z bazy danych i przypisanie jej do zmiennej posts
    all_posts = daneDBList

    # Ustawienia paginacji
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    total = len(all_posts)
    pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')

    # Pobierz tylko odpowiednią ilość postów na aktualnej stronie
    posts = all_posts[offset: offset + per_page]
    if router:
        # Renderowanie szablonu blog-managment.html z danymi o postach (wszystkimi lub po jednym)
        return render_template("blog_management.html", posts=posts, username=session['username'], userperm=session['userperm'], pagination=pagination)
    else:
        return posts, session['username'], session['userperm'], pagination

@app.route('/save-blog-post', methods=['GET', 'POST'])
def save_post():
    """Strona zapisywania edytowanego posta."""
    # print(blog(False))
    
    try:
        posts, username, userperm, pagination = blog(False)
    except Exception as e:
        flash(f"Błąd! {e}", "error")
        return redirect(url_for('blog'))
    
    # Sprawdzenie czy użytkownik jest zalogowany, jeśli nie - przekierowanie do strony głównej
    if 'username' not in session or 'userperm' not in session:
        return redirect(url_for('index'))
    
    if session['userperm']['blog'] == 0:
        flash('Nie masz uprawnień do zarządzania tymi zasobami. Skontaktuj sie z administratorem!')
        return redirect(url_for('index'))
    
    # Obsługa formularza POST
    if request.method == 'POST':
        form_data = request.form.to_dict()
        set_form_id = None
        print(form_data)
        # Znajdź id posta
        for key in form_data.keys():
            if '_' in key:
                set_form_id = key.split('_')[1]
                try: 
                    int(set_form_id)
                    break
                except ValueError:
                    set_form_id = None
        if set_form_id == '9999999':
            new_post = True
            set_form_id = None
            print(f"procedura dodawania nowego posta = {new_post}" )
            flash(f"procedura dodawania nowego posta = {new_post}" )

            return render_template("blog_management.html", posts=posts, username=username, userperm=userperm, pagination=pagination)

        # Sprawdzenie czy udało się ustalić id posta
        if not set_form_id:
            flash('Ustalenie id posta okazało się niemożliwe')
            return render_template("blog_management.html", posts=posts, username=username, userperm=userperm, pagination=pagination)
        
        # Przygotowanie ścieżki do zapisu plików
        upload_path = '../'

        # Obsługa Main Foto
        main_foto = request.files.get(f'mainFoto_{set_form_id}')
        if main_foto and allowed_file(main_foto.filename):
            filename = str(int(time.time())) + secure_filename(main_foto.filename)
            main_foto.save(upload_path + filename)

        # Obsługa Content Foto
        content_foto = request.files.get(f'contentFoto_{set_form_id}')
        if content_foto and allowed_file(content_foto.filename):
            filename = str(int(time.time())) + secure_filename(content_foto.filename)
            content_foto.save(upload_path + filename)

        flash('Dane zostały zapisane poprawnie!')
        print('Dane zostały zapisane poprawnie!')
        print(form_data)
        return render_template("blog_management.html", posts=posts, username=username, userperm=userperm, pagination=pagination)
    
    return redirect(url_for('index'))

@app.route('/remove-post')
def remove_post():
    """Usuwanie bloga"""
    # Sprawdzenie czy użytkownik jest zalogowany, jeśli nie - przekierowanie do strony głównej
    if 'username' not in session or 'userperm' not in session:
        return redirect(url_for('index'))
    
    if session['userperm']['blog'] == 0:
        flash('Nie masz uprawnień do zarządzania tymi zasobami. Skontaktuj sie z administratorem!')
        return redirect(url_for('index'))
    
    return render_template("home.html", userperm=session['userperm'])

@app.route('/remove-comment')
def remove_comment():
    """Usuwanie komentarza"""
    # Sprawdzenie czy użytkownik jest zalogowany, jeśli nie - przekierowanie do strony głównej
    if 'username' not in session:
        return redirect(url_for('index'))
    
    return render_template("home.html", userperm=session['userperm'])

@app.route('/user')
def users(router=True):
    """Strona z zarządzaniem użytkownikami."""
    # Sprawdzenie czy użytkownik jest zalogowany, jeśli nie - przekierowanie do strony głównej
    if 'username' not in session or 'userperm' not in session:
        return redirect(url_for('index'))
    
    if session['userperm']['users'] == 0:
        flash('Nie masz uprawnień do zarządzania tymi zasobami. Skontaktuj sie z administratorem!')
        return redirect(url_for('index'))
    
    all_users = userDataDB

    # Ustawienia paginacji
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    total = len(all_users)
    pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')

    # Pobierz tylko odpowiednią ilość postów na aktualnej stronie
    users = all_users[offset: offset + per_page]
    if router:
        # Renderowanie szablonu blog-managment.html z danymi o postach (wszystkimi lub po jednym)
        return render_template("user_management.html", users=users, username=session['username'], userperm=session['userperm'], pagination=pagination)
    else:
        return users, session['username'], session['userperm'], pagination
    

@app.route('/newsletter')
def newsletter():
    """Strona Newslettera."""
    # Sprawdzenie czy użytkownik jest zalogowany, jeśli nie - przekierowanie do strony głównej
    if 'username' not in session or 'userperm' not in session:
        return redirect(url_for('index'))
    
    if session['userperm']['newsletter'] == 0:
        flash('Nie masz uprawnień do zarządzania tymi zasobami. Skontaktuj sie z administratorem!')
        return redirect(url_for('index'))
    
    
    return render_template("newsletter_management.html", userperm=session['userperm'])

@app.route('/team')
def team():
    """Strona zespołu."""
    # Sprawdzenie czy użytkownik jest zalogowany, jeśli nie - przekierowanie do strony głównej
    if 'username' not in session:
        return redirect(url_for('index'))
    
    if session['userperm']['team'] == 0:
        flash('Nie masz uprawnień do zarządzania tymi zasobami. Skontaktuj sie z administratorem!')
        return redirect(url_for('index'))
    
    return render_template("team_management.html", userperm=session['userperm'])

@app.route('/subscriber')
def subscribers(router=True):
    """Strona zawierająca listę subskrybentów Newslettera."""
    # Sprawdzenie czy użytkownik jest zalogowany, jeśli nie - przekierowanie do strony głównej
    if 'username' not in session:
        return redirect(url_for('index'))
    
    if session['userperm']['subscribers'] == 0:
        flash('Nie masz uprawnień do zarządzania tymi zasobami. Skontaktuj sie z administratorem!')
        return redirect(url_for('index'))
    
    subscribers_all = subsDataDB

    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    total = len(subscribers_all)
    pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')

    # Pobierz tylko odpowiednią ilość postów na aktualnej stronie
    subs = subscribers_all[offset: offset + per_page]
    if router:
        # Renderowanie szablonu blog-managment.html z danymi o postach (wszystkimi lub po jednym)
        return render_template("subscriber_management.html", subs=subs, username=session['username'], userperm=session['userperm'], pagination=pagination)
    else:
        return subs, session['username'], pagination


@app.route('/setting')
def settings():
    """Strona z ustawieniami."""
    # Sprawdzenie czy użytkownik jest zalogowany, jeśli nie - przekierowanie do strony głównej
    if 'username' not in session:
        return redirect(url_for('index'))
    
    if session['userperm']['settings'] == 0:
        flash('Nie masz uprawnień do zarządzania tymi zasobami. Skontaktuj sie z administratorem!')
        return redirect(url_for('index'))
    
    return render_template("setting_management.html", userperm=session['userperm'])



if __name__ == '__main__':
    app.run(debug=True, port=8000)