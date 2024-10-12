import click
import requests

BASE_URL = "http://127.0.0.1:8000/files"

@click.group()
def cli():
    """CLI for file storage server"""
    pass

@cli.command()
@click.argument("file_path", type=click.Path(exists=True))
@click.argument("file_name")
def upload_file(file_path, file_name):
    """Upload a file to the server."""
    with open(file_path, 'rb') as f:
        response = requests.post(f"{BASE_URL}/{file_name}", files={"file": f})
        if response.status_code == 200:
            click.echo(f"File '{file_name}' uploaded successfully.")
        else:
            click.echo(f"Failed to upload '{file_name}'. Status code: {response.status_code}")

@cli.command()
@click.argument("file_name")
def delete_file(file_name):
    """Delete a file from the server."""
    response = requests.delete(f"{BASE_URL}/{file_name}")
    if response.status_code == 200:
        click.echo(f"File '{file_name}' deleted successfully.")
    else:
        click.echo(f"Failed to delete '{file_name}'. Status code: {response.status_code}")

@cli.command()
def list_files():
    """List all files on the server."""
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        files = response.json()
        click.echo("Files on the server:")
        for file in files:
            click.echo(f"- {file}")
    else:
        click.echo(f"Failed to list files. Status code: {response.status_code}")

if __name__ == "__main__":
    cli()
