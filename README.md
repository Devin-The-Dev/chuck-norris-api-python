# Chuck Norris Joke CLI

A small interactive terminal app that fetches Chuck Norris jokes from [api.chucknorris.io](https://api.chucknorris.io). Built with **Python standard library only** — no pip installs required.

## Requirements

- Python 3.10+ (uses modern type hints)
- Internet access

## Quick start

```bash
python3 fetch_joke.py
```

You’ll see an ASCII banner, then a numbered menu. Pick an option, read a joke, and return to the menu until you quit.

## Menu options

| Choice | What it does |
|--------|----------------|
| **1** | Fetch a random joke |
| **2** | List categories, then fetch a random joke from your pick (by number or name) |
| **3** | Search jokes by keyword (shows the first match) |
| **4** | Exit |

## Features

- **Colored output** — cyan menu, yellow jokes, green loading text, red errors (when your terminal supports it)
- **ASCII art** — startup banner and bordered joke display
- **Category cache** — categories are fetched once per session
- **Graceful exit** — quit from the menu or press `Ctrl+C`

## Disabling colors

Colors turn off automatically when output is not a TTY (e.g. piping). You can also disable them explicitly:

```bash
NO_COLOR=1 python3 fetch_joke.py
```

## API

Jokes come from the free [Chuck Norris Jokes API](https://api.chucknorris.io):

- `GET /jokes/random`
- `GET /jokes/categories`
- `GET /jokes/random?category={name}`
- `GET /jokes/search?query={query}`

## Project layout

```
fetch_joke.py   # The entire CLI (run this file)
README.md       # This file
```

## License

Joke content is provided by the Chuck Norris API. Use this script for fun and learning.
