from flask import Flask, request, jsonify


app = Flask(__name__)

joblist = {'test': 'test'}

@app.route('/jobs', methods=['GET'])
def get_list():
    return jsonify(joblist)

@app.route('/jobs', methods=['POST'])
def add_list():
    new_job = request.json
    joblist.update(new_job)
    return jsonify(new_job)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)