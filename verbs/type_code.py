from engine.text_engine import wrap_print

def type_code(game, code):
    if game.current_room.name == "Hallway":
        if not game.flags.get("iron_door_unlocked", False):
            correct_code = "five"
            if code.lower() == correct_code:
                game.flags["iron_door_unlocked"] = True
                return "The keypad beeps approvingly and the iron door unlocks with a loud clang!"
            else:
                return "The keypad flashes red. Incorrect code."
        else:
            return "The iron door is already unlocked."
    else:
        return "There is nothing here to type a code into."

def try_type_code(game, code):
    wrap_print(type_code(game, code))