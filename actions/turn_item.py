from engine.item_util import match_room_item, resolve_alias
from engine.text_util import wrap_print


def turn_prism(game, direction):
    if not game.flags.get("attunement_core_inserted", False):
        return f"The prism rotates {direction}, but with no effect. Looks like it's not powered and still dormant."

    if direction == "right":
        game.current_refraction_index = (game.current_refraction_index + 1) % len(game.mirror_refractions)
    elif direction == "left":
        game.current_refraction_index = (game.current_refraction_index - 1) % len(game.mirror_refractions)
    return f"The light is now pointing to: {game.mirror_refractions[game.current_refraction_index]}."

turn_inventory_data = {
    "knob": {"message" : "You turn the knob to the {direction} in midair. The door remains locked."}
}

turn_item_data = {
    "fire": {"message" : "You try to twist the fire with your hands, but it only crackles in amusement — untouchable, untamed."},
    "floorboards": {"message" : "You press your foot and twist — the floorboards creak and shudder, but they hold fast, too weary to dance for you."},
    "portrait": {"message" : "You try to turn the portrait, but it feels unnaturally resistant, as if some unseen force is holding it in place. No matter how hard you push, it refuses to move."},
    "globe": {"message": "You spin the globe slowly to the {direction}. The faint hum of its movement fades as it comes to a quiet stop, its surface still and expectant."},
    "candle": {"message": "You turn the candle slowly to the {direction}. The wax softens, but the flame flickers, staying steady and unchanging."},
    "teacup": {"message": "You turn the teacup slowly to the {direction}. It wobbles slightly, the cracks catching the light — delicate and unchanged."},
    "encyclopedia": {"message": "You turn the books slowly to the {direction}. They're old, their spines brittle. You hesitate to disturb them too much."},
    "ashes": {"message": "You turn the ashes slowly to the {direction} with the poker. The embers shift, but nothing new is revealed."},
    "bookshelf": {"message": "You try to turn the bookshelf, but it's firmly anchored to the wall. It won't budge."},
    "fireplace": {"message": "You try to turn the fireplace, but it's firmly anchored to the wall. It won't budge."},
    "desk": {"message": "You try to turn the desk, but it's too heavy. It won't budge."},
    "prism": {"action": turn_prism},
}

direction_alias = {
    "clockwise": "right",
    "counter-clockwise": "left",
    "counter clockwise": "left",
}

def turn_item(game, item, direction):
    direction = direction_alias.get(direction, direction)
    item = resolve_alias(game, item)
    item_name = item.get("name")

    if direction not in ("right", "left"):
        return f"You try turning it {direction}, but nothing seems to happen. (Only 'left' or 'right' seem to work.)"
    
    # first verify if item is in inventory
    if item_name in game.inventory:
        inventory_item_data = turn_inventory_data.get(item_name)
        return inventory_item_data["message"].format(direction=direction) if inventory_item_data else f"You turn the {item_name} to the {direction} in midair. You feel kind of silly after doing it."
    
    # next try to match item in room
    matched_item = match_room_item(game, item)

    if not matched_item:
        return f"You see no {item_name} to turn."
        
    # Define turn messages or actions for items
    turn_data = turn_item_data.get(matched_item.get("name"))

    if turn_data:
        if "message" in turn_data:
            output = turn_data["message"].format(direction=direction)
        elif "action" in turn_data:
            output = turn_data["action"](game, direction)
        return output
    
    return f"You can't quite turn the {item}."

def turn_item_in_direction(game, item, direction):
    wrap_print(turn_item(game, item, direction))
