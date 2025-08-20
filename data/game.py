import os
import sys
from data.room import setup_rooms
from data.contributor import setup_credits
from engine.game_util import start_game

class Game:
    def __init__(self):
        self.version = "Vellum 0.60"
        self.base_path = os.path.dirname(os.path.abspath(sys.argv[0]))
        self.save_dir = os.path.join(self.base_path, "saves")
        self.mirror_refractions = ["chamber", "left mirror", "machinery", "center mirror", "distiller", "clock", "right mirror", "lab door"]
        self.current_refraction_index = 0  # Start at the first refraction
        self.correct_lock_count = 0
        self.flags = {
            "wooden_door_unlocked": False,
            "rusty_key_found": False,
            "rusty_key_taken": False,
            "knob_found": False,
            "knob_inserted": False,
            "drawer_open": False,
            "iron_door_unlocked": False,
            "plaque_examined": False,
            "note_examined": False,
            "lab_door_unlocked": False,
            "attunement_core_revealed": False,
            "attunement_core_inserted": False,
            "shard_inserted": False,
            "shard_taken": False,
            "shard_visible": False,
            "attunement_core_taken": False,
            "attunement_core_inserted": False,
            "combination_lock_unlocked": False,
        }
        self.inventory = {}
        self.contributors = setup_credits()
        self.rooms = setup_rooms()
        self.current_room = self.rooms["Study"]

    def start(self):
        start_game(self)
