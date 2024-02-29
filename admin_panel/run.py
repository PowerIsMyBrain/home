from flask import Flask, render_template, redirect, url_for, flash, jsonify, session, request
from flask_wtf import FlaskForm
from flask_paginate import Pagination, get_page_args
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from werkzeug.utils import secure_filename
import secrets
import app.utils.passwordSalt as hash
from temp import daneDBList, subsDataDB, userDataDB, teamDB
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
app.config['PER_PAGE'] = 5  # Określa liczbę elementów na stronie

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
        brands_data = {}
        for un in userDataDB: 
            usersTempDict[un['username']] = {
                'hashed_password': un['password'],
                'salt': un['salt']
            }
            permTempDict[un['username']] = un['uprawnienia']
            users_data[un['username']] = {
                'id': un['id'], 
                'username': un['username'],  
                'email': un['email'],
                'phone': un['phone'],
                'facebook': un['facebook'],
                'linkedin': un['linkedin'],
                'name': un['name'], 
                'stanowisko': un['stanowisko'],
                'opis': un['opis'],
                'status': un['status'],
                'avatar': un['avatar']
            }
            brands_data[un['username']] = un['brands']

        # weryfikacja danych użytkownika
        if username in usersTempDict and \
            hash.hash_password(
                password, usersTempDict[username]['salt']
                ) == usersTempDict[username]['hashed_password']:
            session['username'] = username
            session['userperm'] = permTempDict[username]
            session['user_data'] = users_data[username]
            session['brands'] = brands_data[username]

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
    
    # try:
    #     users_data = users(False)[0]
    # except Exception as e:
    #     flash(f"Błąd! {e}", "error")
    #     return redirect(url_for('blog'))
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

@app.route('/team-domy', methods=['GET', 'POST'])
def team_domy():
    """Strona zespołu domy."""
    # Sprawdzenie czy użytkownik jest zalogowany, jeśli nie - przekierowanie do strony głównej
    if 'username' not in session:
        return redirect(url_for('index'))
    
    if session['userperm']['team'] == 0:
        flash('Nie masz uprawnień do zarządzania tymi zasobami. Skontaktuj sie z administratorem!')
        return redirect(url_for('index'))
    
    curent_settings_team = teamDB
    users_atributes = {}
    assigned_dmddomy = []
    
    for usr_d in userDataDB:
        u_name = usr_d['name']
        u_login = usr_d['username']
        users_atributes[u_name] = usr_d
        if usr_d['brands']['domy'] == 1:
            assigned_dmddomy.append(u_login)

    collections = {
            'domy': {
                'home': [],
                'team': [],
                'available': []
            }
        }

    employee_photo_dict = {}

    i_domy = 1 
    for employees in curent_settings_team:
        group = employees['EMPLOYEE_DEPARTMENT']
        department = str(group).replace('dmd ', '')
        employee = employees['EMPLOYEE_NAME']
        employee_login = users_atributes[employee]['username']

        employee_photo = users_atributes[employee]['avatar']
        try: employee_photo_dict[employee_login]
        except KeyError: employee_photo_dict[employee_login] = employee_photo
        
        if i_domy < 5 and department == "domy":
            collections[department]['home'].append(employee_login)
        elif i_domy >= 5 and department == "domy":
            collections[department]['team'].append(employee_login)
        if department == 'domy':
            i_domy += 1
        
    for assign in assigned_dmddomy:
        if assign not in collections['domy']['home'] + collections['domy']['team']:
            collections['domy']['available'].append(assign)

            for row in userDataDB:
                if row['username'] == assign:
                    employee_photo = row['avatar']
                    try: employee_photo_dict[assign]
                    except KeyError: employee_photo_dict[assign] = employee_photo

    # Tutaj złapane dane
    if request.method == 'POST':
        data = request.get_json()
        sequence_data = data.get('sequence', [])
        sequence = []
        for s in sequence_data:
            clear_data = s.strip()
            sequence.append(clear_data)

        users_atributesByLogin = {}
        for usr_d in userDataDB:
            u_login = usr_d['username']
            users_atributesByLogin[u_login] = usr_d
        
        ready_exportDB = []
        for u_login in sequence:
            set_row = {
                'EMPLOYEE_PHOTO': users_atributesByLogin[u_login]['avatar'],
                'EMPLOYEE_NAME': users_atributesByLogin[u_login]['name'],
                'EMPLOYEE_ROLE': users_atributesByLogin[u_login]['stanowisko'],
                'EMPLOYEE_DEPARTMENT': 'dmd domy',
                'PHONE': users_atributesByLogin[u_login]['phone'],
                'EMAIL': users_atributesByLogin[u_login]['email'],
                'FACEBOOK': users_atributesByLogin[u_login]['facebook'],
                'LINKEDIN': users_atributesByLogin[u_login]['linkedin'],
                'STATUS': 1
            }
            ready_exportDB.append(set_row)
        # 1. usuń wszystkie pozycje dla EMPLOYEE_DEPARTMENT
        # 2. wstaw nowe dane do bazy zachowując kolejność zapisu w bazie

        print('dane:', ready_exportDB)

    return render_template(
                            "team_management_domy.html", 
                            userperm=session['userperm'], 
                            user_brands=session['brands'], 
                            members=collections['domy'], 
                            photos_dict=employee_photo_dict)

@app.route('/team-elitehome', methods=['GET', 'POST'])
def team_elitehome():
    """Strona zespołu elitehome."""
    # Sprawdzenie czy użytkownik jest zalogowany, jeśli nie - przekierowanie do strony głównej
    if 'username' not in session:
        return redirect(url_for('index'))
    
    if session['userperm']['team'] == 0:
        flash('Nie masz uprawnień do zarządzania tymi zasobami. Skontaktuj sie z administratorem!')
        return redirect(url_for('index'))
    
    curent_settings_team = teamDB
    users_atributes = {}
    
    assigned_dmdelitehome = []
    for usr_d in userDataDB:
        u_name = usr_d['name']
        u_login = usr_d['username']
        users_atributes[u_name] = usr_d
        
        if usr_d['brands']['elitehome'] == 1:
            assigned_dmdelitehome.append(u_login)
        
    collections = {
            'elitehome': {
                'home': [],
                'team': [],
                'available': []
            }
    }
    employee_photo_dict = {}
    i_elitehome = 1
    for employees in curent_settings_team:
        group = employees['EMPLOYEE_DEPARTMENT']
        department = str(group).replace('dmd ', '')
        employee = employees['EMPLOYEE_NAME']
        employee_login = users_atributes[employee]['username']

        employee_photo = users_atributes[employee]['avatar']
        try: employee_photo_dict[employee_login]
        except KeyError: employee_photo_dict[employee_login] = employee_photo

        if i_elitehome < 5 and department == "elitehome":
            collections[department]['home'].append(employee_login)
        elif i_elitehome >= 5 and department == "elitehome":
            collections[department]['team'].append(employee_login)
        if department == 'elitehome':
            i_elitehome += 1
    
    for assign in assigned_dmdelitehome:
        if assign not in collections['elitehome']['home'] + collections['elitehome']['team']:
            collections['elitehome']['available'].append(assign)

            for row in userDataDB:
                if row['username'] == assign:
                    employee_photo = row['avatar']
                    try: employee_photo_dict[assign]
                    except KeyError: employee_photo_dict[assign] = employee_photo

    # Tutaj złapane dane
    if request.method == 'POST':
        data = request.get_json()
        sequence_data = data.get('sequence', [])
        sequence = []
        for s in sequence_data:
            clear_data = s.strip()
            sequence.append(clear_data)

        users_atributesByLogin = {}
        for usr_d in userDataDB:
            u_login = usr_d['username']
            users_atributesByLogin[u_login] = usr_d
        
        ready_exportDB = []
        for u_login in sequence:
            set_row = {
                'EMPLOYEE_PHOTO': users_atributesByLogin[u_login]['avatar'],
                'EMPLOYEE_NAME': users_atributesByLogin[u_login]['name'],
                'EMPLOYEE_ROLE': users_atributesByLogin[u_login]['stanowisko'],
                'EMPLOYEE_DEPARTMENT': 'dmd elitehome',
                'PHONE': users_atributesByLogin[u_login]['phone'],
                'EMAIL': users_atributesByLogin[u_login]['email'],
                'FACEBOOK': users_atributesByLogin[u_login]['facebook'],
                'LINKEDIN': users_atributesByLogin[u_login]['linkedin'],
                'STATUS': 1
            }
            ready_exportDB.append(set_row)
        # 1. usuń wszystkie pozycje dla EMPLOYEE_DEPARTMENT
        # 2. wstaw nowe dane do bazy zachowując kolejność zapisu w bazie

        print('dane:', ready_exportDB)

    return render_template(
                            "team_management_elitehome.html", 
                            userperm=session['userperm'], 
                            user_brands=session['brands'],  
                            members=collections['elitehome'], 
                            photos_dict=employee_photo_dict)

@app.route('/team-budownictwo', methods=['GET', 'POST'])
def team_budownictwo():
    """Strona zespołu budownictwo."""
    # Sprawdzenie czy użytkownik jest zalogowany, jeśli nie - przekierowanie do strony głównej
    if 'username' not in session:
        return redirect(url_for('index'))
    
    if session['userperm']['team'] == 0:
        flash('Nie masz uprawnień do zarządzania tymi zasobami. Skontaktuj sie z administratorem!')
        return redirect(url_for('index'))
    
    curent_settings_team = teamDB
    users_atributes = {}

    assigned_dmdbudownictwo = []

    for usr_d in userDataDB:
        u_name = usr_d['name']
        u_login = usr_d['username']
        users_atributes[u_name] = usr_d
        if usr_d['brands']['budownictwo'] == 1:
            assigned_dmdbudownictwo.append(u_login)

    collections = {
        'budownictwo': {
            'home': [],
            'team': [],
            'available': []
        }
    }

    employee_photo_dict = {}
    i_budownictwo = 1
    for employees in curent_settings_team:
        group = employees['EMPLOYEE_DEPARTMENT']
        department = str(group).replace('dmd ', '')
        employee = employees['EMPLOYEE_NAME']
        employee_login = users_atributes[employee]['username']

        employee_photo = users_atributes[employee]['avatar']
        try: employee_photo_dict[employee_login]
        except KeyError: employee_photo_dict[employee_login] = employee_photo

        if i_budownictwo < 5 and department == "budownictwo":
            collections[department]['home'].append(employee_login)
        elif i_budownictwo >= 5 and department == "budownictwo":
            collections[department]['team'].append(employee_login)
        if department == 'budownictwo':
            i_budownictwo += 1

    for assign in assigned_dmdbudownictwo:
        if assign not in collections['budownictwo']['home'] + collections['budownictwo']['team']:
            collections['budownictwo']['available'].append(assign)

            for row in userDataDB:
                if row['username'] == assign:
                    employee_photo = row['avatar']
                    try: employee_photo_dict[assign]
                    except KeyError: employee_photo_dict[assign] = employee_photo

    # Tutaj złapane dane
    if request.method == 'POST':
        data = request.get_json()
        sequence_data = data.get('sequence', [])
        sequence = []
        for s in sequence_data:
            clear_data = s.strip()
            sequence.append(clear_data)

        users_atributesByLogin = {}
        for usr_d in userDataDB:
            u_login = usr_d['username']
            users_atributesByLogin[u_login] = usr_d
        
        ready_exportDB = []
        for u_login in sequence:
            set_row = {
                'EMPLOYEE_PHOTO': users_atributesByLogin[u_login]['avatar'],
                'EMPLOYEE_NAME': users_atributesByLogin[u_login]['name'],
                'EMPLOYEE_ROLE': users_atributesByLogin[u_login]['stanowisko'],
                'EMPLOYEE_DEPARTMENT': 'dmd budownictwo',
                'PHONE': users_atributesByLogin[u_login]['phone'],
                'EMAIL': users_atributesByLogin[u_login]['email'],
                'FACEBOOK': users_atributesByLogin[u_login]['facebook'],
                'LINKEDIN': users_atributesByLogin[u_login]['linkedin'],
                'STATUS': 1
            }
            ready_exportDB.append(set_row)
        # 1. usuń wszystkie pozycje dla EMPLOYEE_DEPARTMENT
        # 2. wstaw nowe dane do bazy zachowując kolejność zapisu w bazie

        print('dane:', ready_exportDB)
    return render_template(
                            "team_management_budownictwo.html", 
                            userperm=session['userperm'], 
                            user_brands=session['brands'],  
                            members=collections['budownictwo'], 
                            photos_dict=employee_photo_dict)

@app.route('/team-development', methods=['GET', 'POST'])
def team_development():
    """Strona zespołu development."""
    # Sprawdzenie czy użytkownik jest zalogowany, jeśli nie - przekierowanie do strony głównej
    if 'username' not in session:
        return redirect(url_for('index'))
    
    if session['userperm']['team'] == 0:
        flash('Nie masz uprawnień do zarządzania tymi zasobami. Skontaktuj sie z administratorem!')
        return redirect(url_for('index'))
    
    curent_settings_team = teamDB
    users_atributes = {}
    assigned_dmddevelopment = []
    for usr_d in userDataDB:
        u_name = usr_d['name']
        u_login = usr_d['username']
        users_atributes[u_name] = usr_d
        
        if usr_d['brands']['development'] == 1:
            assigned_dmddevelopment.append(u_login)


    collections = {
        'development': {
            'home': [],
            'team': [],
            'available': []
        }
    }
    
    employee_photo_dict = {}
    i_development = 1
    for employees in curent_settings_team:
        group = employees['EMPLOYEE_DEPARTMENT']
        department = str(group).replace('dmd ', '')
        employee = employees['EMPLOYEE_NAME']
        employee_login = users_atributes[employee]['username']

        employee_photo = users_atributes[employee]['avatar']
        try: employee_photo_dict[employee_login]
        except KeyError: employee_photo_dict[employee_login] = employee_photo

        if i_development < 5 and department == "development":
            collections[department]['home'].append(employee_login)
        elif i_development >= 5 and department == "development":
            collections[department]['team'].append(employee_login)
        if department == 'development':
            i_development += 1

    for assign in assigned_dmddevelopment:
        if assign not in collections['development']['home'] + collections['development']['team']:
            collections['development']['available'].append(assign)

            for row in userDataDB:
                if row['username'] == assign:
                    employee_photo = row['avatar']
                    try: employee_photo_dict[assign]
                    except KeyError: employee_photo_dict[assign] = employee_photo

    # Tutaj złapane dane
    if request.method == 'POST':
        data = request.get_json()
        sequence_data = data.get('sequence', [])
        sequence = []
        for s in sequence_data:
            clear_data = s.strip()
            sequence.append(clear_data)

        users_atributesByLogin = {}
        for usr_d in userDataDB:
            u_login = usr_d['username']
            users_atributesByLogin[u_login] = usr_d
        
        ready_exportDB = []
        for u_login in sequence:
            set_row = {
                'EMPLOYEE_PHOTO': users_atributesByLogin[u_login]['avatar'],
                'EMPLOYEE_NAME': users_atributesByLogin[u_login]['name'],
                'EMPLOYEE_ROLE': users_atributesByLogin[u_login]['stanowisko'],
                'EMPLOYEE_DEPARTMENT': 'dmd development',
                'PHONE': users_atributesByLogin[u_login]['phone'],
                'EMAIL': users_atributesByLogin[u_login]['email'],
                'FACEBOOK': users_atributesByLogin[u_login]['facebook'],
                'LINKEDIN': users_atributesByLogin[u_login]['linkedin'],
                'STATUS': 1
            }
            ready_exportDB.append(set_row)
        # 1. usuń wszystkie pozycje dla EMPLOYEE_DEPARTMENT
        # 2. wstaw nowe dane do bazy zachowując kolejność zapisu w bazie

        print('dane:', ready_exportDB)
    return render_template(
                            "team_management_development.html", 
                            userperm=session['userperm'], 
                            user_brands=session['brands'],  
                            members=collections['development'], 
                            photos_dict=employee_photo_dict)

@app.route('/team-inwestycje', methods=['GET', 'POST'])
def team_investment():
    """Strona zespołu."""
    # Sprawdzenie czy użytkownik jest zalogowany, jeśli nie - przekierowanie do strony głównej
    if 'username' not in session:
        return redirect(url_for('index'))
    
    if session['userperm']['team'] == 0:
        flash('Nie masz uprawnień do zarządzania tymi zasobami. Skontaktuj sie z administratorem!')
        return redirect(url_for('index'))
    
    curent_settings_team = teamDB
    users_atributes = {}
    
    assigned_dmdinvestment = []
    for usr_d in userDataDB:
        u_name = usr_d['name']
        u_login = usr_d['username']
        users_atributes[u_name] = usr_d
        
        if usr_d['brands']['inwestycje'] == 1:
            assigned_dmdinvestment.append(u_login)

    collections = {
        'inwestycje': {
            'home': [],
            'team': [],
            'available': []
        }
    }

    employee_photo_dict = {}
    i_investment = 1
    for employees in curent_settings_team:
        group = employees['EMPLOYEE_DEPARTMENT']
        department = str(group).replace('dmd ', '')
        employee = employees['EMPLOYEE_NAME']
        employee_login = users_atributes[employee]['username']

        employee_photo = users_atributes[employee]['avatar']
        try: employee_photo_dict[employee_login]
        except KeyError: employee_photo_dict[employee_login] = employee_photo

       
        if i_investment < 5 and department == "investment":
            collections[department]['home'].append(employee_login)
        elif i_investment >= 5 and department == "investment":
            collections[department]['team'].append(employee_login)
        if department == 'investment':
            i_investment += 1
    
    for assign in assigned_dmdinvestment:
        if assign not in collections['inwestycje']['home'] + collections['inwestycje']['team']:
            collections['inwestycje']['available'].append(assign)

            for row in userDataDB:
                if row['username'] == assign:
                    employee_photo = row['avatar']
                    try: employee_photo_dict[assign]
                    except KeyError: employee_photo_dict[assign] = employee_photo

    # Tutaj złapane dane
    if request.method == 'POST':
        data = request.get_json()
        sequence_data = data.get('sequence', [])
        sequence = []
        for s in sequence_data:
            clear_data = s.strip()
            sequence.append(clear_data)

        users_atributesByLogin = {}
        for usr_d in userDataDB:
            u_login = usr_d['username']
            users_atributesByLogin[u_login] = usr_d
        
        ready_exportDB = []
        for u_login in sequence:
            set_row = {
                'EMPLOYEE_PHOTO': users_atributesByLogin[u_login]['avatar'],
                'EMPLOYEE_NAME': users_atributesByLogin[u_login]['name'],
                'EMPLOYEE_ROLE': users_atributesByLogin[u_login]['stanowisko'],
                'EMPLOYEE_DEPARTMENT': 'dmd inwestycje',
                'PHONE': users_atributesByLogin[u_login]['phone'],
                'EMAIL': users_atributesByLogin[u_login]['email'],
                'FACEBOOK': users_atributesByLogin[u_login]['facebook'],
                'LINKEDIN': users_atributesByLogin[u_login]['linkedin'],
                'STATUS': 1
            }
            ready_exportDB.append(set_row)
        # 1. usuń wszystkie pozycje dla EMPLOYEE_DEPARTMENT
        # 2. wstaw nowe dane do bazy zachowując kolejność zapisu w bazie

        print('dane:', ready_exportDB)
    return render_template(
                            "team_management_inwestycje.html", 
                            userperm=session['userperm'], 
                            user_brands=session['brands'],  
                            members=collections['inwestycje'], 
                            photos_dict=employee_photo_dict)

@app.route('/team-instalacje', methods=['GET', 'POST'])
def team_instalacje():
    """Strona zespołu instalacje."""
    # Sprawdzenie czy użytkownik jest zalogowany, jeśli nie - przekierowanie do strony głównej
    if 'username' not in session:
        return redirect(url_for('index'))
    
    if session['userperm']['team'] == 0:
        flash('Nie masz uprawnień do zarządzania tymi zasobami. Skontaktuj sie z administratorem!')
        return redirect(url_for('index'))
    
    curent_settings_team = teamDB
    users_atributes = {}
    assigned_dmdinstalacje = []
    for usr_d in userDataDB:
        u_name = usr_d['name']
        u_login = usr_d['username']
        users_atributes[u_name] = usr_d
        
        if usr_d['brands']['instalacje'] == 1:
            assigned_dmdinstalacje.append(u_login)

    collections = {
        'instalacje': {
            'home': [],
            'team': [],
            'available': []
        }
    }

    employee_photo_dict = {}
    i_instalacje = 1

    for employees in curent_settings_team:
        group = employees['EMPLOYEE_DEPARTMENT']
        department = str(group).replace('dmd ', '')
        employee = employees['EMPLOYEE_NAME']
        employee_login = users_atributes[employee]['username']

        employee_photo = users_atributes[employee]['avatar']
        try: employee_photo_dict[employee_login]
        except KeyError: employee_photo_dict[employee_login] = employee_photo

        if i_instalacje < 5 and department == "instalacje":
            collections[department]['home'].append(employee_login)
        elif i_instalacje >= 5 and department == "instalacje":
            collections[department]['team'].append(employee_login)
        if department == 'instalacje':
            i_instalacje += 1

    for assign in assigned_dmdinstalacje:
        if assign not in collections['instalacje']['home'] + collections['instalacje']['team']:
            collections['instalacje']['available'].append(assign)

            for row in userDataDB:
                if row['username'] == assign:
                    employee_photo = row['avatar']
                    try: employee_photo_dict[assign]
                    except KeyError: employee_photo_dict[assign] = employee_photo

    # Tutaj złapane dane
    if request.method == 'POST':
        data = request.get_json()
        sequence_data = data.get('sequence', [])
        sequence = []
        for s in sequence_data:
            clear_data = s.strip()
            sequence.append(clear_data)

        users_atributesByLogin = {}
        for usr_d in userDataDB:
            u_login = usr_d['username']
            users_atributesByLogin[u_login] = usr_d
        
        ready_exportDB = []
        for u_login in sequence:
            set_row = {
                'EMPLOYEE_PHOTO': users_atributesByLogin[u_login]['avatar'],
                'EMPLOYEE_NAME': users_atributesByLogin[u_login]['name'],
                'EMPLOYEE_ROLE': users_atributesByLogin[u_login]['stanowisko'],
                'EMPLOYEE_DEPARTMENT': 'dmd instalacje',
                'PHONE': users_atributesByLogin[u_login]['phone'],
                'EMAIL': users_atributesByLogin[u_login]['email'],
                'FACEBOOK': users_atributesByLogin[u_login]['facebook'],
                'LINKEDIN': users_atributesByLogin[u_login]['linkedin'],
                'STATUS': 1
            }
            ready_exportDB.append(set_row)
        # 1. usuń wszystkie pozycje dla EMPLOYEE_DEPARTMENT
        # 2. wstaw nowe dane do bazy zachowując kolejność zapisu w bazie

        print('dane:', ready_exportDB)
    return render_template(
                            "team_management_instalacje.html", 
                            userperm=session['userperm'], 
                            user_brands=session['brands'],  
                            members=collections['instalacje'], 
                            photos_dict=employee_photo_dict)






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