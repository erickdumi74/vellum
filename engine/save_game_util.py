import os
import json
import time

def save_game(game, slot):
    slot = str(slot)
    
    if not slot.isdigit():
        print("Please use a numeric slot (e.g., 'save 1').")
        return

    slot_num = int(slot)
    if slot_num < 1 or slot_num > 4:
        print("You can only use save slots 1 to 4.")
        return
    
    # create save directory if not exists
    if not os.path.exists(game.save_dir):
        os.makedirs(game.save_dir)

    filename = os.path.join(game.save_dir, f"save{slot_num}.json")

    if os.path.exists(filename):
        confirm = input(f"Slot {slot_num} already exists. Overwrite? (y/n): ").strip().lower()
        if confirm != 'y':
            print("Save cancelled.") 
            return

    data = {
        "inventory": game.inventory,
        "flags": game.flags,
        "current_room": game.current_room.name,
        "room_items": {room_name: room.items_data for room_name, room in game.rooms.items()},  # Save room items,
    }

    try:
        with open(filename, 'w') as f:
            json.dump(data, f)
        print(f"Game saved to slot {slot_num}.")
    except Exception as e:
        print(f"An error occurred while saving the game: {e}")

def load_game(game, slot):
    slot = int(slot)
    
    if not (1 <= slot <= 4):
        print("Invalid slot. Please choose a number between 1 and 4.")
        return

    filename = os.path.join(game.save_dir, f"save{slot}.json")
    if not os.path.exists(filename):
        print(f"No saved game in slot {slot}.")
        return

    try:
        with open(filename, "r") as f:
            state = json.load(f)

        game.flags = state["flags"]
        game.inventory = state["inventory"]
        game.current_room = game.rooms[state["current_room"]]

        # Restore room items
        for room_name, items in state["room_items"].items():
            game.rooms[room_name].items_data = items

        print(f"Game loaded from slot {slot}.")
        print(game.current_room.description)
    except Exception  as e:
        print(f"An error occurred while loading the game: {e}")

def list_save_slots(game):
    found = False
    print("Available save slots (1–4):")
    for i in range(1, 5):
        filename = os.path.join(game.save_dir, f"save{i}.json")
        if os.path.exists(filename):
            timestamp = os.path.getmtime(filename)
            readable = time.ctime(timestamp)
            try:
                with open(filename, "r") as f:
                    state = json.load(f)

                current_room = game.rooms[state["current_room"]]
            except Exception as e:
                print(f"An error occurred while obtaining the room from save: {e}")
            print(f" - Slot {i}: {current_room.name} - saved on {readable}")
            found = True
        else:
            print(f" - Slot {i}: [empty]")

    if not found:
        print("No saves found yet.")

def delete_save_game(game, slot):
    slot = str(slot)
    
    if not slot.isdigit():
        print("Please use a numeric slot (e.g., 'delete 1').")
        return

    slot_num = int(slot)
    if slot_num < 1 or slot_num > 4:
        print("You can only delete save slots 1 to 4.")
        return

    filename = os.path.join(game.save_dir, f"save{slot_num}.json")
    
    if not os.path.exists(filename):
        print(f"No saved game in slot {slot_num}.")
        return

    # Confirm before deleting
    confirm = input(f"Are you sure you want to delete save slot {slot_num}? (y/n): ").strip().lower()
    if confirm != 'y':
        print("Delete operation cancelled.")
        return

    try:
        os.remove(filename)
        print(f"Save slot {slot_num} deleted.")
    except Exception as e:
        print(f"An error occurred while deleting the save: {e}")