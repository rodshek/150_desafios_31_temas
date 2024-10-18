import os

from flask import Flask, jsonify, request, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import VIDEOS, UploadSet, configure_uploads

app = Flask(__name__)

# Configurações do upload
app.config['UPLOADED_VIDEOS_DEST'] = 'uploads/videos'
app.config['UPLOADED_VIDEOS_ALLOW'] = ['mp4', 'avi', 'mov']
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///videos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

videos = UploadSet('videos', VIDEOS)
configure_uploads(app, videos)
db = SQLAlchemy(app)

# Modelo de banco de dados para Vídeos
class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(120), unique=True, nullable=False)

# Cria o banco de dados se não existir
with app.app_context():
    db.create_all()

@app.route('/upload', methods=['POST'])
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
def list_videos():
    videos = Video.query.all()
    video_list = [{'id': video.id, 'filename': video.filename} for video in videos]
    return jsonify(video_list)

if __name__ == '__main__':
    app.run(debug=True)
