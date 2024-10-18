from flask import (Flask, flash, redirect, render_template, request, session,
                   url_for)
from flask_login import (LoginManager, UserMixin, current_user, login_required,
                         login_user, logout_user)
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Usado para proteger a sessão
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Usuários em memória (para simplicidade)
users = {}


class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User {self.username}>'


@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = next((u for u in users.values()
                    if u.username == username), None)
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Login successful.')
            return redirect(url_for('profile'))
        flash('Invalid credentials.')
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in [u.username for u in users.values()]:
            flash('Username already exists.')
        else:
            user_id = str(len(users) + 1)
            hashed_password = generate_password_hash(password, method='sha256')
            user = User(user_id, username, hashed_password)
            users[user_id] = user
            flash('User registered successfully.')
            return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/profile')
@login_required
def profile():
    return f'Welcome {current_user.username}!'


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
