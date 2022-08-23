from html import escape

from gi.repository import GLib
from gi.repository import Playerctl as Pctl
from libqtile.widget import base


class PlayerCtl(base.ThreadPoolText):
    defaults = [
        ("update_interval", 0.5, "Interval of update widget"),
    ]

    def __init__(self, **config):
        super().__init__("Initializing", **config)
        self.add_defaults(PlayerCtl.defaults)

    def poll(self):
        try:
            player = Pctl.Player.new()
            status = player.props.playback_status
            if status == 0:
                symbol = ""
            elif status == 1:
                symbol = ""
            else:
                symbol = ""
            if player.props.shuffle:
                shuffle_symbol = "列"
            else:
                shuffle_symbol = "劣"
            if player.props.loop_status != 0:
                loop_symbol = "凌"
            else:
                loop_symbol = "稜"
            formatted = f"{symbol} {player.get_artist()} - {player.get_title()} {loop_symbol} {shuffle_symbol}"
            return escape(formatted)
        except:
            return "No device playing"
