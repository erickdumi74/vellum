class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items_data = {}          # items in the room: name -> description
        self.exits = {}          # passage name -> Room object
        self.aliases = {}


def describe_study_intro():
    return (
        "A cozy space warmed by the flickering fireplace, where shadows dance softly on the wooden floorboards. "
        "A rusty firepoker lies on the floor close to the fire. "
        "The worn leather couch looks inviting but carries the faint scent of old smoke. "
        "A faded wooden door leans to the right of the fireplace, its frame weathered from age. "
        "Nearby, a desk holds a half-melted candle and a small, cracked teacup. "
        "A dusty globe spins lazily on the bookshelf beside an old encyclopedia set that looks worn but oddly out of place. "
        "A faded portrait hangs crookedly on the wall, its subject's eyes seeming to follow you. "
        "On the wall, you notice a strange eye symbol, its gaze piercing beyond the visible, watching even when you're not looking."
    )

def setup_rooms():
    # --- Room Creation ---

    # Study
    study = Room("Study", describe_study_intro())
    study.items_data = {
        "fireplace": {"description": "The fireplace crackles softly, ashes glowing faintly.", "aliases": ["flickering fireplace"]},
        "firepoker": {"description": "A rusty firepoker that hasn't been used in a long time.", "aliases": ["poker", "fire poker", "rusty firepoker"]},
        "floorboards": {"description": "The boards bend ever so slightly, sighing with each footstep.", "aliases": ["wooden floorboards"]},
        "desk": {"description": "An old wooden desk with a half-melted candle on top and a drawer in the middle.", "aliases": ["wooden desk", "old desk", "old wooden desk"]},
        "candle": {"description": "The candle's wax is half-melted, its flame flickering gently.", "aliases": ["half-melted candle", "melted candle"]},
        "teacup": {"description": "A small, cracked teacup that looks like it hasn't been used in years.", "aliases": ["cracked teacup", "small teacup", "small cracked teacup"]},
        "portrait": {"description": "A faded portrait of a stern-looking man. His eyes seem to follow you.", "aliases": ["faded portrait"]},
        "encyclopedia": {"description": "A peculiar encyclopedia set that looks worn but oddly out of place.", "aliases": ["old encyclopedia set", "encyclopedia set", "old encyclopedia"]},
        "couch" : {"description": "The worn leather couch looks inviting but carries the faint scent of old smoke.",  "aliases": ["worn leather couch", "worn couch", "leather couch"]},
        "globe" : {"description": "A dusty globe spins ever so slowly, its axis creaking like old bone.", "aliases": ["dusty globe"]},
        "bookshelf": {"description": "A bookshelf full of encyclopedias."},
        "ashes": {"description": "A pile of ashes."},
        "drawer": {"description": "Its tightly locked."},
        "wooden door": {"description": "A faded wooden door leaning slightly to the right of the fireplace."},
        "eye symbol": {"description": "A strange eye, its gaze piercing beyond the visible. It seems to watch, even when you're not looking.", "aliases": ["strange eye symbol"]},
        "fire": {"description": "The flames flicker and twist, casting shadows that dance along the walls. It offers warmth… and perhaps a warning."},
        "eyes": {"description": "You lean closer to examine the portraits eyes. They don't follow you, but more like anticipate you."},
    }

    # --- Hallway ---
    def describe_hallway_intro():
        return (
            "A narrow hallway dimly lit by a wall lamp that flickers intermittently. "
            "The wooden door stands open behind you, leading back to the Study. "
            "An imposing iron door looms ahead, clearly sealed and handleless. "
            "Cold steel, faintly scratched, as if someone once tried — and failed — to force it open. "
            "A small keypad glows dimly beside it, its purpose unclear. "
            "Beneath the lamp, a worn brass plaque is mounted on the wall, scratched and partially unreadable. "
            "What's left of the inscription reads: 'Those who seek beyond must hear what cannot be spo…' "
            "The rest is marred by deep, deliberate gouges. "
            "Above, an old intercom speaker is mounted near the ceiling, its surface dusted with age. "
            "Just beneath the plaque, a faint symbol is scratched into the wall: an intertwined 'V' and 'I'. "
            "A low, persistent humming vibrates through the air. "
            "You also spot a dormant terminal mounted on the wall. "
            "Along one side of the wall, a rusted metal steam pipe runs, faintly hissing as vapor leaks out steadily."
        )

    hallway = Room("Hallway", describe_hallway_intro())

    hallway.items_data = {
        "keypad": {"description": "A keypad to enter characters and numbers.", "aliases": []},
        "plaque": {"description": "The brass plaque is scratched and aged. What's left of the inscription reads:\n"
                                "'Those who seek beyond must hear what cannot be spo…'\n"
                                "The rest is marred by deep gouges.", "aliases": []},
        "intercom": {"description": "An old intercom speaker. Faint static can be heard if you listen closely.", "aliases": []},
        "symbol": {"description": "A faint, scratched symbol resembling an intertwined 'V' and 'I'.", "aliases": []},
        "iron door": {"description": "A sealed, handleless iron door. Cold steel faintly scratched.", "aliases": []},
        "wooden door": {"description": "A faded wooden door, slightly ajar, frame worn from age.", "aliases": []},
        "terminal": {"description": "A dormant terminal, screen dark, with a shallow slot beside it.", "aliases": []},
        "hourglass symbol": {"description": "An hourglass, frozen in time, its sands stuck.", "aliases": []},
        "pipe": {"description": "A rusted pipe hisses faintly as vapor leaks out.", "aliases": []},
        "twisted symbol": {"description": "A warped, contorted shape. Its meaning unclear.", "aliases": []},
        "lamp": {"description": "A wall lamp flickers faintly, casting uneven shadows.", "aliases": []},
    }

    # --- Secret Chamber ---
    def describe_secret_chamber_intro():
        return (
            "You are in a dim chamber carved from ancient stone. "
            "The walls pulse with violet glyphs — unreadable, yet oddly familiar. "
            "At the center, a black plinth cradles a cracked mirror, its surface shifting faintly. "
            "Several candles line the edges of the chamber, flames flickering erratically. "
            "An arcane diagram is etched into the walls, intertwined with intricate shapes. "
            "Nearby, an ancient book rests on a pedestal, its pages yellowed and cracked. "
            "The air feels thick with the weight of knowledge. "
            "Shadows cling to the edges of the room, recoiling from your presence. "
            "Two exits disturb the stone: the iron door you entered through, and the lab door beyond."
        )

    secret_chamber = Room("Secret Chamber", describe_secret_chamber_intro())

    secret_chamber.items_data = {
        "glyphs": {"description": "Violet glyphs pulse faintly, shifting as if alive.", "aliases": []},
        "candles": {"description": "Candles flicker weakly, casting jittery shadows.", "aliases": []},
        "plinth": {"description": "A smooth obsidian plinth. Its surface ripples faintly.", "aliases": []},
        "mirror": {"description": "An ancient cracked mirror, humming faintly.", "aliases": []},
        "symbols": {"description": "Ancient wall symbols, one resembles 'V' over an inverted triangle.", "aliases": []},
        "spiral symbol": {"description": "A spiral twisting inward endlessly.", "aliases": []},
        "fractured symbol": {"description": "A symbol cracked into pieces but still whole.", "aliases": []},
        "book": {"description": "An ancient book, its text mostly unreadable.", "aliases": []},
        "diagram": {"description": "An arcane diagram partially obscured by age.", "aliases": []},
        "lanterns": {"description": "Candles/lanterns line the edges, flames erratic.", "aliases": []},
    }

    # --- Lab ---
    def describe_lab_intro():
        return (
            "You find yourself in a dimly lit laboratory, cold metal surfaces gleaming under flickering lights. "
            "The air carries a faint scent of chemicals and ozone. "
            "In the center stands a strange prism with a small receptacle beside it, glowing faintly. "
            "Towering machines line the walls, silent but imposing. "
            "A sealed glass chamber sits nearby, its interior faintly smudged. "
            "A rusted distiller hisses softly, its pipes casting serpentine shadows. "
            "A dusty clock ticks faintly, its hands frozen. "
            "On the wall, a candle symbol marks the struggle against the dark. "
            "A combination lock rests silently in the corner. "
            "The lab door, seamless and cold, stands silent."
        )

    lab = Room("Lab", describe_lab_intro())

    lab.items_data = {
        "prism": {"description": "A glowing prism refracts light into shifting patterns.", "aliases": []},
        "machinery": {"description": "Towering machines line the walls, silent but intimidating.", "aliases": []},
        "chamber": {"description": "A sealed glass chamber — empty, yet unsettling.", "aliases": []},
        "lab door": {"description": "A seamless, cold alloy door with no handle.", "aliases": []},
        "candle symbol": {"description": "A candle symbol fights against the dark.", "aliases": []},
        "clock": {"description": "A dusty clock, hands frozen in time.", "aliases": []},
        "light": {"description": "A dim, flickering light sways above.", "aliases": []},
        "distiller": {"description": "A rusted distiller hisses softly.", "aliases": []},
        "right mirror": {"description": "A dim mirror, almost waiting for purpose.", "aliases": []},
        "center mirror": {"description": "A dim mirror, almost waiting for purpose.", "aliases": []},
        "left mirror": {"description": "A dim mirror, almost waiting for purpose.", "aliases": []},
        "combination lock": {"description": "A lock waiting for the correct sequence.", "aliases": []},
        "instruments": {"description": "Archaic devices: tubes, coils, fittings clamped to the floor.", "aliases": []},
    }


    # --- Link Rooms ---
    study.exits["wooden door"] = hallway
    hallway.exits["wooden door"] = study
    hallway.exits["iron door"] = secret_chamber
    secret_chamber.exits["iron door"] = hallway
    secret_chamber.exits["lab door"] = lab
    lab.exits["lab door"] = secret_chamber

    # --- Store in dictionary ---
    return {
        "Study": study,
        "Hallway": hallway,
        "Secret Chamber": secret_chamber,
        "Lab": lab,
    }