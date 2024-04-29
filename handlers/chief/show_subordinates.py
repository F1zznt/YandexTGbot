from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from db import session
from db.data import Users
from handlers.chief.func import show_chief_panel
from keyboards.inline import inline_exit
from keyboards.inline.callback_data import tools, exit_calldata
from loader import dp, bot
from states.chief import ShowSubordinatesState


@dp.callback_query_handler(tools.filter(role='chief', type='add_subordinate'),
                           state=ShowSubordinatesState.Start)
async def add_subordinate(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(text='Введите код подчиненного\n'
                                   'Он может получить его из своего профиля',
                              reply_markup=inline_exit('add_subordinate'))
    await ShowSubordinatesState.EditCod.set()


@dp.message_handler(content_types=['text'], state=ShowSubordinatesState.EditCod)
async def edit_subordinate_id(msg: types.Message, state: FSMContext):
    user_id = msg.text
    error = incorrect_user_id(user_id)
    if error:
        await msg.answer(text=f'Ошибка: {error}', reply_markup=inline_exit('add_subordinate'))
        return
    user_id = int(user_id)
    user = session.query(Users).get(user_id)
    user.chief_id = msg.from_user.id
    session.commit()
    await msg.answer(text='Подчиненный добавлен')
    await bot.send_message(chat_id=user_id, text=f'У вас новый начальник: {msg.from_user.full_name}')
    await ShowSubordinatesState.Start.set()
    await show_chief_panel(msg.from_user.id)


@dp.callback_query_handler(exit_calldata.filter(type='add_subordinate'), state='*')
async def exit_from_call(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await ShowSubordinatesState.Start.set()
    await show_chief_panel(call.from_user.id)


def incorrect_user_id(text):
    if not text.isdigit():
        return 'Должны быть цифры'
    id = int(text)
    user = session.query(Users).get(id)
    if not user:
        return 'Такого пользователя нет'
    if user.role.tag == 'chief':
        return 'Пользователь является Начальником'
    if user.chief_id:
        return 'Пользователь уже привязан к Начальнику'
