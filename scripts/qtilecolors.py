#!/usr/bin/env python

import configparser
import os

import yaml


def set_term_colors(theme):
    alacritty_config_path = os.path.expanduser("~/.config/alacritty/colors.yml")
    with open(alacritty_config_path, "w") as alacritty_config:
        loaded_config = {
            "colors": {
                "primary": {
                    "background": theme["background"],
                    "foreground": theme["foreground"],
                },
                "normal": {
                    "black": theme["black"],
                    "red": theme["red"],
                    "green": theme["green"],
                    "yellow": theme["yellow"],
                    "blue": theme["blue"],
                    "magenta": theme["magenta"],
                    "cyan": theme["cyan"],
                    "white": theme["white"],
                },
                "bright": {
                    "black": theme["altblack"],
                    "red": theme["altred"],
                    "green": theme["altgreen"],
                    "yellow": theme["altyellow"],
                    "blue": theme["altblue"],
                    "magenta": theme["altmagenta"],
                    "cyan": theme["altcyan"],
                    "white": theme["altwhite"],
                },
            }
        }
        yaml.dump(loaded_config, alacritty_config, sort_keys=False)


def set_rofi_colors(theme):
    rofi_config_path = os.path.expanduser("~/.config/qtile/rofi/themes/colors.rasi")
    with open(rofi_config_path, "w") as rofi_config:
        rofi_config.writelines(
            [
                "* {\n",
                f"      background:     {theme['background']};\n",
                f"      foreground:     {theme['foreground']};\n",
                f"      selected:       {theme['blue']};\n",
                f"      highlight:      {theme['yellow']};\n",
                f"      urgent:         {theme['red']};\n",
                f"      on:             {theme['green']};\n",
                f"      off:            {theme['red']};\n" "}",
            ]
        )


def set_dunst_color(theme):
    dunst_config_path = os.path.expanduser("~/.config/qtile/dunstrc")
    config = configparser.ConfigParser()
    config.read(dunst_config_path)
    config["urgency_low"] = {
        "timeout": "2",
        "background": f'"{theme["background"]}"',
        "foreground": f'"{theme["foreground"]}"',
        "frame_color": f'"{theme["blue"]}"',
    }
    config["urgency_normal"] = {
        "timeout": "5",
        "background": f'"{theme["background"]}"',
        "foreground": f'"{theme["foreground"]}"',
        "frame_color": f'"{theme["blue"]}"',
    }
    config["urgency_critical"] = {
        "timeout": "0",
        "background": f'"{theme["background"]}"',
        "foreground": f'"{theme["foreground"]}"',
        "frame_color": f'"{theme["red"]}"',
    }
    with open(dunst_config_path, "w") as dunst_config:
        config.write(dunst_config)


def main(theme):
    set_rofi_colors(theme)
    set_term_colors(theme)
    set_dunst_color(theme)
