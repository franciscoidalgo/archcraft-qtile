#!/usr/bin/env python

import json
import os
import re
import subprocess


def show_themes_options(themes):
    themes_string = ""
    for i, theme in enumerate(themes):
        themes_string += f"{(i + 1):2}  {theme['name']}\n"

    themes_string = themes_string.rstrip()

    command = os.path.expanduser("~/.config/qtile/scripts/themes")
    pipe = subprocess.run([command, themes_string], capture_output=True, text=True)
    selected_theme = re.match(r"\s*(\d+)\s+(.+)", pipe.stdout)
    selected_theme_index = int(selected_theme.group(1)) - 1
    selected_theme_name = selected_theme.group(2)

    print(selected_theme_index, selected_theme_name)
    # theme = list(filter(lambda theme: theme["name"] == selected_theme_name, themes))


def choose_theme():
    themes_path = os.path.expanduser("~/.config/qtile/themes.json")
    with open(themes_path, "r") as themes_file:
        themes = json.load(themes_file)

    show_themes_options(themes)
    # themes = dict()
    # for theme in themes_paths:
    #     with open(theme, "r") as theme_json:
    #         themes[theme] = json.load(theme_json)


if __name__ == "__main__":
    choose_theme()
