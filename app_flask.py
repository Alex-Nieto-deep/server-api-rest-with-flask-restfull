import flask
from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
db = {}
id = 0


@app.route("/item", methods=['POST'])
def create_item():
    global id
    id += 1
    db[id] = request.json
    print(db)
    print(request.json)
    return ({"status": "OK"})


@app.route('/items', methods=['GET'])
def get_items():
    return(db)


@app.route('/item/<int:selected>', methods=['GET'])
def get_item(selected):
    return(db[int(selected)])


@app.route('/item/<int:id>', methods=['PUT'])
def update_item(id):
    db[int(id)] = request.json
    print(request.json)
    return ({"status": "UPDATE"})


@app.route('/item', methods=['DELETE'])
def delete_item():
    del_id = request.json['id']
    print(del_id)
    if (db.get(del_id) != None):
        del db[del_id]
        return({"status": "DELETE"})
    else:
        return({"status": "NOT FOUND"})


if __name__ == '__main__':
    app.run("0.0.0.0", debug=False)
    # app.run("0.0.0.0",debug=True)
