#!/usr/bin/env python

import json
import os
import subprocess
import re


def show_themes_options(themes):
    themes_string = ""
    for theme in themes:
        themes_string += f"  {theme}\n"

    command = os.path.expanduser("~/.config/qtile/scripts/themes")
    pipe = subprocess.run([command, themes_string], capture_output=True, text=True)
    selected_theme = re.match(r"\s+(.+)", pipe.stdout).group(1)


def choose_theme():
    themes_dir = os.path.expanduser("~/.config/qtile/themes")
    themes_paths = []
    with os.scandir(themes_dir) as td:
        for entry in td:
            if entry.name.endswith(".json"):
                themes_paths.append(entry.path)

    show_themes_options(themes_paths)
    # themes = dict()
    # for theme in themes_paths:
    #     with open(theme, "r") as theme_json:
    #         themes[theme] = json.load(theme_json)


if __name__ == "__main__":
    choose_theme()
