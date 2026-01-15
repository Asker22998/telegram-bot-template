from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from bot.keyboards import main_keyboard

router = Router()


@router.message(Command("start"))
async def start_handler(message: Message) -> None:
    await message.answer(
        "Hello!\n\n"
        "This is a lightweight Telegram bot template.\n"
        "Use /help to see available commands.",
        reply_markup=main_keyboard()
    )


@router.message(Command("help"))
async def help_handler(message: Message) -> None:
    await message.answer(
        "Available commands:\n"
        "/start — start the bot\n"
        "/help — show this help message\n\n"
        "Buttons below are an example of the control panel."
    )


@router.message()
async def unknown_message_handler(message: Message) -> None:
    await message.answer(
        "I don't understand this command.\n"
        "Please use /help."
    )
