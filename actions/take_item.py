from engine.item_engine import match_room_item, resolve_alias
from engine.text_engine import wrap_print

def take_shard(game, matched_item):
    game.flags["shard_taken"] = True
    game.flags["shard_visible"] = False  # Shard is no longer visible after being taken

def take_core(game, matched_item):
    game.flags["attunement_core_taken"] = True  # Mark the core as taken

take_data = {
    # Study
    "fire": {
        "takeable": False,
        "message": "You reach toward the fire, then think better of it. Even your boldness has limits.",
    },
    "firepoker": {
        "takeable": True,
        "message": "You grab the cold, metal firepoker.",
    },
    "floorboards": {
        "takeable": False,
        "message": "You tug at the floorboards, but they groan in protest. They’re not going anywhere — and neither are you, that way."
    },
    "globe": {
        "takeable": False,
        "message": "You could take it, but you would damage it.",
    },
    "key": {
        "takeable": False,
        "message": "You try to grab the key, but the heat from the fire burns your hand. There must be a safer way to take it.",
    },
    "letter": {
        "takeable": True,
        "message": "You carefully fold the letter and tuck it into your pocket.",
    },
    "parchment": {
        "takeable": True,
        "message": "The parchment crackles as you unfold it. " 
                    "Time has gnawed the edges, but the words remain — " 
                    "**'Five leads the way.'** "
                    "No signature. No context. Just that.",
    },
    "eyes": {
        "takeable": False,
        "message": "You don't want to make the portaint more unsettling."
    },
    "knob": {
        "takeable": True,
        "message": "You hold the heavy door knob in your hand.",
    },
    "core": {
        "takeable": True,
        "message": "You pick up the attunement core. It pulses gently, almost like it recognizes your touch.",
        "action": take_core,
    },
    "wooden door": {
        "takeable": False,
        "message": "It won't budge.",
    },
    "desk": {
        "takeable": False,
        "message": "The desk is heavy. You can't take it.",
    },
    "drawer": {
        "takeable": False,
        "message": "You don't want to take that.",
    },
    "fireplace": {
        "takeable": False,
        "message": "The fireplace is built into the wall.",
    },
    "couch": {
        "takeable": False,
        "message": "It's far too bulky to carry around.",
    },
    "teacup": {
        "takeable": False,
        "message": "This is really not the time to have tea.",
    },
    "ashes": {
        "takeable": False,
        "message": "No reason to carry ashes around.",
    },
    "candle": {
        "takeable": False,
        "message": "It's best to leave the candle where it is — for light and for warmth.",
    },
    "portrait": {
        "takeable": False,
        "message": "The portrait remains firmly mounted on the wall, its frame immovable. You could try to take it, but it's as fixed as the memories it holds.",
    },
    "encyclopedia": {
        "takeable": False,
        "message": "The volumes are brittle with age — too many to carry, and too delicate to disturb.",
    },
    "bookshelf": {
        "takeable": False,
        "message": "The bookshelf is built into the wall.",
    },
    "eye symbol": {
        "takeable": False,
        "message": "It's painted on the wall.",
    },
    # Hallway
    "keypad": {
        "takeable": False,
        "message": "The keypad is affixed to the wall.",
    },
    "plaque": {
        "takeable": False,
        "message": "The plaque is bolted to the wall.",
    },
    "note": {
        "takeable": False,
        "message": "The note is pinned firmly behind the plaque. It will rip if you take it.",
    },
    "intercom": {
        "takeable": False,
        "message": "You'd need a ladder, a screwdriver, and a good reason.",
    },
    "symbol": {
        "takeable": False,
        "message": "It represents something you cannot obtain so easily.",
    },
    "iron door": {
        "takeable": False,
        "message": "You can't take the iron door — it's bolted to the frame.",
    },
    "terminal": {
        "takeable": False,
        "message": "It's part of the lab equipment — far too complex to carry.",
    },
    "hourglass symbol": {
        "takeable": False,
        "message": "It's painted on the wall.",
    },
    "pipe": {
        "takeable": False,
        "message": "It's stuck to the wall.",
    },
    "twisted symbol": {
        "takeable": False,
        "message": "It's painted on the wall.",
    },
    "lamp": {
        "takeable": False,
        "message": "Its mounted on the wall.",
    },
    # Secret Chamber
    "shard": {
        "takeable": True,
        "message": "You pick up the glowing shard. It pulses gently in your hand, warm and impossibly light.",
        "action": take_shard
    },
    "glyphs": {
        "takeable": False,
        "message": "These are painted on the wall.",
    },
    "candles": {
        "takeable": False,
        "message": "There are too many, you might burn yourself.",
    },  
    "plinth": {
        "takeable": False,
        "message": "The plinth is part of the floor. You're not prying it out.",
    }, 
    "mirror": {
        "takeable": False,
        "message": "The mirror is fused into the plinth.",
    },
    "symbols": {
        "takeable": False,
        "message": "They represent something you cannot obtain so easily.",
    },
    "spiral symbol": {
        "takeable": False,
        "message": "It's painted on the wall.",
    },
    "fractured symbol": {
        "takeable": False,
        "message": "It's painted on the wall.",
    },
    "book": {
        "takeable": False,
        "message": "There's no reason to take it — its secrets won't travel with you.",
    },
    "diagram": {
        "takeable": False,
        "message": "It's writing. You can't take writing.",
    },
    "lanterns": {
        "takeable": False,
        "message": "Those are best left where they are",
    },
    # Lab
    "prism": {
        "takeable": False,
        "message": "It is firmly bolted on the ground. You can turn it, but you can't take it.",
    },
    "machinery": {
        "takeable": False,
        "message": "It's the size of a wardrobe and weighs a ton.",
    },
    "chamber": {
        "takeable": False,
        "message": "Thick glass, sealed tight. You sense it wasn’t meant to be moved — only opened.",
    },
    "lab door": {
        "takeable": False,
        "message": "No use trying to carry a door.",
    },
    "candle symbol": {
        "takeable": False,
        "message": "It's painted on the wall.",
    },
    "clock": {
        "takeable": False,
        "message": "Time doesn’t belong to you. Not here.",
    },
    "light": {
        "takeable": False,
        "message": "You definitely cannot take light!",
    },
    "distiller": {
        "takeable": False,
        "message": "It's heavy and clunky.",
    },
    "instruments": {
        "takeable": False,
        "message": "I think they are best left where they are.",
    },
    "combination lock": {
        "takeable": False,
        "message": "You can't take the lock; it's fixed in place, waiting for the right combination.",
    },  
}

def take(game, item):
    item = resolve_alias(game, item)
    matched_item = match_room_item(game, item)
    name = matched_item.get("name")

    if not matched_item:
        return f"There is no {item} to take."
        
    if name in game.inventory:
        return f"You already have the {name}"
        
    take_info = take_data.get(name, {})

    if not take_info.get("takeable", True):
        return take_info.get("message", f"The {name} can't be taken.") 
    
    if "action" in take_info:
        take_info["action"](game, name)
        
    game.inventory[name] = game.current_room.items_data.pop(name)
    return take_info.get("message", f"You take the {name}.")

def take_item(game, item):
    wrap_print(take(game, item))