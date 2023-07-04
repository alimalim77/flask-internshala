from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

app = Flask(__name__, template_folder='template', static_folder='static')
CORS(app)

class Fruit:
    def __init__(self, id, name, color):
        self.id = id
        self.name = name
        self.color = color

def sort_fruits_by_color(fruits):
    sorted_fruits = sorted(fruits, key=lambda fruit: fruit.color)
    return sorted_fruits

fruits = []

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/fruits', methods=['GET', 'POST'])
def handle_fruits():
    if request.method == 'POST':
        fruit_name = request.form.get('fruit')
        fruit_color = request.form.get('color')
        new_fruit = Fruit(len(fruits) + 1, fruit_name, fruit_color)
        fruits.append(new_fruit)
        sorted_fruits = sort_fruits_by_color(fruits)
        fruit_list = []
        for fruit in sorted_fruits:
            fruit_list.append({
                'id': fruit.id,
                'name': fruit.name,
                'color': fruit.color
            })
        return jsonify(fruit_list)
    elif request.method == 'GET':
        return jsonify(fruits)

if __name__ == '__main__':
    app.run()
