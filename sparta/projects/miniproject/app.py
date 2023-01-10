from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://homesite:oBJqg6n3yp0IItHS@cluster0.gnq7ra8.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.miniproject


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/saveAdopt", methods=["POST"])
def saveAdopt_post():

    index_receive = request.form['index_give']
    name_receive = request.form['name_give']
    age_receive = request.form['age_give']
    address_receive = request.form['address_give']
    reason_receive = request.form['reason_give']
    doc = {'index': index_receive,'name': name_receive, 'age':age_receive, 'address':address_receive, 'reason':reason_receive}
    print (doc)
    print (doc)
    db.miniproject.insert_one(doc)

    return jsonify({'msg':'저장완료'})

@app.route("/homework", methods=["GET"])
def saveAdopt_get():
    all_comments = list(db.homework.find({}, {'_id': False}))
    return jsonify({'homework': all_comments})

@app.route("/saveAdoptView", methods=["POST"])
def saveAdoptView_post():
    index_receive = request.form['index_give']
    # index_receive = request.args.get('index_give', "")
    print(index_receive)
    all_comments = list(db.miniproject.find({'index':index_receive}, {'_id': False}))
    print(all_comments)
    return jsonify({'msg': all_comments})

@app.route("/saveAdoptView")
def saveAdoptView_page():
    return render_template('AdoptView.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)