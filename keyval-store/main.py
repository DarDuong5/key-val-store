import click
from kvstore import KeyValueStore

kv_store = KeyValueStore(fileName='data.json')

@click.group()
def cli():
    """ A CLI for Key-Value Store """
    pass

@cli.command()
@click.argument("key")
@click.argument("value")
def insert(key, value):
    """ Inserts given key and value into key-value store """
    kv_store.insert(key, value)
    click.echo(f"Inserted {key}: {value}")

@cli.command()
@click.argument("key")
def read(key):
    """ Reads the value of the key """
    value = kv_store.get(key)
    if value is not None:
        click.echo(f"{key}: {value}")
    else:
        click.echo("This key does not exist")

@cli.command()
@click.argument("key")
@click.argument("value")
def update(key, value):
    """ Updates the value of the key """
    if kv_store.get(key) is not None:
        kv_store.update(key, value)
        click.echo(f"Updated! {key}: {value}")
    else:
        click.echo("This key does not exist")
    
@cli.command()
@click.argument("key")
def delete(key):
    """ Deletes the key and its value """
    if kv_store.get(key) is not None:
        kv_store.delete(key)
        click.echo(f"Successfully deleted {key}")
    else:
        click.echo("This key does not exist")

if __name__ == '__main__':
    cli()
