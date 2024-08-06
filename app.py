from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample in-memory data store for tasks
todos = []

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    priority = request.form.get('priority')
    todos.append({'task': task, 'completed': False, 'priority': priority})
    return redirect(url_for('index'))

@app.route('/update/<int:task_index>', methods=['POST'])
def update_task(task_index):
    # Toggle the completed status
    todos[task_index]['completed'] = not todos[task_index]['completed']
    return redirect(url_for('index'))

@app.route('/delete/<int:task_index>', methods=['POST'])
def delete_task(task_index):
    # Remove the task from the list
    todos.pop(task_index)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
