import click

@click.command()
def cli():
    """List all tasks."""
    try:
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()
        if not tasks:
            click.echo("No tasks found.")
        else:
            for i, task in enumerate(tasks, 1):
                click.echo(f"{i}. {task.strip()}")
    except FileNotFoundError:
        click.echo("No task file found.")
