# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import subprocess

from libqtile import bar, hook, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from scripts.qtilecolors import main as set_colors
from themes.load_theme import theme
from scripts.qtiletheme import change_theme

mod = "mod4"
terminal = guess_terminal()
browser = "firefox"
text_editor = "codium"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key(
        [mod],
        "r",
        lazy.spawncmd(),
        desc="Spawn a command using a prompt widget",
    ),
    # Rofi
    Key(
        [mod], "p", lazy.spawn(os.path.expanduser("~/.config/qtile/rofi/bin/launcher"))
    ),
    Key(
        [mod], "x", lazy.spawn(os.path.expanduser("~/.config/qtile/rofi/bin/powermenu"))
    ),
    Key([mod], "m", lazy.spawn(os.path.expanduser("~/.config/qtile/rofi/bin/mpd"))),
    Key(
        [mod],
        "s",
        lazy.spawn(os.path.expanduser("~/.config/qtile/rofi/bin/screenshot")),
    ),
    Key(
        ["mod1"],
        "Tab",
        lazy.spawn(os.path.expanduser("~/.config/qtile/rofi/bin/windows")),
    ),
    # Custom script for changing themes
    Key(["control", "mod1"], "t", lazy.function(change_theme)),
    # Apps
    Key(
        [mod],
        "b",
        lazy.spawn(browser),
    ),
    Key(
        [mod],
        "f",
        lazy.spawn("thunar"),
    ),
    Key(
        [mod],
        "e",
        lazy.spawn(text_editor),
    ),
    Key(
        [mod],
        "c",
        lazy.spawn("color-gpick"),
    ),
    # Terminal apps
    Key(
        ["control", "mod1"],
        "v",
        lazy.spawn(terminal + " -e vim"),
    ),
    Key(
        ["control", "mod1"],
        "h",
        lazy.spawn(terminal + " -e htop"),
    ),
    Key(
        ["control", "mod1"],
        "r",
        lazy.spawn(terminal + " -e ranger"),
    ),
    # TODO: Brightness & that kind of stuff (too lazy to do it rn)
]

groups = [Group(i) for i in ["", "", "", "", "", "", ""]]

groups.append(Group("", matches=[Match(wm_class="Lxappearance")]))

for i, g in enumerate(groups, start=1):
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                str(i),
                lazy.group[g.name].toscreen(),
                desc="Switch to group {}".format(g.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                str(i),
                lazy.window.togroup(g.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(g.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.MonadTall(
        border_focus=theme["blue"],
        border_normal=theme["background"],
        margin=10,
        border_width=2,
    ),
    layout.Max(),
]

widget_defaults = dict(
    font="Iosevka Nerd Font", fontsize=13, padding=1, foreground=theme["foreground"]
)
extension_defaults = widget_defaults.copy()

separator = lambda: widget.TextBox(
    text=" ◆ ",
    background=theme["background"],
    foreground=theme["foreground"],
    padding=2,
)

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(
                    background=theme["yellow"], foreground=theme["background"], width=65
                ),
                separator(),
                widget.GroupBox(
                    disable_drag=True,
                    foreground=theme["foreground"],
                    highlight_method="line",
                    highlight_color=theme["background"],
                    block_highlight_text_color=theme["blue"],
                    this_current_screen_border=theme["blue"],
                    urgent_border=theme["red"],
                    urgent_text=theme["red"],
                    padding=1,
                    active=theme["green"],
                    inactive=theme["foreground"],
                ),
                separator(),
                widget.Prompt(cursor_color=theme["cursor"]),
                separator(),
                widget.Spacer(),
                widget.Mpd2(play_states={"pause": "", "play": "", "stop": ""}),
                widget.Spacer(),
                widget.TextBox(" ", foreground=theme["blue"]),
                widget.PulseVolume(),
                separator(),
                widget.TextBox(text="爵 ", foreground=theme["cyan"]),
                widget.Net(format="{down} {up}"),
                separator(),
                # widget.Battery(
                #     format="{char} {percent:2.0%}",
                #     charge_char="",
                #     discharge_char="",
                #     empty_char="",
                # ),
                # separator(),
                widget.Systray(),
                separator(),
                widget.TextBox(" ", foreground=theme["red"]),
                widget.Clock(format="%Y-%m-%d %I:%M %p"),
            ],
            28,
            background=theme["background"],
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_focus=theme["blue"],
    border_normal=theme["background"],
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class="floating-app"),  # custom class for floating apps
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None


@hook.subscribe.startup
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.Popen(["feh", "--no-fehbg", "--bg-fill", theme["wallpaper"]])
    set_colors(theme)
    subprocess.Popen([home])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
