import os

from flask import Flask, jsonify, request, send_from_directory
from flask_uploads import IMAGES, VIDEOS, UploadSet, configure_uploads

app = Flask(__name__)

# Configurações do upload
app.config['UPLOADED_VIDEOS_DEST'] = 'uploads/videos'
app.config['UPLOADED_VIDEOS_ALLOW'] = ['mp4', 'avi', 'mov']
videos = UploadSet('videos', VIDEOS)
configure_uploads(app, videos)

# Cria o diretório de upload se não existir
if not os.path.exists(app.config['UPLOADED_VIDEOS_DEST']):
    os.makedirs(app.config['UPLOADED_VIDEOS_DEST'])


@app.route('/upload', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return jsonify({'erro': 'Nenhum vídeo enviado!'}), 400

    video = request.files['video']

    if video and video.filename.endswith(tuple(app.config['UPLOADED_VIDEOS_ALLOW'])):
        filename = videos.save(video)
        return jsonify({'mensagem': 'Vídeo enviado com sucesso!', 'url': f'/video/{filename}'})
    return jsonify({'erro': 'Formato de vídeo não permitido!'}), 400


@app.route('/video/<filename>', methods=['GET'])
def get_video(filename):
    return send_from_directory(app.config['UPLOADED_VIDEOS_DEST'], filename)


if __name__ == '__main__':
    app.run(debug=True)
