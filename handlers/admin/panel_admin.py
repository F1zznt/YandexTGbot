from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from handlers.admin.func import is_admin
from keyboards.default.admin import panel_admin
from loader import dp
from states.admin import AdminState


@dp.message_handler(is_admin, commands=['admin_panel'], state='*')
async def admin_panel(msg: Message, state: FSMContext):
    await msg.answer(text='Админ панель', reply_markup=panel_admin)
    await AdminState.Start.set()
