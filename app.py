from flask import Flask, jsonify
import time
from configparser import ConfigParser
from gevent.pywsgi import WSGIServer

config = ConfigParser()
config.read("config.ini")
config_port = config.getint("server", "port")
config_G_0 = config.getfloat("app", "G_0")
config_Y_0 = config.getfloat("app", "Y_0")
config_G_1 = config.getfloat("app", "G_1")
config_Y_1 = config.getfloat("app", "Y_1")

initialTime = time.time()
period = config_G_0 + config_Y_0 + config_G_1 + config_Y_1

app = Flask(__name__)


@app.route("/api/sync")
def get_time():
    return jsonify({"initialTime": initialTime, "currentTime": time.time()})


@app.route("/api/config")
def get_config():
    return jsonify(
        {"G_0": config_G_0, "Y_0": config_Y_0, "G_1": config_G_1, "Y_1": config_Y_1}
    )


@app.route("/Minecraft-Regular.otf")
def get_font():
    return app.send_static_file("Minecraft-Regular.otf")


@app.route("/favicon.ico")
def get_favicon():
    return app.send_static_file("favicon.ico")


@app.route("/")
def index():
    return app.send_static_file("index.html")


print(f"CyberCrossing 服务已启动，访问 本机IP:{config_port} 查看页面。")

server = WSGIServer(("0.0.0.0", config_port), app)
server.serve_forever()