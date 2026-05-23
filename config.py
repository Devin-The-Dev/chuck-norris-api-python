"""Terminal colors and menu configuration for the Chuck Norris joke CLI."""

import os
import sys

BANNER_ART = r"""
     _____________________________
    |  CHUCK NORRIS JOKE MACHINE |
    |   *  *  *  ROUNDHOUSE  *  * |
    |_____________________________|
         \   ^__^
          \  (oo)\_______
             (__)\       )\/\
                 ||----w |
                 ||     ||
"""

TAGLINE = "Legends say Chuck Norris doesn't read — the words surrender."

MENU_BOX = """
╔══════════════════════════════════════╗
║     CHUCK NORRIS JOKE MACHINE        ║
╠══════════════════════════════════════╣
║  1) Random joke                      ║
║  2) Joke by category                 ║
║  3) Search jokes                     ║
║  4) Quit                             ║
╚══════════════════════════════════════╝"""


class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    CYAN = "\033[36m"
    YELLOW = "\033[33m"
    GREEN = "\033[32m"
    RED = "\033[31m"
    MAGENTA = "\033[35m"


USE_COLOR = sys.stdout.isatty() and not os.environ.get("NO_COLOR")


def colorize(text: str, code: str) -> str:
    if not USE_COLOR:
        return text
    return f"{code}{text}{Colors.RESET}"


def print_styled(text: str, code: str, *, file=None) -> None:
    print(colorize(text, code), file=file or sys.stdout)


def print_error(message: str) -> None:
    print_styled(message, Colors.RED, file=sys.stderr)


def print_banner() -> None:
    print_styled(BANNER_ART, Colors.BOLD)
    print_styled(TAGLINE, Colors.CYAN)
    print()


def print_menu() -> None:
    print_styled(MENU_BOX, Colors.CYAN)
