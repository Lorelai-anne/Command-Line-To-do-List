import click

@click.command()
@click.argument("task")
def cli(task):
    """Add a new task."""
    with open("tasks.txt", "a") as f:
        f.write(task + "\n")
    click.echo(f"Task added: {task}")
