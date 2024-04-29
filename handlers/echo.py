from aiogram.dispatcher.filters import Text
from aiogram.types import CallbackQuery

from handlers.func.user import show_panel_role
from keyboards.inline.callback_data import exit_calldata
from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext


@dp.message_handler(Text(equals=['Назад', 'В главное меню']), state='*')
async def back(msg: types.Message, state: FSMContext):
    await show_panel_role(msg.from_user.id, 'Возвращение')


@dp.message_handler(state='*')
async def bot_echo(msg: types.Message, state: FSMContext):
    await show_panel_role(msg.from_user.id, 'Произошла ошибка')
    await state.reset_data()


@dp.callback_query_handler(exit_calldata.filter(type='panel'), state='*')
async def exit_from_call_panel(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await show_panel_role(call.from_user.id, 'Возвращение')


@dp.callback_query_handler(state='*')
async def exit_from_call(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await show_panel_role(call.from_user.id, 'Произошла ошибка')
