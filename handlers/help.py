from aiogram.dispatcher.filters.builtin import CommandHelp
from aiogram.types import Message

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(msg: Message):
    text = ("Список команд: ",
            "/start - Начать диалог",
            "/help - Получить справку"
            "/reset_role - обнулить роль")

    await msg.answer("\n".join(text))