from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from bot.keyboards import main_keyboard, ABOUT_BUTTON, HELP_BUTTON

router = Router()


@router.message(Command("start"))
async def start_handler(message: Message) -> None:
    await message.answer(
        "Hello!\n\n"
        "This is a lightweight Telegram bot template.",
        reply_markup=main_keyboard()
    )


@router.message(Command("help"))
async def help_handler(message: Message) -> None:
    await message.answer(
        "Available commands:\n"
        "/start — start the bot\n"
        "/help — show help"
    )


@router.message(lambda message: message.text == ABOUT_BUTTON)
async def about_button_handler(message: Message) -> None:
    await message.answer(
        "This bot is an open-source Telegram bot template.\n"
        "You can use it as a base for your own projects."
    )


@router.message(lambda message: message.text == HELP_BUTTON)
async def help_button_handler(message: Message) -> None:
    await help_handler(message)


@router.message()
async def unknown_message_handler(message: Message) -> None:
    await message.answer(
        "Unknown command.\n"
        "Use /help or buttons below."
    )

