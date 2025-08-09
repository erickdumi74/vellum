from item_util import match_room_item, resolve_alias
from text_util import wrap_print

def poke_ashes(game, item, target):
    if not game.flags["rusty_key_found"]:
        game.flags["rusty_key_found"] = True
        # Add rusty key to room items so player can take it
        game.current_room.items_data["key"] = {
            "description": "A small rusty key, found hidden beneath the ashes.",
            "aliases": ["rusty key"]
            }
        return ("You poke the ashes and the fireplace; something shifts beneath the embers. A rusty key is revealed!")
    else:
        return ("Nothing more happens when you poke the ashes.")

def poke_globe(game, item, target):
    if not game.flags["attunement_core_taken"]:
        return ("You tap the globe with the firepoker. There's a soft clink — something inside shifts. It stops spinning for a brief moment... then starts again.")
    else:
        return ("You tap the globe with the firepoker. It no longer clinks — whatever was inside is gone.")

def poke_key(game, item, target):
    game.flags["rusty_key_taken"] = True
    game.flags["rusty_key_found"] = False  
    game.inventory[target] = game.current_room.items_data[target] # Add it to the inventory
    del game.current_room.items_data["key"] 
    return ("You carefully use the firepoker to lift the key. It feels heavy, the rusted metal cool to the touch.")

def use_key_on_drawer(game, item, target):
    if "key" in game.inventory:
        game.flags["drawer_open"] = True
        # Reveal letter and cryptic note
        game.current_room.items_data["letter"] = {
            "description": "It's a simple folded letter, nothing special on the front.",
            "aliases": ["folded letter"]
            }
        game.current_room.items_data["parchment"] = {
            "description": "A worn parchment that reads: 'Five leads the way.'",
            "aliases": ["worn parchment"]
        }
        return("You use the rusty key to unlock the desk drawer. Inside, you find a folded letter and a worn parchment.")
    else:
        return("You don't have the rusty key.")

def use_letter_on_candle(game, item, target):
    if "letter" in game.inventory:
        game.flags["knob_found"] = True
        # Add knob to the encyclopedia so it can be taken
        if "knob" not in game.current_room.items_data:
            game.current_room.items_data["knob"] = {
                "description": "A small, heavy door knob hidden inside one volume of the encyclopedia.",
                "aliases": ["door knob", "small knob", "heavy knob"]
                }
        return("You hold the letter close to the candle flame. On the back, a faint Roman numeral 'V' appears!")
    else:
        return("You don't have the letter to examine with the candle.")

def use_knob_on_door(game, item, target):
    if "knob" in game.inventory:
        game.flags["knob_inserted"] = True  # Mark the knob as inserted
        game.flags["wooden_door_unlocked"] = True  # This flag specifically tracks the wooden door's state
        del game.inventory["knob"]
        return("You fit the knob you found in the encyclopedia onto the wooden door. You hear a satisfying click as it unlocks.")
    else:
        return("You don't have a knob to use.")
    
def use_shard_on_terminal(game, item, target):
    if not game.flags.get("shard_inserted", False):
        output = ("You slide the glowing shard into the terminal's slot. It fits perfectly.")
        game.flags["shard_inserted"] = True  # Mark the shard as inserted
        del game.inventory["shard"]

        # If 'vellum' has already been said, unlock the lab door
        if game.flags.get("code_spoken", False) and not game.flags.get("lab_door_unlocked", False):
            game.flags["lab_door_unlocked"] = True  # Unlock the Lab door
            code_spoken_msg = ("The terminal hums faintly, its screen flickering. You hear something distant click, like a lock disengaging.")
            return f"{output}\n{code_spoken_msg}"

        return output
    else:
        return ("The shard is already inserted. The terminal awaits further instructions.")

def use_core_on_prism(game, item, target):
    if "core" in game.inventory:
        if not game.flags.get("attunement_core_inserted", False):
            game.flags["attunement_core_inserted"] = True  # Mark core as inserted
            del game.inventory["core"]
            # Trigger the effect of the core insertion (glowing, humming, etc.)
            return ("You slide the attunement core into the prism's slot. It clicks into place."
                    "The prism hums softly, light refracting in strange patterns directly at specific objects in the room.")
        else:
            return ("The attunement core is already inserted. The prism awaits your command.")
    else:
        return ("You need to have the attunement core in your inventory to use it.")

item_use_data = {
    ("firepoker", "ashes"): {"action": poke_ashes},
    ("firepoker", "fireplace"): {"action": poke_ashes},
    ("firepoker", "drawer"): {"message": "You will probably break it."},
    ("firepoker", "floorboards"): {"message": "You jab at the floorboards with whatever you can muster. Dust stirs. They creak, tired and unbothered, like old bones long past caring."},
    ("firepoker", "desk"): {"message": "You will probably break it."},
    ("firepoker", "portrait"): {"message": "Its eerie, but not enough to make you want to rip it."},
    ("firepoker", "wooden door"): {"message": "It's too thick to poke through."},
    ("firepoker", "couch"): {"message": "Its already old and torn."},
    ("firepoker", "candle"): {"message": "You tap the candle with the firepoker. The flame wavers, then steadies — unimpressed by your efforts."},
    ("firepoker", "globe"): {"action": poke_globe},
    ("firepoker", "key"): {"action": poke_key},
    ("firepoker", "fire"): {"message": "You jab at the flames. Sparks leap, and the fire hisses in reply, disturbed but far from threatened."},
    ("firepoker", "eyes"): {"message": "You point the firepoker toward the painted eyes, but something deep within you says no. Not these eyes. Not yet."},
    ("key", "drawer"): {"action": use_key_on_drawer},
    ("letter", "candle"): {"action": use_letter_on_candle},
    ("knob", "wooden door"): {"action": use_knob_on_door},
    ("shard", "terminal"): {"action": use_shard_on_terminal},
    ("core", "prism"): {"action": use_core_on_prism},
}

def use_item(game, item, target):
    item = resolve_alias(game, item.lower())
    if not item:
        return "You don’t have that item, and you don’t see it in the room."
    item_name = item.get("name")

    target = resolve_alias(game, target.lower())
    if not target:
        return f"You don’t see anything like that to use {item_name} on."
    target_name = target.get("name")

    # Confirm item is in inventory
    if item_name not in game.inventory:
        return f"You don’t have a {item_name} to use."

    # Confirm target is in the room
    matched_target = match_room_item(game, target)
    if not matched_target:
        return f"You don’t see any {target_name} here."

    # Retrieve specific item/target pair logic
    use_data = item_use_data.get((item_name, target_name))
    if use_data:
        if "message" in use_data:
            return use_data["message"]
        elif "action" in use_data:
            return use_data["action"](game, item_name, target_name)

    return f"Using the {item_name} on the {target_name} has no effect."


def use_item_on_target(game, item, target):
    wrap_print(use_item(game, item, target))