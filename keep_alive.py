from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return "Anjay Hidup!"

def run():
    app.run(host="0.0.0.0", port=6420)

def keep_alive():
    server = Thread(target=run)
    server.start()
