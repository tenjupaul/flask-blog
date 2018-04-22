from flask_blog import db

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(80))
    username = db.Column(db.String(35),unique=True)
    email = db.Column(db.String(80),unique=True)
    password = db.Column(db.String(80))
    is_author = db.Column(db.Boolean)

def __init__(self, fullname, username, email, password, is_author=False):
    self.fullname = fullname
    self.username = username
    self.email = email
    self.password= password
    self.is_author = is_author

def __repr__(self):
    return '<Author %r>' % self.username