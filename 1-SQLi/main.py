import sqlite3
from flask import Flask, request, g, redirect, url_for


# Initializing the app
app = Flask(__name__)


# Configuration
DATABASE = 'prism.db'
app.config.from_object(__name__)


# Web routes
@app.route('/')  # read: url '/' triggers hello()
def hello():
    form = """
<!doctype html>
<title>SQLi</title>
<form action="/insight" method=post>
    name: <input type=text name=name><br />
    <input type=submit>
</form>
        """
    return form


@app.route('/insight', methods=['POST'])
def show_entries():
    unsafe_name = request.form['name']
    query = 'select name from prism_secrets where name="%s"' % unsafe_name
    db_cursor = g.db.execute(query)
    res_html = '<br>\n'.join([row[0] for row in db_cursor.fetchall()])
    res_html += '<br>\n<a href="/">go home</a>'
    return res_html


@app.route('/debug')
def enter_debugger():
    return 1 + 'a'


@app.route('/see')
def print_db():
    db_cursor = g.db.execute('select * from prism_secrets')
    entries = []
    for row in db_cursor.fetchall():
        str_row = [str(item) for item in row]
        entries.append('\t'.join(str_row))
    return '<br>\n'.join(entries)


# Handlers
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def init_connect():
    g.db = connect_db()

@app.teardown_request
def close_db(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


# Run the server
if __name__ == "__main__":
    app.debug = True
    app.run()
