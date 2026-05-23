#!/usr/bin/env python3
"""Chuck Norris joke CLI — api.chucknorris.io (stdlib only)."""

import json
import textwrap
import time
import urllib.error
import urllib.parse
import urllib.request

from config import Colors, colorize, print_banner, print_error, print_menu, print_styled

API_BASE = "https://api.chucknorris.io"
USER_AGENT = "chuck-norris-api/1.0 (Python urllib)"

_categories_cache: list[str] | None = None


def print_joke_box(joke: str) -> None:
    wrapped = textwrap.fill(joke, width=68)
    border = "━" * 36
    print()
    print_styled(border, Colors.YELLOW)
    for line in wrapped.splitlines():
        print_styled(f"  {line}", Colors.YELLOW)
    print_styled(border, Colors.YELLOW)
    print()


def print_goodbye() -> None:
    print()
    print_styled("Chuck Norris never says goodbye. He says 'You're welcome.'", Colors.MAGENTA)
    print_styled("  \\ (^_^) /", Colors.MAGENTA)
    print()


def show_loading() -> None:
    print_styled("Chuck is thinking...", Colors.GREEN)
    time.sleep(0.3)


def api_get(path: str) -> dict:
    url = f"{API_BASE}{path}"
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/json",
            "User-Agent": USER_AGENT,
        },
    )
    with urllib.request.urlopen(request, timeout=10) as response:
        return json.loads(response.read().decode("utf-8"))


def handle_api_errors(func):
    """Run func(); return False on API failure (errors already printed)."""

    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
            return True
        except urllib.error.HTTPError as exc:
            print_error(f"HTTP error {exc.code}: {exc.reason}")
            return False
        except urllib.error.URLError as exc:
            print_error(f"Request failed: {exc.reason}")
            return False
        except (KeyError, json.JSONDecodeError) as exc:
            print_error(f"Unexpected API response: {exc}")
            return False

    return wrapper


@handle_api_errors
def fetch_and_show_joke(path: str) -> None:
    show_loading()
    data = api_get(path)
    print_joke_box(data["value"])


def get_categories() -> list[str]:
    global _categories_cache
    if _categories_cache is None:
        data = api_get("/jokes/categories")
        _categories_cache = data
    return _categories_cache


@handle_api_errors
def action_random() -> None:
    fetch_and_show_joke("/jokes/random")


@handle_api_errors
def action_category() -> None:
    show_loading()
    categories = get_categories()
    print()
    print_styled("Categories:", Colors.CYAN)
    for index, name in enumerate(categories, start=1):
        print_styled(f"  {index}) {name}", Colors.CYAN)

    while True:
        choice = input(colorize("\nCategory (number or name): ", Colors.CYAN)).strip()
        if not choice:
            print_error("Please enter a category.")
            continue

        if choice.isdigit():
            index = int(choice)
            if 1 <= index <= len(categories):
                category = categories[index - 1]
                break
            print_error(f"Pick a number between 1 and {len(categories)}.")
            continue

        if choice in categories:
            category = choice
            break

        print_error("Unknown category. Try again.")

    fetch_and_show_joke(f"/jokes/random?category={urllib.parse.quote(category)}")


@handle_api_errors
def action_search() -> None:
    query = input(colorize("Search keyword: ", Colors.CYAN)).strip()
    if not query:
        print_error("Please enter a search term.")
        return

    show_loading()
    data = api_get(f"/jokes/search?query={urllib.parse.quote(query)}")
    results = data.get("result", [])
    if not results:
        print_error("No jokes found for that search.")
        return

    print_joke_box(results[0]["value"])


def read_menu_choice() -> str:
    while True:
        choice = input(colorize("Choice: ", Colors.BOLD)).strip()
        if choice in ("1", "2", "3", "4"):
            return choice
        print_error("Invalid choice. Enter 1, 2, 3, or 4.")


def main() -> int:
    print_banner()

    try:
        while True:
            print_menu()
            choice = read_menu_choice()

            if choice == "1":
                action_random()
            elif choice == "2":
                action_category()
            elif choice == "3":
                action_search()
            elif choice == "4":
                print_goodbye()
                return 0
    except KeyboardInterrupt:
        print()
        print_goodbye()
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
