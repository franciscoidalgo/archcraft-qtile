from libqtile.widget import base
from subprocess import run
import html


class PlayerCtl(base.ThreadPoolText):
    defaults = [
        ("update_interval", 2, "Interval of update widget"),
        ("mouse_buttons", keys, "b_num -> action."),
    ]

    def __init__(self, **config):
        super().__init__("Hola", **config)
        self.add_defaults(PlayerCtl.defaults)

    def poll(self):
        pipe = run(
            [
                "playerctl",
                "metadata",
                "--format",
                "{{ artist }} - {{ trunc(title, 40) }}",
            ],
            capture_output=True,
            text=True,
        )
        formatted = " " + pipe.stdout.strip().replace("&", "&amp;")
        return formatted
