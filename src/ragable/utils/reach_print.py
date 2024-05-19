from rich.console import Console
from rich.markdown import Markdown


def display_message(msg: str):
    console = Console()
    mk_msg = Markdown(msg)
    console.print(mk_msg)


if __name__ == '__main__':
    msg = """
This is markdown hello world.
- Hello
- World
"""
    display_message(msg)