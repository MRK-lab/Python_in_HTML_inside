####### arka planda bash ekrani geiyor ve calisiyor
from flask import Flask
import subprocess
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/run_app', methods=['POST'])
def run_app():
    try:
        # Python betiğini yeni bir terminal penceresinde başlat
        if os.name == 'nt':  # Windows
            subprocess.Popen(['python', 'run_app.py'], creationflags=subprocess.CREATE_NEW_CONSOLE)
        else:  # Unix/Linux/Mac
            subprocess.Popen(['x-terminal-emulator', '-e', 'python3 run_app.py'])
        
        return "Python script arka planda çalışıyor ve terminalde gösteriliyor..."
    except Exception as e:
        return f"Hata: {e}"

if __name__ == '__main__':
    app.run(debug=True)



####### arka planda ekran gelmeden calisiyor
# from flask import Flask
# import subprocess
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# @app.route('/')
# def index():
#     return app.send_static_file('index.html')

# @app.route('/run_app', methods=['POST'])
# def run_app():
#     try:
#         # Python komutunu arka planda çalıştır
#         subprocess.Popen(['python', 'run_app.py'])
        
#         # Kullanıcıya sadece bir başarı mesajı döndür
#         return "Python script arka planda çalışıyor..."
#     except Exception as e:
#         return f"Hata: {e}"

# if __name__ == '__main__':
#     app.run(debug=True)
