from flask import Flask, render_template

app = Flask(__name__)

users = [
    {"id": 1, "name": "Jahongir", "age": 25, "city": "Tashkent"},
    {"id": 2, "name": "Aziz", "age": 22, "city": "Samarqand"},
    {"id": 3, "name": "Malika", "age": 28, "city": "Bukhara"}
]

@app.route('/users')
def show_users():
    return render_template('users.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
