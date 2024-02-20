from flask import Flask, render_template, jsonify

"""
Aplikacja "Admin Panel" stanowi kompleksowe narzędzie do 
zarządzania wieloma witrynami
internetowymi skupionymi pod marką DMD. Została stworzona 
w oparciu o framework Flask, co
pozwala na łatwe dostosowywanie i obsługę. 
Aplikacja oferuje intuicyjny interfejs użytkownika,
umożliwiający administratorom efektywne zarządzanie 
różnymi aspektami stron.
"""

app = Flask(__name__)

# Przykładowa lista danych
data = [
    {"id": 1, "name": "Produkt A", "price": 100},
    {"id": 2, "name": "Produkt B", "price": 200},
    {"id": 3, "name": "Produkt C", "price": 150}
]

# Trasa zwracająca listę danych w formacie JSON
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(data)

# Trasa zwracająca opis panelu administracyjnego
@app.route('/admin', methods=['GET'])
def admin_panel():
    with open('templates/gateway.html', 'r', encoding='utf-8') as panel_description:
        return panel_description.read()

@app.route('/admin2', methods=['GET'])
def admin_panel2():
    # Przykładowe dane dla znaczników Flask
    user = 'John Doe'
    logged_in = False
    items = ['Apple', 'Banana', 'Orange']
    weather = 'cloudy'

    # Renderowanie szablonu HTML z wykorzystaniem znaczników Flask
    return render_template('gateway2.html', user=user, logged_in=logged_in, items=items, weather=weather)


if __name__ == '__main__':
    app.run(debug=True)