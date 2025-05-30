
from flask import Flask, render_template, request, jsonify
from bson.objectid import ObjectId
from data_base import get_all_todos, add_todo, toggle_done, delete_todo, update_todo
from flask_cors import CORS

app = Flask(__name__, template_folder="templates")
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/todos")
def get_todos():
    todos = get_all_todos()
    # Convert ObjectId to string for JSON
    todos = [{**todo, '_id': str(todo['_id'])} for todo in todos]
    return jsonify(todos)

@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("todo")
    if task and task.strip():
        add_todo(task.strip())
    return jsonify({"status": "success"})

@app.route("/check/<id>", methods=["POST"])
def check(id):
    done = request.form.get("done", "false").lower() == "true"
    toggle_done(ObjectId(id), done)
    return jsonify({"status": "success"})

@app.route("/delete/<id>", methods=["POST"])
def delete(id):
    delete_todo(ObjectId(id))
    return jsonify({"status": "success"})

@app.route("/edit/<id>", methods=["POST"])
def edit(id):
    new_task = request.form.get("todo")
    if new_task and new_task.strip():
        update_todo(ObjectId(id), new_task.strip())
    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(host= "0.0.0.0", port = 5000, debug=True)












