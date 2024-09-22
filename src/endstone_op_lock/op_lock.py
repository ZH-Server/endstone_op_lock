from endstone.plugin import Plugin
from endstone.command import *
from endstone.event import PlayerCommandEvent, event_handler
import json, os

class OpLock(Plugin):
    api_version = "0.5"

    def on_enable(self) -> None:
        self.op_list_dir=os.path.join(os.getcwd(), "plugins", "lock_op")
        self.op_list_json=os.path.join(os.getcwd(), "plugins", "lock_op", "op_list.json")
        if not os.path.exists(self.op_list_json):
            os.makedirs(self.op_list_dir, exist_ok=True)
            with open(self.op_list_json,'w',encoding='utf-8') as f:
                json.dump({}, f, ensure_ascii=False, indent=4)
        self.register_events(self)
    
    @event_handler
    def on_use_op_cmd(self, event: PlayerCommandEvent) -> None:
        with open(self.op_list_json, 'r', encoding='utf-8') as f:
            op_data=json.load(f)
        if ["op", "deop"] in event.command:
            if event.player.is_op == True:
                op_info={
                    f"{event.player.name}": "True"
                }
                json.dump(op_info, f, ensure_ascii=False, indent=4)
                event.player.send_message(f"{event.command}")
