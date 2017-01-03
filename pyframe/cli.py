import click
from structure import ProjectBuilder

@click.group(help="A happy little python package creation framework.")
def run():
    pass

@run.command(help="Create a new package framework")
@click.option("-n", "--name", required=True, help="Python project to initialize")
@click.option("-a", "--author", required=True, help="Project author")
@click.option("-d", "--description", required=True, help="Project description.")
@click.option("-t", "--templates", default=None, help="Personal templates directory (will override defaults).")
@click.option("-k", "--kwargs", type=click.File(), help="Yaml config file for additional template args if needed.")
def new(name, author, description, templates, kwargs):
    build = ProjectBuilder(**locals())
    build.run()

@run.command(help="Utility command to create test files mirroring package layout.")
def tests():
    pass


if __name__ == "__main__":
    run()
