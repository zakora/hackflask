import sqlite3
from flask import Flask, request, g, redirect, url_for


# Initializing the app
app = Flask(__name__)


# Configuration
DATABASE = 'prism.db'
SECRET_KEY = 'HURRYUPHIDETHEFACTS'
app.config.from_object(__name__)


# Web routes
@app.route('/', methods=['POST', 'GET'])  # read: url '/' triggers hello()
def hello():
    if request.method == 'POST':
        unsafe_name = request.form['name']
        unsafe_secret = request.form['secret']
        g.db.execute('insert into prism_secrets (name, secret)' + \
                     'values ("' + unsafe_name + '", "' + unsafe_secret + '")')
        g.db.commit()
        return redirect(url_for('hello'))
    else:
        form = """
<!doctype html>
<title>SQLi</title>
<form action="/" method=post>
    name: <input type=text name=name><br />
    secret: <input type=text name=secret><br />
    <input type=submit>
</form>
        """
        return form


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
    return '\n'.join(entries)


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
