import argparse
import random
from rich import print
import builtins
from .cat_art import cats
from rich.console import Console
from rich.text import Text

console=Console()
WIDTH = 40
AVAILABLE_COLORS = [
    "red",
    "green",
    "yellow",
    "blue",
    "magenta",
    "cyan",
    "white",
    "black",
    "orange1",   
    "deep_pink4"  
]

def make_balloon(text: str) -> str:
    width = len(text)
    if len(text) > WIDTH:
        print("[bold red] Write shorter! [/bold red]")
        return 0

    top = "  " + "_" * (width + 2)
    bottom = "  " + "-" * (width + 2)

    balloon = [top]
    balloon.append(f"  |{text.ljust(width)}|")
    balloon.append(bottom)
    return "\n".join(balloon)

def list_colors():
    console.print("[bold underline]Colors available:[/bold underline]")
    for color in AVAILABLE_COLORS:
        console.print(f"[{color}]{color}[/]")

def main():
    parser = argparse.ArgumentParser(prog="catsay", description="Catsay CLI: Display your message with a talking ASCII cat!")
    parser.add_argument("message", nargs="*", help="The message your cat will say")
    parser.add_argument("-c", "--color", help="Color of the output text (e.g. red, blue, magenta)")
    parser.add_argument("--list-colors", action="store_true", help="Show all supported colors")
    args = parser.parse_args()

    if args.list_colors:
        list_colors()
        return
    
    if not args.message:
        parser.print_help()
        return
    
    text = " ".join(args.message)
    ballon= make_balloon(text)
    if ballon == 0 : return
    cat = random.choice(cats)
    result = ballon + "\n" + cat

    if args.color:
        if args.color not in AVAILABLE_COLORS:
            console.print(f"[red]catsay -c redColor '{args.color}' is not valid. To see available colors, use:[/] [bold]catsay --list-colors[/bold]")
            return
        console.print(Text(result, style=args.color))
    else:
        builtins.print(result)

if __name__ == "__main__":
    main()