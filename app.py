from flask import Flask,render_template,request,redirect,url_for
import uuid

app = Flask(__name__)

tasks = [] 
# {
# title : string,
# id : string,
# completed : bool,
# }

@app.route('/')
def home():
    return render_template('index.html', tasks = tasks)

@app.route('/add', methods = ['POST'])
def add_task():
    title = request.form.get("title")
    if title:
        newtask = {
            "title" : title,
            "id" : str(uuid.uuid4()),
            "completed" : False
        }
        tasks.append(newtask)
        return redirect(url_for('home'))
    else:
        return "No Task"

# @app.route('/delete/<taskId>', methods = ['DELETE'])
# def del_task(taskId):
#     global tasks
#     tasks = [task for task in tasks if task["id"] != taskId]
#     return tasks

@app.route('/delete/<taskId>')
def del_task(taskId):
    global tasks
    tasks = [task for task in tasks if task["id"] != taskId]
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug = True)