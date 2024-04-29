from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from handlers.chief.func import show_chief_panel
from loader import dp
from states.chief import ChiefRoleState


@dp.message_handler(Text(equals=['Подчиненные']), state=ChiefRoleState.Start)
async def org_with_rob(msg: types.Message, state: FSMContext):
    await show_chief_panel(msg.from_user.id)


