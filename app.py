from flask import Flask
from web.routes import web

app = Flask(__name__)
app.secret_key = "your-secret-key"

app.register_blueprint(web)
