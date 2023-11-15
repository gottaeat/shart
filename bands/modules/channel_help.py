from bands.colors import MIRCColors

# pylint: disable=invalid-name
c = MIRCColors()


# pylint: disable=too-few-public-methods
class ChannelHelp:
    def __init__(self, channel, user, user_args):
        self.channel = channel
        self.user = user  # unused
        self.user_args = user_args  # unused

        self._run()

    def _run(self):
        msg = f"{c.WHITE}├ {c.LRED}usage\n"
        msg += f"{c.WHITE}│ ├ {c.LGREEN}?advice{c.RES} {{target}}\n"
        msg += f"{c.WHITE}│ ├ {c.LGREEN}?bands{c.RES}\n"
        msg += f"{c.WHITE}│ ├ {c.LGREEN}?help{c.RES}\n"
        msg += f"{c.WHITE}│ ├ {c.LGREEN}?piss{c.RES}   [target]\n"
        msg += (
            f"{c.WHITE}│ └ {c.LGREEN}?tarot{c.RES}  has its own detailed help prompt\n"
        )
        msg += (
            f"{c.WHITE}└ {c.LRED}src{c.RES}       https://github.com/gottaeat/bands\n"
        )

        self.channel.send_query(msg)