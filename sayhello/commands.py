from sayhello import app, db
import click


@app.cli.command()
def initdb():
    db.drop_all()
    db.create_all()
    click.echo('Initialized database, Done.')