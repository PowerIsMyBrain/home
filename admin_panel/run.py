from flask import Flask, render_template, redirect, url_for, flash, jsonify, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length
import secrets
from temp import users

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

class LoginForm(FlaskForm):
    username = StringField('Nazwa użytkownika', validators=[DataRequired()])
    password = PasswordField('Hasło', validators=[DataRequired()])
    submit = SubmitField('Zaloguj się')

def get_all_posts():
    # tutaj powinno być zapytanie do bazy danych z pobraniem wszystkich postów.
    # symulacja danych z bazy
    daneDB = {
        1: {
            'title': "Dom Lustrzany: Alucobond w Grze Świateł i Natury",
            'introduction': "Zapraszamy do fascynującej podróży do podwarszawskiego Izabelina, gdzie w otulinie Puszczy Kampinoskiej powstał wyjątkowy Lustrzany Dom. Projekt tego jednorodzinnego budynku, autorstwa Marcina Tomaszewskiego z pracowni REFORM Architekt, to połączenie nowoczesności z naturą, gdzie alucobond odgrywa główną rolę w kreowaniu niezwykłej atmosfery.",
            'highlight': "“ Dom Lustrzany to nie tylko budynek mieszkalny, to interaktywna forma sztuki, w której alucobond staje się magią odbić, łącząc nowoczesność z otaczającym krajobrazem. ”",
            'mainFoto': "https://dmddomy.pl/images/blog/bl-00-1920x750-DomLustrzany.png",
            'contentFoto': "https://dmddomy.pl/images/blog/bl-01-750x430-DomLustrzany-1.png",
            'additionalList': "Alucobond: Lustrzane Odbicie Natury: Dom Lustrzany, o powierzchni 400 m² na dwóch kondygnacjach, opiera się na dwóch bryłach, które płynnie łączą się poziomo. Elewacja dolnej części, niemal w całości pokryta alucobondem - aluminiową płytą kompozytową, nadaje budynkowi charakter lustra. Marcin Tomaszewski, opowiadając o swoim projekcie, podkreśla zalety alucobondu, który imituje lustro, zachowując jednocześnie trwałość i wytrzymałość.#splx#Zanurzenie w Naturze: Alucobond sprawia, że dom staje się niemal niewidoczny, odbijając otaczający las i zlewając się z przyrodą. Biała bryła piętra zdaje się unosić w powietrzu, dzięki czemu granice między budynkiem a naturą stają się nieostrzejsze. To nie tylko dom, ale także interaktywna przestrzeń, gdzie światło i odbicia nadają mu dynamiczną formę.#splx#Trwałość i Niski Wymiar Utrzymania: Alucobond, jako materiał niezwykle twardy i trwały, nie wymaga regularnych odnawiania ani odświeżania. Prosta pielęgnacja, polegająca na umyciu powierzchni czystą wodą, sprawia, że budynek zachowuje swoją estetykę na długie lata.",
            'tags': "#DomLustrzany, #Alucobond, #REFORMArchitekt, #ArchitekturaNowoczesna",
            'category': "Architektura Nowoczesna",
            'data': "22 stycznia 2024",
            'author': 'Michał Kowalski',
            'comments': {
                1: {
                    'message': "Super! Takie domy są jak najlepiej.",
                    'user': 'Mariusz Nowak',
                    'e-mail': 'mariusz@nowak.com',
                    'data-time': '18 lutego 2024'
                },
                2: {
                    'message': "Widzę to już w nowych projektach...",
                    'user': 'Jan Kowalski',
                    'e-mail': 'jan@gmail.com',
                    'data-time': '1 marca 2024'
                },
                3: {
                    'message': "To tak naprawdę ciekawo! Dzięki",
                    'user': 'Roh Kowalski',
                    'e-mail': 'rohk@gmail.com',
                    'data-time': '1 marca 2024'
                }
            }
        },
        2: {
            'title': "Dom Lustrzany",
            'introduction': "Zapraszamy do fascynującej podróży do podwarszawskiego Izabelina.",
            'highlight': "“ Dom Lustrzany to nie tylko budynek mieszkalny, to interaktywna forma sztuki. ”",
            'mainFoto': "https://dmddomy.pl/images/blog/bl-00-1920x750-DomLustrzany.png",
            'contentFoto': "https://dmddomy.pl/images/blog/bl-01-750x430-DomLustrzany-1.png",
            'additionalList': "Alucobond: Lustrzane Odbicie Natury: Dom Lustrzany, o powierzchni 400 m²#splx#Zanurzenie w Naturze: Alucobond sprawia, że dom staje się niemal niewidoczny.#splx#Trwałość i Niski Wymiar Utrzymania: Alucobond, jako materiał niezwykle twardy .",
            'tags': "#DomLustrzany, #ArchitekturaNowoczesna",
            'category': "Architektura Nowoczesna",
            'data': "20 luty 2024",
            'author': 'Piotr Walec',
            'comments': {
                1: {
                    'message': "Jestem zaszokowany! Czy na pewno?",
                    'user': 'Mariusz Kot',
                    'e-mail': 'mariusz@kot.com',
                    'data-time': '18 lutego 2024'
                },
                2: {
                    'message': """Fascynujący projekt! Dom Lustrzany wydaje się być nie tylko miejscem do życia, ale prawdziwym arcydziełem sztuki architektonicznej. Zaskakujące, jak alucobond potrafi połączyć nowoczesność z otaczającym krajobrazem, sprawiając, że budynek staje się niemal częścią natury. Jestem pod wrażeniem tego, jak biała bryła piętra zdaje się unosić w powietrzu, tworząc dynamiczną formę.""",
                    'user': 'Jan Kowalski',
                    'e-mail': 'jan@gmail.com',
                    'data-time': '1 marca 2024'
                },
            }
        },
        3: {
            'title': "Dom Lustrzany",
            'introduction': "Zapraszamy do fascynującej podróży do podwarszawskiego Izabelina.",
            'highlight': "“ Dom Lustrzany to nie tylko budynek mieszkalny, to interaktywna forma sztuki. ”",
            'mainFoto': "https://dmddomy.pl/images/blog/bl-00-1920x750-DomLustrzany.png",
            'contentFoto': "https://dmddomy.pl/images/blog/bl-01-750x430-DomLustrzany-1.png",
            'additionalList': "Alucobond: Lustrzane Odbicie Natury: Dom Lustrzany, o powierzchni 400 m²#splx#Zanurzenie w Naturze: Alucobond sprawia, że dom staje się niemal niewidoczny.#splx#Trwałość i Niski Wymiar Utrzymania: Alucobond, jako materiał niezwykle twardy .",
            'tags': "#DomLustrzany, #ArchitekturaNowoczesna",
            'category': "Architektura Nowoczesna",
            'data': "20 luty 2024",
            'author': 'Piotr Walec',
            'comments': {
                1: {
                    'message': "Jestem zaszokowany! Czy na pewno?",
                    'user': 'Mariusz Kot',
                    'e-mail': 'mariusz@kot.com',
                    'data-time': '18 lutego 2024'
                },
                2: {
                    'message': """Fascynujący projekt! Dom Lustrzany wydaje się być nie tylko miejscem do życia, ale prawdziwym arcydziełem sztuki architektonicznej. Zaskakujące, jak alucobond potrafi połączyć nowoczesność z otaczającym krajobrazem, sprawiając, że budynek staje się niemal częścią natury. Jestem pod wrażeniem tego, jak biała bryła piętra zdaje się unosić w powietrzu, tworząc dynamiczną formę.""",
                    'user': 'Jan Kowalski',
                    'e-mail': 'jan@gmail.com',
                    'data-time': '1 marca 2024'
                },
            }
        },
        4: {
            'title': "Dom Lustrzany",
            'introduction': "Zapraszamy do fascynującej podróży do podwarszawskiego Izabelina.",
            'highlight': "“ Dom Lustrzany to nie tylko budynek mieszkalny, to interaktywna forma sztuki. ”",
            'mainFoto': "https://dmddomy.pl/images/blog/bl-00-1920x750-DomLustrzany.png",
            'contentFoto': "https://dmddomy.pl/images/blog/bl-01-750x430-DomLustrzany-1.png",
            'additionalList': "Alucobond: Lustrzane Odbicie Natury: Dom Lustrzany, o powierzchni 400 m²#splx#Zanurzenie w Naturze: Alucobond sprawia, że dom staje się niemal niewidoczny.#splx#Trwałość i Niski Wymiar Utrzymania: Alucobond, jako materiał niezwykle twardy .",
            'tags': "#DomLustrzany, #ArchitekturaNowoczesna",
            'category': "Architektura Nowoczesna",
            'data': "20 luty 2024",
            'author': 'Piotr Walec',
            'comments': {
                1: {
                    'message': "Jestem zaszokowany! Czy na pewno?",
                    'user': 'Mariusz Kot',
                    'e-mail': 'mariusz@kot.com',
                    'data-time': '18 lutego 2024'
                },
                2: {
                    'message': """Fascynujący projekt! Dom Lustrzany wydaje się być nie tylko miejscem do życia, ale prawdziwym arcydziełem sztuki architektonicznej. Zaskakujące, jak alucobond potrafi połączyć nowoczesność z otaczającym krajobrazem, sprawiając, że budynek staje się niemal częścią natury. Jestem pod wrażeniem tego, jak biała bryła piętra zdaje się unosić w powietrzu, tworząc dynamiczną formę.""",
                    'user': 'Jan Kowalski',
                    'e-mail': 'jan@gmail.com',
                    'data-time': '1 marca 2024'
                },
            }
        },
        5: {
            'title': "Dom Lustrzany",
            'introduction': "Zapraszamy do fascynującej podróży do podwarszawskiego Izabelina.",
            'highlight': "“ Dom Lustrzany to nie tylko budynek mieszkalny, to interaktywna forma sztuki. ”",
            'mainFoto': "https://dmddomy.pl/images/blog/bl-00-1920x750-DomLustrzany.png",
            'contentFoto': "https://dmddomy.pl/images/blog/bl-01-750x430-DomLustrzany-1.png",
            'additionalList': "Alucobond: Lustrzane Odbicie Natury: Dom Lustrzany, o powierzchni 400 m²#splx#Zanurzenie w Naturze: Alucobond sprawia, że dom staje się niemal niewidoczny.#splx#Trwałość i Niski Wymiar Utrzymania: Alucobond, jako materiał niezwykle twardy .",
            'tags': "#DomLustrzany, #ArchitekturaNowoczesna",
            'category': "Architektura Nowoczesna",
            'data': "20 luty 2024",
            'author': 'Piotr Walec',
            'comments': {
                1: {
                    'message': "Jestem zaszokowany! Czy na pewno?",
                    'user': 'Mariusz Kot',
                    'e-mail': 'mariusz@kot.com',
                    'data-time': '18 lutego 2024'
                },
                2: {
                    'message': """Fascynujący projekt! Dom Lustrzany wydaje się być nie tylko miejscem do życia, ale prawdziwym arcydziełem sztuki architektonicznej. Zaskakujące, jak alucobond potrafi połączyć nowoczesność z otaczającym krajobrazem, sprawiając, że budynek staje się niemal częścią natury. Jestem pod wrażeniem tego, jak biała bryła piętra zdaje się unosić w powietrzu, tworząc dynamiczną formę.""",
                    'user': 'Jan Kowalski',
                    'e-mail': 'jan@gmail.com',
                    'data-time': '1 marca 2024'
                },
            }
        },
        6: {
            'title': "Dom Lustrzany",
            'introduction': "Zapraszamy do fascynującej podróży do podwarszawskiego Izabelina.",
            'highlight': "“ Dom Lustrzany to nie tylko budynek mieszkalny, to interaktywna forma sztuki. ”",
            'mainFoto': "https://dmddomy.pl/images/blog/bl-00-1920x750-DomLustrzany.png",
            'contentFoto': "https://dmddomy.pl/images/blog/bl-01-750x430-DomLustrzany-1.png",
            'additionalList': "Alucobond: Lustrzane Odbicie Natury: Dom Lustrzany, o powierzchni 400 m²#splx#Zanurzenie w Naturze: Alucobond sprawia, że dom staje się niemal niewidoczny.#splx#Trwałość i Niski Wymiar Utrzymania: Alucobond, jako materiał niezwykle twardy .",
            'tags': "#DomLustrzany, #ArchitekturaNowoczesna",
            'category': "Architektura Nowoczesna",
            'data': "20 luty 2024",
            'author': 'Piotr Walec',
            'comments': {
                1: {
                    'message': "Jestem zaszokowany! Czy na pewno?",
                    'user': 'Mariusz Kot',
                    'e-mail': 'mariusz@kot.com',
                    'data-time': '18 lutego 2024'
                },
                2: {
                    'message': """Fascynujący projekt! Dom Lustrzany wydaje się być nie tylko miejscem do życia, ale prawdziwym arcydziełem sztuki architektonicznej. Zaskakujące, jak alucobond potrafi połączyć nowoczesność z otaczającym krajobrazem, sprawiając, że budynek staje się niemal częścią natury. Jestem pod wrażeniem tego, jak biała bryła piętra zdaje się unosić w powietrzu, tworząc dynamiczną formę.""",
                    'user': 'Jan Kowalski',
                    'e-mail': 'jan@gmail.com',
                    'data-time': '1 marca 2024'
                },
            }
        },
        7: {
            'title': "Dom Lustrzany",
            'introduction': "Zapraszamy do fascynującej podróży do podwarszawskiego Izabelina.",
            'highlight': "“ Dom Lustrzany to nie tylko budynek mieszkalny, to interaktywna forma sztuki. ”",
            'mainFoto': "https://dmddomy.pl/images/blog/bl-00-1920x750-DomLustrzany.png",
            'contentFoto': "https://dmddomy.pl/images/blog/bl-01-750x430-DomLustrzany-1.png",
            'additionalList': "Alucobond: Lustrzane Odbicie Natury: Dom Lustrzany, o powierzchni 400 m²#splx#Zanurzenie w Naturze: Alucobond sprawia, że dom staje się niemal niewidoczny.#splx#Trwałość i Niski Wymiar Utrzymania: Alucobond, jako materiał niezwykle twardy .",
            'tags': "#DomLustrzany, #ArchitekturaNowoczesna",
            'category': "Architektura Nowoczesna",
            'data': "20 luty 2024",
            'author': 'Piotr Walec',
            'comments': {
                1: {
                    'message': "Jestem zaszokowany! Czy na pewno?",
                    'user': 'Mariusz Kot',
                    'e-mail': 'mariusz@kot.com',
                    'data-time': '18 lutego 2024'
                },
                2: {
                    'message': """Fascynujący projekt! Dom Lustrzany wydaje się być nie tylko miejscem do życia, ale prawdziwym arcydziełem sztuki architektonicznej. Zaskakujące, jak alucobond potrafi połączyć nowoczesność z otaczającym krajobrazem, sprawiając, że budynek staje się niemal częścią natury. Jestem pod wrażeniem tego, jak biała bryła piętra zdaje się unosić w powietrzu, tworząc dynamiczną formę.""",
                    'user': 'Jan Kowalski',
                    'e-mail': 'jan@gmail.com',
                    'data-time': '1 marca 2024'
                },
            }
        },
    }
    return  daneDB
    

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
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
def  blog_management():
    """Strona z zarządzaniem blogiem."""
    # Sprawdzenie czy użytkownik jest zalogowany, jeśli nie - przekierowanie do strony głównego
    if 'username' not in session:
        return redirect(url_for('index'))

    # Wczytanie listy wszystkich postów z bazy danych i przypisanie jej do zmiennej posts
    posts = get_all_posts()
    # Renderowanie szablonu blog-managment.html z danymi o postach (wszystkimi lub po jednym)
    return render_template("blog_management.html", posts=posts, username=session['username'] )

if __name__ == '__main__':
    app.run(debug=True)