from flask import Flask, render_template, request, redirect
app = Flask(__name__)

tasks=[] # Empty list
# Home page route
@app.route("/")
def Home():
    return render_template("index.html", tasks=tasks)

# For adding new task in Taks list
@app.route("/add", methods=["POST"])
def add_task():
    new_task = request.form.get("task_name")            
    tasks.append(new_task)
    return redirect("/")
# For deleting any task
@app.route('/delete/<int:index>', methods=['POST'])
def delete_task(index):
    tasks.pop(index)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)        