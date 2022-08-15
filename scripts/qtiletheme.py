#!/usr/bin/env python

import json
import os
import re
import subprocess
from shutil import copyfile


def choose_theme(themes):
    themes_string = ""
    for i, theme in enumerate(themes, 1):
        themes_string += f"{i:2}  {theme['name']}\n"

    themes_string = themes_string.rstrip()

    command = os.path.expanduser("~/.config/qtile/scripts/themes")
    pipe = subprocess.run(
        [command, themes_string, str(len(themes))], capture_output=True, text=True
    )
    selected_theme = re.match(r"\s*(\d+).+", pipe.stdout)
    selected_theme_index = int(selected_theme.group(1)) - 1

    return themes[selected_theme_index]


def change_theme(qtile):
    qtile_path = os.path.expanduser("~/.config/qtile")
    themes_path = qtile_path + "/themes.json"
    current_theme_path = qtile_path + "/themes/current.json"
    with open(themes_path, "r") as themes_file:
        themes = json.load(themes_file)

    chosen_theme = choose_theme(themes)
    copyfile(qtile_path + "/themes/" + chosen_theme["color_scheme"], current_theme_path)
    subprocess.run(
        [
            qtile_path + "/scripts/set_xsettings",
            chosen_theme["widget_theme"],
            chosen_theme["icon_theme"],
            chosen_theme["cursor_theme"],
        ]
    )
    qtile.restart()
