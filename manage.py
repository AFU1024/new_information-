from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from info import create_app, db

app = create_app('develop')
manage = Manager(app)
Migrate(app, db)
manage.add_command("db", MigrateCommand)


@app.route("/")
def index():
    return "HelloWorld"


if __name__ == "__main__":
    manage.run()
