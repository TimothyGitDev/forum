from flask import Flask, render_template, request, redirect
import sqlite3
# import webview

   # Укажите URL вашего сайта



app = Flask(__name__)

# Функция для инициализации базы данных
def init_db():
    with sqlite3.connect('messages.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                content TEXT NOT NULL
            )
        ''')
        conn.commit()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.form.get('message')  # Используем get вместо прямого доступа
        name = request.form.get('names')  # Используем get вместо прямого доступа
        
        if message and name:  # Проверяем, что обе переменные не пустые
            with sqlite3.connect('messages.db') as conn:
                cursor = conn.cursor()
                cursor.execute('INSERT INTO messages (name, content) VALUES (?, ?)', (name, message))
                conn.commit()
            return redirect('/')
        
        

    with sqlite3.connect('messages.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM messages')
        messages = cursor.fetchall()

    return render_template('index.html', messages=messages)

if __name__ == '__main__':  # Исправлено здесь
    init_db()
    app.run(debug=True)