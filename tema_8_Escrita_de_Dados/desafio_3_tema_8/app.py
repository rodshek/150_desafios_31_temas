import os

from flask import (Flask, jsonify, redirect, render_template, request,
                   send_from_directory, url_for)
from flask_login import (LoginManager, UserMixin, current_user, login_required,
                         login_user, logout_user)
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import VIDEOS, UploadSet, configure_uploads

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Configurações do upload
app.config['UPLOADED_VIDEOS_DEST'] = 'uploads/videos'
app.config['UPLOADED_VIDEOS_ALLOW'] = ['mp4', 'avi', 'mov']
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///videos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

videos = UploadSet('videos', VIDEOS)
configure_uploads(app, videos)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Modelo de banco de dados para Vídeos


class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(120), unique=True, nullable=False)

# Modelo de banco de dados para Usuários


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)


# Cria o banco de dados se não existir
with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    if User.query.filter_by(username=username).first():
        return jsonify({'erro': 'Usuário já existe!'}), 400
    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'mensagem': 'Usuário registrado com sucesso!'})


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter_by(username=username, password=password).first()
    if user:
        login_user(user)
        return jsonify({'mensagem': 'Login realizado com sucesso!'})
    return jsonify({'erro': 'Credenciais inválidas!'}), 401


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/upload', methods=['POST'])
@login_required
def upload_video():
    if 'video' not in request.files:
        return jsonify({'erro': 'Nenhum vídeo enviado!'}), 400

    video = request.files['video']

    if video and video.filename.endswith(tuple(app.config['UPLOADED_VIDEOS_ALLOW'])):
        filename = videos.save(video)
        new_video = Video(filename=filename)
        db.session.add(new_video)
        db.session.commit()
        return jsonify({'mensagem': 'Vídeo enviado com sucesso!', 'url': f'/video/{filename}'})
    return jsonify({'erro': 'Formato de vídeo não permitido!'}), 400


@app.route('/video/<filename>', methods=['GET'])
def get_video(filename):
    return send_from_directory(app.config['UPLOADED_VIDEOS_DEST'], filename)


@app.route('/videos', methods=['GET'])
@login_required
def list_videos():
    videos = Video.query.all()
    video_list = [{'id': video.id, 'filename': video.filename}
                  for video in videos]
    return jsonify(video_list)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
