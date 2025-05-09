import click
import os

plugin_folder = os.path.join(os.path.dirname(__file__))  # modify this if you want to store commands in subfolder
cli_marker = "cli_"

class MyCLI(click.MultiCommand):
    """ Main entry point for a multicommand that loads commands from the program home folder. """
    def list_commands(self, ctx):
        """ List subcommands found in folder.  Only show those with appropriate markers. """
        rv = []
        for filename in os.listdir(plugin_folder):
            if filename.startswith(cli_marker) and filename.endswith('.py'):
                rv.append(filename[len(cli_marker):-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        """Secret sauce that loads, compiles and runs a command file dynamically."""
        ns = {}
        fn = os.path.join(plugin_folder, cli_marker + name + '.py')
        try:
            with open(fn) as f:
                code = compile(f.read(), fn, 'exec')
                eval(code, ns, ns)
            return ns['cli']
        except FileNotFoundError:
            pass


@click.command(cls=MyCLI)
@click.version_option(package_name="mytools")  # this package name needs to match the *name* at the top of pyproject.toml
@click.pass_context
def main(ctx):
    """ Multicommand demonstration program

    your very own to-do list manager in the command line! Easily add, remove, and list tasks.
    """
    pass

if __name__ == '__main__':
    main()
    