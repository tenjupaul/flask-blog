import os, sys

#print(sys.path)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'home')))
#print(sys.path)
from flask_script import Manager, Server
from flask_blog import app

manager = Manager(app)

manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = os.getenv('IP','127.0.0.1'),
    port = int(os.getenv('PORT',8080))
    )
)

if __name__ == "__main__":
   # print(sys.path)
    manager.run()
