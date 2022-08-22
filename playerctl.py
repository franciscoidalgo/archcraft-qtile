from html import escape

from gi.repository import GLib
from gi.repository import Playerctl as Pctl
from libqtile.widget import base


class PlayerCtl(base.ThreadPoolText):
    defaults = [
        ("update_interval", 2, "Interval of update widget"),
        ("mouse_buttons", keys, "b_num -> action."),
    ]

    def __init__(self, **config):
        super().__init__("Hola", **config)
        self.add_defaults(PlayerCtl.defaults)

    def poll(self):
        player = Pctl.Player.new()
        formatted = f" {player.get_artist()} - {player.get_title()}"
        return escape(formatted)
