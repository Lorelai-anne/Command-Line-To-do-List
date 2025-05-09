import click

@click.command()
@click.argument("task_number", type=int)
def cli(task_number):
    """Mark a task as done by number."""
    try:
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()

        if 1 <= task_number <= len(tasks):
            completed = tasks.pop(task_number - 1)
            with open("tasks.txt", "w") as f:
                f.writelines(tasks)
            click.echo(f"Task completed: {completed.strip()}")
        else:
            click.echo("Invalid task number.")
    except FileNotFoundError:
        click.echo("No task file found.")
