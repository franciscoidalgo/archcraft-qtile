import json
import os

with open(os.path.expanduser("~/.config/qtile/themes/current.json")) as theme_file:
    theme = json.load(theme_file)
