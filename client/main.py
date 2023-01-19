from flask import Flask, render_template
import requests, json, socket

app = Flask(__name__)


@app.route("/")
def get():
    r = requests.get("http://server:5000/jobs")
    json_data = json.loads(r.text)
    return render_template('index.html', jobs=json_data)

@app.route("/help")
def post():
    ip = get_ip()
    r = requests.post("http://server:5000/jobs", json={ip: 'открыта'})
    json_data = json.loads(r.text)
    return render_template('reg.html', host_ip=ip, status=json_data[ip])

def get_ip():
    r = requests.get("https://ipv4-internet.yandex.net/api/v0/ip")
    ip = json.loads(r.text)
    return ip

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)