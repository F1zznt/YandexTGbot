from aiogram import types
from aiogram.dispatcher.filters import Text

from db import session
from db.data import Users, Roles
from keyboards.default import panel_choose_role
from loader import dp
from states import NoRoleState, ChooseRoleState


@dp.message_handler(Text(equals=['Выбрать роль']), state=NoRoleState.Start)
async def roles(msg: types.Message):
    await msg.answer(text='Роли',
                     reply_markup=panel_choose_role)
    await ChooseRoleState.Start.set()


@dp.message_handler(Text(equals=['Начальник']), state=ChooseRoleState.Start)
async def role_chief(msg: types.Message):
    user = session.query(Users).get(msg.from_user.id)
    user.role_id = session.query(Roles).filter(Roles.tag == 'chief').first().id
    session.commit()
    await msg.answer('Напишите команду /start')


@dp.message_handler(Text(equals=['Подчиненный']), state=ChooseRoleState.Start)
async def role_subordinate(msg: types.Message):
    user = session.query(Users).get(msg.from_user.id)
    user.role_id = session.query(Roles).filter(Roles.tag == 'subordinate').first().id
    session.commit()
    await msg.answer('Напишите команду /start')