from flask import Flask, jsonify
from resources.apartment import apartments
from resources.user import user
import models
from flask_cors import CORS
from flask_login import LoginManager

DEBUG = True
PORT = 8000

app = Flask(__name__)

app.secret_key = 'ABCD'

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    try:
        return models.User.get(models.User.id == user_id)
    except models.DoesNotExist:
        return None

app.config['CORS_HEADERS'] = 'Content-Type'

CORS(app, resources={r"/*": {"origins": "*"}})
CORS(apartments, origins=['*'], supports_credentials=True)
CORS(user, origins=['*'], supports_credentials=True)

app.register_blueprint(apartments,url_prefix='/api/v1/apartments')
app.register_blueprint(user,url_prefix='/api/v1/user')

# test route
# @app.route('/sample')
# def get_sample():
#     return ['hello','hi']

if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)