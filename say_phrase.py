from text_util import wrap_print

def unlock_lab_door(game, phrase):
    if game.current_room.name == "Hallway":
        if phrase == "vellum":
            # Track that the player has said 'vellum'
            game.flags["code_spoken"] = True
            
            # If shard is inserted, unlock the door
            if game.flags.get("shard_inserted", False):
                if not game.flags["lab_door_unlocked"]:
                    game.flags["lab_door_unlocked"] = True  # Unlock the Lab door
                    return "The terminal hums faintly, its screen flickering. You hear something click in the distance, like a lock disengaging."
                else:
                    return "The terminal hums faintly, but no further action occurs — the lab door is already unlocked."
            else:
                return "The terminal flickers, accompanied by a stuttering, electronic buzz. Nothing happens. It seems like something is missing..."

# to analyze
def unlock_combination_lock(game, phrase):
    if game.current_room.name != "Lab":
        return "There is no combination lock here."

    if game.flags.get("combination_lock_unlocked", False):
        return "The combination lock has been unlocked. It no longer accepts input."

    expected_sequence = ["eye", "hourglass", "spiral"]
    normalized_phrase = phrase.lower().replace(" symbol", "")

    if normalized_phrase not in expected_sequence:
        game.correct_lock_count = 0
        return "You hear the gears shift back into their starting position, and the lock resets."

    expected_phrase = expected_sequence[game.correct_lock_count]

    if normalized_phrase == expected_phrase:
        game.correct_lock_count += 1
        if game.correct_lock_count == len(expected_sequence):
            game.flags["combination_lock_unlocked"] = True
            return "You whisper 'spiral'. The final gear clicks into place, and the lock opens with a satisfying click."
        else:
            return f"You whisper '{normalized_phrase}'. The gear clicks into place."
    else:
        game.correct_lock_count = 0
        return "The lock rattles, frustrated by the incorrect sequence. It shifts back into its default position, waiting for you to try again."

def unlock_combination_lock(game, phrase):
    if game.current_room.name == "Lab":
        if not game.flags["combination_lock_unlocked"]:
            frustration_message = "The lock rattles, frustrated by the incorrect sequence. It shifts back into its default position, waiting for you to try again."
            if phrase == "eye" or phrase == "eye symbol":
                if game.correct_lock_count == 0:
                    game.correct_lock_count += 1
                    return "You whisper 'eye'. The first gear clicks into place."
                else: # incorrect sequence reset
                    game.correct_lock_count = 0
                    return frustration_message
            if phrase == "hourglass" or phrase == "hourglass symbol":
                if game.correct_lock_count == 1:
                    game.correct_lock_count += 1
                    return "You whisper 'hourglass'. The second gear clicks into place."
                else: # Incorrect sequence reset
                    game.correct_lock_count = 0
                    return frustration_message
            if phrase == "spiral" or phrase == "spiral symbol":
                if game.correct_lock_count == 2:
                    game.flags["combination_lock_unlocked"] = True
                    return "You whisper 'spiral'. The final gear clicks into place, and the lock opens with a satisfying click."
                else: # Incorrect sequence reset
                    game.correct_lock_count = 0
                    return frustration_message
            
            game.correct_lock_count = 0
            return "You hear the gears shift back into their starting position, and the lock resets."
        else:
            return "The combination lock has been unlocked. It no longer accepts input."    

symbol_aliases = {
    "eye symbol": "eye",
    "hourglass symbol": "hourglass",
    "spiral symbol": "spiral"
}

say_actions = {
    "vellum": unlock_lab_door,
    "eye": unlock_combination_lock,
    "hourglass": unlock_combination_lock,
    "spiral": unlock_combination_lock,
}

def say(game, phrase):
    phrase = symbol_aliases.get(phrase.lower(), phrase.lower())
    if phrase in say_actions:
        response = say_actions[phrase](game, phrase)
        return response or f"You say '{phrase}', but nothing happens."
    
    return f"You say '{phrase}', but your words echo in the silence..."


def say_phrase(game, phrase):
    wrap_print(say(game, phrase))
