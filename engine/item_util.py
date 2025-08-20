def match_room_item(game, item):
    matched_item = None

    # First: exact match in current room
    if item.get("name") in game.current_room.items_data:
        matched_item = item
    #else:
    #    # Fallback: partial match in room items
    #    for real_name in self.current_room.items:
    #        if item in real_name:
    #            matched_item = real_name
    #            break

    return matched_item

def show_inventory(game):
    if game.inventory:
        print("You have:")
        for item in game.inventory:
            print(f" - {item}")
    else:
        print("You have nothing in your inventory.")

def normalize_item(item):
    return item.lower()

def look_through_aliases(data, term):
    for item_name, item_info in data.items():
        for alias in item_info.get("aliases", []):
            if term == alias.lower():
                return item_name
            
def resolve_alias(game, term):
    term = term.lower()

    if term in game.inventory:
        return {"name": term, "source": "inventory"}
    if term in game.current_room.items_data:
        return {"name": term, "source": "room"}

    match = look_through_aliases(game.inventory, term)
    if match:
        return {"name": match, "source": "inventory"}

    match = look_through_aliases(game.current_room.items_data, term)
    if match:
        return {"name": match, "source": "room"}

    return None

def describe_room_item(game, item_name):
    return game.current_room.items_data.get(item_name, {}).get("description", f"There is no {item_name} to examine.")

def describe_inventory_item(game, item_name):
    return game.inventory.get(item_name, {}).get("description", f"You don’t seem to have a {item_name}.")

