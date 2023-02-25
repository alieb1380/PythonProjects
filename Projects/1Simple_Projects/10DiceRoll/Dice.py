import random


DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}

DICE_HEIGHT = len(DICE_ART[1])
DICE_WIDTH = len(DICE_ART[1][0])
DICE_FACE_SEPARATOR = " "

def parse_input(input_string):
    if input_string.strip() in {"1", "2", "3", "4", "5", "6"}:
        return int(input_string)
    else:
        print("Please WEnter a number from 1 to 6!!")
        '''# The raise keyword is used to raise an exception.
        You can define what kind of error to raise, and the text to print to the user.'''
        raise SystemExit(1)
    
    
def roll_dice(num_dice):
    roll_results = []
    for _ in range(num_dice):
        roll = random.randint(1, 6)
        roll_results.append(roll)
    return roll_results


def generate_dice_faces_diagram(dice_values):
    """Return an ASCII diagram of dice faces from `dice_values`.
    The string returned contains an ASCII representation of each die.
    For example, if `dice_values = [4, 1, 3, 2]` then the string
    returned looks like this:
    ~~~~~~~~~~~~~~~~~~~ RESULTS ~~~~~~~~~~~~~~~~~~~
    ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
    │  ●   ●  │ │         │ │  ●      │ │  ●      │
    │         │ │    ●    │ │    ●    │ │         │
    │  ●   ●  │ │         │ │      ●  │ │      ●  │
    └─────────┘ └─────────┘ └─────────┘ └─────────┘
    """
    dice_faces = _get_dice_faces(dice_values)
    dice_faces_rows = _generate_dice_faces_rows(dice_faces)
    
    # generate header with the word "RESULTS" centerd
    width = len(dice_faces_rows[0])
    diagram_header = " RESULTS ".center(width, "~")
    
    dice_faces_diagram = '\n'.join([diagram_header] + dice_faces_rows)
    return dice_faces_diagram

def _get_dice_faces(dice_values):
    dice_faces = []
    for value in dice_values:
        dice_faces.append(DICE_ART[value])
    return dice_faces

def _generate_dice_faces_rows(dice_faces):
    dice_faces_rows = []
    for row_idx in range(DICE_HEIGHT):
        row_components = []
        for dice in dice_faces:
            row_components.append(dice[row_idx])
        row_string = DICE_FACE_SEPARATOR.join(row_components)
        dice_faces_rows.append(row_string)
    return dice_faces_rows


num_dice_input = input("HOW MANY DICE DO YOU WANT TO ROLL? [1-6]")
num_dice = parse_input(num_dice_input)

roll_results = roll_dice(num_dice)

dice_face_diagram = generate_dice_faces_diagram(roll_results)

print(f"\n{dice_face_diagram}")