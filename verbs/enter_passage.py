from engine.text_engine import wrap_print

# Entry conditions per passage
passage_rules = {
    "lab door": {
        "required_flag": "lab_door_unlocked",
        "locked_message": "The lab door is still locked. You can't go through it quite yet."
    },
    "iron door": {
        "required_flag": "iron_door_unlocked",
        "locked_message": "The iron door is still locked. You can't go through it quite yet."
    },
    "wooden door": {
        "required_flag": "wooden_door_unlocked",
        "locked_message": "It's missing a knob. You can't go through it yet."
    },
    # You can add more doors here easily
}

def enter(game, passage_name):
    passage_name = passage_name.lower().strip()
    current_room = game.current_room

    if passage_name not in current_room.exits:
        return(f"There is no {passage_name} here to enter.")

    rule = passage_rules.get(passage_name)
    if rule and not game.flags.get(rule["required_flag"], False):
        return(rule["locked_message"])

    # Move to the next room
    next_room = current_room.exits[passage_name]
    game.current_room = next_room
    return(f"You enter the {passage_name} and find yourself in the {next_room.name}.\n{next_room.description}")

def enter_passage(game, passage_name):
    wrap_print(enter(game, passage_name))
