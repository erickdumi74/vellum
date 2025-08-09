
from item_util import describe_room_item, describe_inventory_item, resolve_alias
from text_util import wrap_print

def examine_door(game, item, unlocked_flag_name, unlocked_msg, locked_msg):
    description = describe_room_item(game, item)
    if game.flags.get(unlocked_flag_name, False):
        return f"{description}\n{unlocked_msg}"
    return f"{description}\n{locked_msg}"


def examine_wooden_door(game, item):   
    return examine_door(
        game,
        item,
        "knob_inserted",
        "It is unlocked and can be entered.",
        "It is locked. There is no knob, just a hole where one should be."
    )

def examine_iron_door(game, item):
    return examine_door(
        game,
        item,
        "iron_door_unlocked",
        "The wooden door is unlocked. The knob turns easily now, and the way is clear.",
        "The iron door is locked. You can't go through it yet."
    )

def examine_lab_door(game, item):
    return examine_door(
        game,
        item,
        "lab_door_unlocked",
        "The lab door is unlocked and can be opened.",
        "The lab door is locked. You can't go through it yet."
    )

def examine_globe(game, item):
    if game.flags.get("attunement_core_taken"):
        return (
            "The globe spins slowly, and now the small compartment remains open, "
            "but the attunement core is gone."
        )

    if game.flags.get("attunement_core_revealed"):
        return (
            "The globe spins slowly, and now the small compartment remains open, "
            "revealing a metallic orb: the attunement core."
        )

    if game.flags.get("mirror_vision_seen_twice"):
        count = game.flags.get("globe_examined_count", 0)

        if count == 0:
            game.flags["globe_examined_count"] = 1
            return "You spin the globe absentmindedly. Something inside clunks softly."

        if count == 1:
            game.flags["globe_examined_count"] = 2
            game.current_room.items_data["core"] = {
                "description": "A metallic orb nested inside the globe, pulsating with a dim, blue light.",
                "aliases": ["attunement core"]
                }
            game.flags["attunement_core_revealed"] = True
            return (
                "You give the globe another spin. The axis squeaks… then halts oddly. "
                "A small compartment pops open. Inside is a metallic orb: the attunement core."
            )

    return describe_room_item(game, item)

def examine_drawer(game, item):
    if game.flags.get("drawer_open"):
        contents = []
        if "letter" in game.current_room.items_data:
            contents.append("a folded letter")
        if "parchment" in game.current_room.items_data:
            contents.append("a worn parchment")
        if contents:
            if len(contents) > 1:
                joined = ", ".join(contents[:-1]) + f" and {contents[-1]}"
            else:
                joined = contents[0]
            return  f"The drawer is open, revealing {joined} within."
        return "The desk drawer is open, revealing its empty interior."
    return describe_room_item(game, item)


def examine_ashes(game, item):
    if game.flags.get("rusty_key_found"):
        return "A pile of ashes showing a rusty key."
    if game.flags.get("rusty_key_taken"):
        return "A pile of ashes where a rusty key was found."
    return describe_room_item(game, item)

def examine_letter(game, item):
    if game.flags["knob_found"]:
        return "The letter's back reveals a faint Roman numeral: V, made visible by the candle's warmth."
    return describe_room_item(game, item)
        
def examine_portrait(game, item):
    if game.flags.get("attunement_core_taken", False) and not game.flags.get("attunement_core_inserted", False):
        return ("The stern expression on the portrait seems to soften, just slightly, " 
        "as though it's considering something. There's a quiet, unsettling feeling that the "
        "portrait knows more than it lets on.")
    if game.flags.get("attunement_core_inserted", False):
        return ("You approach the portrait again, and you notice it — the subject is now grinning. " 
        "Not a smile, but a cold, knowing grin that was there all along, waiting. You feel the weight of " 
        "that grin in the air, the tension rising as if the portrait is silently watching your every move.")
    if game.flags.get("iron_door_unlocked", False):
            return "The eyes in the portrait... they moved. Just for a moment. You're sure of it."
    return describe_room_item(game, item)

def examine_encyclopedia(game, item):
    if game.flags["knob_found"] and "knob" not in game.inventory:
        return "Volume 'V' in the encyclopedia has a small knob attached. Could it fit somewhere?"
    if game.flags["knob_found"] and "knob" in game.inventory:
        return "Volume 'V' in the encyclopedia now has a small indentation where the knob once rested."
    return describe_room_item(game, item)

def examine_desk(game, item):
    item_msg = describe_room_item(game, item)
    unlocked_msg = "The drawer is unlocked" if game.flags["drawer_open"] else ""
    return f"{item_msg}\n{unlocked_msg}"
    
def examine_plaque(game, item):
    item_msg = describe_room_item(game, item)

    if not game.flags["plaque_examined"]:
        game.flags["plaque_examined"] = True
        # Add the note to the room
        game.current_room.items_data["note"] = {
            "description": ("A torn note is pinned behind the plaque, barely legible. "
                "It reads: '...they listen even when we sleep. Vellum... watches.'"),
            "aliases": ["torn note"]
        }
        examine_msg = "As you examine it more closely, you notice a faintly pinned note tucked just behind the edge."
    elif game.flags["plaque_examined"] and not game.flags["note_examined"]:
        examine_msg = "There is a faintly pinned note tucked just behind the edge."
    else:
        return item_msg
    
    return f"{item_msg}\n{examine_msg}"

def examine_intercom(game, item):
    if game.flags.get("mirror_vision_seen_twice"):
        return "The intercom crackles to life. You hear a faint voice, barely audible, but unmistakable. It whispers, '...Vellum...' The static hisses and the voice fades into silence again."
    else:
        return describe_room_item(game, item)
    
def examine_note(game, item):
    if game.flags["plaque_examined"]:
        game.flags["note_examined"] = True
        return ("The torn note is pinned just behind the plaque, barely legible. "
                "It reads: '...they listen even when we sleep. Vellum... watches.' "
                "It's fixed in place — you can't take it, but its message lingers.")
    else:
        return "You see no 'note' worth examining."
    
def examine_terminal(game, item):
    item_msg = describe_room_item(game, item)
        
    if "shard" in game.inventory:
        if not game.flags.get("shard_inserted", False):
            examine_msg = "The glowing shard pulsates as you get closer to the terminal"
    else:
        if game.flags.get("shard_inserted", False):
            examine_msg = "The glowing shard is already inserted, its faint pulse steady within the terminal's slot. The terminal waits patiently for your command."
        else:
            examine_msg = "There's a shallow slot beside it. Looks like something might fit, but the terminal remains unresponsive for now."
    
    return f"{item_msg}\n{examine_msg}" 

def examine_plinth(game, item):
    item_msg = describe_room_item(game, item)
    if game.flags["shard_visible"] and not game.flags["shard_taken"]:
        examine_msg = "The glowing shard revealed still rests at its base."
    elif game.flags["shard_taken"]:
        examine_msg = "The plinth is empty now, its base where the shard once lay is bare."
    else:
        return item_msg

    return f"{item_msg}\n{examine_msg}"

def examine_mirror(game, item):
    if not game.flags.get("mirror_vision_seen_once"):
        game.flags["mirror_vision_seen_once"] = True
        if not game.flags.get("shard_visible"):
            game.flags["shard_visible"] = True
            game.current_room.items_data["shard"] = {
                "description": "A strange crystal shard, faintly glowing with violet light. It seems important.",
                "aliases": ["glowing shard"]
            }
        return ("You lean in. The mirror doesn't reflect you — instead, a shadowy figure appears, inserting a glowing shard into a console. "
                "A whisper drifts into your mind: 'Vellum... you are the successor.' As the vision fades, a soft glow appears at the base of the plinth.")
    elif not game.flags.get("mirror_vision_seen_twice"):
        game.flags["mirror_vision_seen_twice"] = True
        return ("This time, the vision lingers. A shadowy figure turns the dial on a globe. "
                "The vision fades — leaving behind a sense of direction, as though something has shifted in the world around you.")
    else:
        # Mirror is cracked and no longer shows visions after the second vision
        item_msg = "The mirror is cracked, faintly humming "
        if not game.flags.get("shard_taken"):
            examine_msg = "and a soft reflection of the globe's movement catches your eye, but the shard it revealed still rests nearby."
        else:
           examine_msg = "and a soft reflection of the globe's movement catches your eye, but the base where the shard once lay is now bare."
        return f"{item_msg}\n{examine_msg}"
    
def examine_reflecting_mirror (game, mirror_side, item):
    if not game.flags.get("attunement_core_inserted", False):
        return describe_room_item(game, item)

    reflected_item = game.mirror_refractions[game.current_refraction_index]

    if item == reflected_item:
        responses = {
            "center": "As the light strikes the mirror, the surface shimmers, revealing an hourglass glowing faintly, its shape shifting with the light.",
            "right": "As the light strikes the mirror, the surface shimmers, revealing an eye glowing faintly, its gaze shifting, almost as if watching you.",
            "left": "As the light strikes the mirror, the surface shimmers, revealing a spiral glowing faintly, its edges twisting and stretching with the light."
        }
        return responses.get(mirror_side, "The mirror shimmers faintly but nothing else happens.")
    else:
        return "The mirror reflects the light, but nothing special happens."
    
def examine_center_mirror(game, item):
    return examine_reflecting_mirror(game, "center", item)

def examine_right_mirror(game, item):
    return examine_reflecting_mirror(game, "right", item)

def examine_left_mirror(game, item):
    return examine_reflecting_mirror(game, "left", item)

def examine_prism(game, item):
    description = describe_room_item(game, item)
    if game.flags["attunement_core_inserted"]:
        description += f" The prism is currently pointing at the {game.mirror_refractions[game.current_refraction_index]}."
    return description

def examine_inventory_item(game, item):
    look_msg = f"You look closely at the {item} in your inventory."

    handler = inventory_describe_data.get(item)
    item_msg = handler(game, item) if handler else describe_inventory_item(game, item)
        
    return f"{look_msg}\n{item_msg}"

def describe_inventory_letter(game, item):
    if game.flags["knob_found"]:
        item_msg = "On the back of the letter, revealed by the candle's warmth, is a faint Roman numeral: V."
    else:
        item_msg = describe_inventory_item(game, item)
    return item_msg

def resolve_alias_message(game, term):
    resolved = resolve_alias(game, term)
    if not resolved:
        return None

    name = resolved["name"]
    source = resolved["source"]

    if source == "inventory":
        return examine_inventory_item(game, name)
    else:  # source == "room"
        handler = examine_data.get(name)
        return handler(game, name) if handler else describe_room_item(game, name)


inventory_describe_data = {
    "letter": describe_inventory_letter,
}

examine_data = {
    # Study
    "globe": examine_globe,
    "drawer": examine_drawer,
    "ashes": examine_ashes,
    "letter": examine_letter,
    "portrait": examine_portrait,
    "wooden door": examine_wooden_door,
    "encyclopedia": examine_encyclopedia,
    "desk": examine_desk,
    # Hallway
    "plaque" : examine_plaque,
    "iron door": examine_iron_door,
    "intercom": examine_intercom,
    "note": examine_note,
    "terminal": examine_terminal,
    # Secret Chamber
    "lab door": examine_lab_door,
    "plinth": examine_plinth,
    "mirror": examine_mirror,
    # Lab
    "right mirror": examine_right_mirror,
    "center mirror": examine_center_mirror,
    "left mirror": examine_left_mirror,
    "prism": examine_prism,
}

def examine(game, item):

    message = resolve_alias_message(game, item)
    if message:
        return message
    else:
        return f"There is no {item} to examine."
    
def examine_item(game, item):
    wrap_print(examine(game, item))