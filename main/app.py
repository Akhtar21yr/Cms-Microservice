from flask import Flask
from flask_migrate import Migrate
from main import app, db  # Import the app and db instances

migrate = Migrate(app, db)

@app.cli.command("db-init")
def db_init():
    """Initialize the database."""
    from flask_migrate import upgrade
    upgrade()

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
