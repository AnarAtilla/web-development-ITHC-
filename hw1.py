from flask import Flask

# Создаем экземпляр приложения Flask
app = Flask(__name__)

# Маршрут для корневой URL (/)
@app.route('/')
def home():
    return 'Hello, Flask!'

# Дополнительный маршрут для /user/<name>
@app.route('/user/<name>')
def greet_user(name):
    return f'Hello, {name}!'

# Запуск приложения
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)