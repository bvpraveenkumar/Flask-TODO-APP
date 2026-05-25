from flask import Blueprint, render_template, request, redirect, url_for
from tinydb import TinyDB, Query

bp = Blueprint('todo', __name__)

db = TinyDB('db.json')


def _next_todo_id() -> int:
    """Return a unique integer id for a new todo item."""
    todos = db.all()
    if not todos:
        return 1
    return max(todo.get('id', 0) for todo in todos) + 1


@bp.route('/')
def index():
    todo_list = db.all()
    return render_template('index.html', todo_list=todo_list)


@bp.route('/add', methods=['POST'])
def add():
    title = (request.form.get('title') or '').strip()
    if title:
        db.insert({'id': _next_todo_id(), 'title': title, 'complete': False})
    return redirect(url_for('todo.index'))


@bp.route('/update', methods=['POST'])
def update():
    todo_db = Query()
    new_text = request.form.get('inputField')
    todo_id = request.form.get('hiddenField')
    db.update({'title': new_text}, todo_db.id == int(todo_id))
    return redirect(url_for('todo.index'))


@bp.route('/delete/<int:todo_id>', methods=['POST'])
def delete(todo_id):
    todo_db = Query()
    db.remove(todo_db.id == todo_id)
    return redirect(url_for('todo.index'))


@bp.route('/complete/<int:todo_id>', methods=['POST'])
def complete(todo_id):
    todo_db = Query()
    db.update({'complete': True}, todo_db.id == todo_id)
    return redirect(url_for('todo.index'))
