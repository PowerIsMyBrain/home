from flask import Flask, jsonify

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

if __name__ == '__main__':
    app.run(debug=True)