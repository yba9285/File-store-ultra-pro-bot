from flask import Flask
from web.routes import web
from config import PORT, FLASK_SECRET_KEY
from bot import bot

app = Flask(__name__)
app.secret_key = FLASK_SECRET_KEY

app.register_blueprint(web)

# 🔥 START BOT DIRECTLY (FIX)
bot.start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
