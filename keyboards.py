from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

ABOUT_BUTTON = "About bot"
HELP_BUTTON = "Help"


def main_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [
        [KeyboardButton(text=ABOUT_BUTTON)],
        [KeyboardButton(text=HELP_BUTTON)]
    ]

    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True
    )
