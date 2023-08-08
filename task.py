from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simple in-memory storage for tasks.
tasks = [{'id': i, 'text': "Task " + str(i)} for i in range(1, 4)]

# This is your homepage
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

# This is not a page. This route handles the adding process
@app.route('/add_task', methods=['POST'])
def add_task():
    task_text = request.form.get('task')
    if task_text:
        task_id = len(tasks) + 1
        tasks.append({'id': task_id, 'text': task_text})
    return redirect(url_for('index'))

# Also not a page. This route handles the delete process  
@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
