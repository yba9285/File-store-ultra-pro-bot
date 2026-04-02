from flask import Flask
from web.routes import web
from config import PORT, FLASK_SECRET_KEY
from bot import bot
import threading

app = Flask(__name__)
app.secret_key = FLASK_SECRET_KEY

app.register_blueprint(web)


# 🔥 BOT RUN IN BACKGROUND THREAD
def run_bot():
    bot.run()   # ✅ run() handles start + idle


threading.Thread(target=run_bot).start()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
