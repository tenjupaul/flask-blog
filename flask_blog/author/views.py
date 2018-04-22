from flask_blog import app

@app.route('/login')
def login():
    return "Hello User!"

@app.route('/register', methods=('GET','POST'))
def register():
