from examine_item import examine_item
from take_item import take_item
from use_item import use_item_on_target
from turn_item import turn_item_in_direction
from say_phrase import say_phrase
from type_code import try_type_code
from enter_passage import enter_passage
from save_game_util import save_game, load_game, list_save_slots, delete_save_game
from item_util import show_inventory, normalize_item
from text_util import wrap_print
from room import describe_study_intro


def print_credits(game):
    print("\n--- CREDITS ---\n")
    for key in game.contributors:
        print(f"Name: {game.contributors[key].name}")
        print(f"Role: {game.contributors[key].role}")
        wrap_print(f"Contributions: {game.contributors[key].contributions}")
        print("")

def show_help():
    print("Commands you can use:")
    print(" - look or look around")
    print(" - examine <item>")
    print(" - take <item>")
    print(" - use <item> on <target>")
    print(" - enter <door or passage>")
    print(" - type <code>  (for keypads or consoles)")
    print(" - say <phrase>  (some locks respond to spoken words)")
    print(" - turn <item> <direction> (some objects can turn \"right\" or \"left\")")
    print(" - inventory")
    print(" - save <slot> (1-4)")
    print(" - load <slot (1-4)")
    print(" - delete <slot> (1-4)")
    print(" - saves (lists saved games)")
    print(" - help")
    print(" - quit or exit (to exit the game)")
    print(" - credits")

def end_game(game):
    print_credits(game)  # Show credits
    print(f"Thanks for playing {game.version}! Goodbye.\n")
    # Add any additional finalizations here, like saving progress or stats

def start_game(game):
    wrap_print(f"Welcome to {game.version}. Type 'help' to see a list of commands.\n")
    
    intro = ("You wake up in a haze, in a room that looks like a study. The room is unfamiliar, and something feels... off. "
        "As your eyes adjust, you notice ")
    description = describe_study_intro()
    description = description[0].lower() + description[1:]

    wrap_print(f"{intro}{description}")

    while True:
        command = input("\nWhat do you want to do? ").strip()
        process_command(game, command)

def process_command(game, command):
    command = command.lower().strip()

    if command == "help":
        show_help()
        return

    if command in ["look", "look around"]:
        wrap_print(game.current_room.description)
        return

    if command.startswith("examine "):
        item = normalize_item(command[len("examine "):].strip())
        examine_item(game, item)
        return

    if command.startswith("take "):
        item = normalize_item(command[len("take "):].strip())
        take_item(game, item)
        return

    if command.startswith("use "):
        parts = command[4:].split(" on ")
        if len(parts) == 2:
            item = normalize_item(parts[0].strip())
            target = normalize_item(parts[1].strip())
            use_item_on_target(game, item, target)
        else:
            print("Use command format: 'use <item> on <target>'")
        return
    
    if command.startswith("turn "):
        parts = command[5:].rsplit(" ", 1)
        if len(parts) == 2:
            item = normalize_item(parts[0].strip())
            direction = normalize_item(parts[1].strip())
            turn_item_in_direction(game, item, direction)
        else:
            print("Turn command format: 'turn <item> <direction>'")
        return

    if command.startswith("enter "):
        passage_name = command[len("enter "):].strip()
        enter_passage(game, passage_name)
        return

    if command.startswith("type "):
        code = command[len("type "):].strip()
        try_type_code(game, code)
        return

    if command == "inventory":
        show_inventory(game)
        return
    if command.startswith("say "):
        phrase = command[len("say "):].strip()
        say_phrase(game, phrase)
        return

    if command == "quit" or command == "exit":
        #print(f"\nThanks for playing {game.version}! Goodbye.\n")
        #print(self.credits)
        end_game(game)
        exit()

    if command == "saves":
        list_save_slots(game)
        return

    if command.startswith("save "):
        try:
            slot = command[len("save "):].strip()
            save_game(game, slot)
        except ValueError:
            print("Use: save <slot number>")
        return

    if command.startswith("load "):
        try:
            slot = command[len("load "):].strip()
            load_game(game, slot)
        except ValueError:
            print("Use: load <slot number>")
        return
    
    if command.startswith("delete "):
        try:
            slot = command[len("delete "):].strip()
            delete_save_game(game, slot)
        except ValueError:
            print("Use: delete <slot number>")
        return
    
    if command == "credits":
        print_credits(game)
        return

    print("I don't understand that command. Type 'help' for options.")
    