from endstone.plugin import Plugin
from endstone.command import *
from endstone.event import PlayerCommandEvent, event_handler

class OpLock(Plugin):
    api_version = "0.5"

    def __init__(self):
        super().__init__()
        self.oplist: list[str] = []

    def on_enable(self) -> None:
        self.save_default_config()
        self.load_config()
        self.register_events(self)

    @event_handler
    def on_change_permissions(self, event: PlayerCommandEvent) -> None:
        if ["op", "deop"] in event.command:
            if event.player.is_op == True and event.player.name in self.oplist and event.player.name != "Server":
                event.player.perform_command(event.command)
            else:
                event.player.send_error_message("You isn't allowed to change permissions")
                event.cancelled

    def load_config(self) -> None:
        self.oplist = self.config["op_allowed"]
