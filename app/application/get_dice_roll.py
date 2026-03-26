import random


def get_dice_roll() -> int:
    dice_number = random.randint(1, 6)  # noqa: S311
    return dice_number + 2
