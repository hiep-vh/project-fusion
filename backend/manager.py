from app import create_app, db
from flask_migrate import Migrate
from flask.cli import with_appcontext
import click

app = create_app()
migrate = Migrate(app, db)

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    """Command to create all tables."""
    db.create_all()
    click.echo("Tables created successfully!")

# Đăng ký lệnh CLI
app.cli.add_command(create_tables)

if __name__ == '__main__':
    app.run()
