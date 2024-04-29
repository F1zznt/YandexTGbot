from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from keyboards.default.subordinate.func import show_tools_with_task
from loader import dp
from states.subordinate import SubordinateRoleState


@dp.message_handler(Text(equals=['Задачи']), state=SubordinateRoleState.Start)
async def show_task(msg: Message, state: FSMContext):
    await show_tools_with_task(msg.from_user.id)


@dp.message_handler(Text(equals=['Узнать свой код']), state=SubordinateRoleState.Start)
async def print_rob_id(msg: Message):
    await msg.answer(text='Ваш код: \n'
                          f'{msg.from_user.id}')
