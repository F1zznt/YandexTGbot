from aiogram.types import Message

from data.config import ADMINS


def is_admin(msg: Message):
    return msg.from_user.id in ADMINS