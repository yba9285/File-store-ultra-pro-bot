from flask import Flask
from web.routes import web
from config import PORT, FLASK_SECRET_KEY
from bot import bot

import threading
import asyncio

app = Flask(__name__)
app.secret_key = FLASK_SECRET_KEY

app.register_blueprint(web)


# 🔥 FIXED BOT RUN WITH EVENT LOOP
def run_bot():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    bot.run()


# 🔥 START BOT IN BACKGROUND
threading.Thread(target=run_bot).start()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
