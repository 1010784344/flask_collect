from startcheck import app
from flask_script import Manager

manager = Manager(app)
# Run local server
# manager.add_command("runserver", Server("localhost", port=5000))

if __name__ == '__main__':
    manager.run()
