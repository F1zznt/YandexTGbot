from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from db import session
from db.data import Users, Roles
from loader import dp, bot
from states.chief import ChiefRoleState
from states.subordinate import SubordinateRoleState


@dp.message_handler(commands=['reset_role'],
                    state=[ChiefRoleState.Start, SubordinateRoleState.Start])
async def reset_role(msg: Message, state: FSMContext):
    user = session.query(Users).get(msg.from_user.id)
    not_role = session.query(Roles).filter(Roles.tag == 'none').first()
    user.role_id = not_role.id
    user.chief_id = None
    for sub in user.subordinates:
        sub.chief_id = None
        await bot.send_message(chat_id=sub.user_id, text='У вас больше нет Начальника')
    session.commit()
    await msg.answer(text='Напишите команду /start')
