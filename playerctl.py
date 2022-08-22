from html import escape

from gi.repository import GLib
from gi.repository import Playerctl as Pctl
from libqtile.widget import base


class PlayerCtl(base.ThreadPoolText):
    defaults = [
        ("update_interval", 2, "Interval of update widget"),
    ]

    def __init__(self, **config):
        super().__init__("Hola", **config)
        self.add_defaults(PlayerCtl.defaults)

    def poll(self):
        player = Pctl.Player.new()
        status = player.props.playback_status
        if status == 0:
            symbol = ""
        elif status == 1:
            symbol = ""
        else:
            symbol = ""
        formatted = f"{symbol} {player.get_artist()} - {player.get_title()}"
        return escape(formatted)
