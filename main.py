from flask import Flask
from src.config.config import DATABASE_URL
from src.config.database import engine, Base
from src.models.registry import Registry
from src.api.registry import registry_bp
from src.api.token import security_bp
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

Base.metadata.create_all(bind=engine)

app.register_blueprint(registry_bp)

app.register_blueprint(security_bp)


@app.route('/')
def home():
    return {'message':'Retail Supply Network API'}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

