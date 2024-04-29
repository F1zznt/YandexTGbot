from aiogram.dispatcher import FSMContext

from keyboards.default.subordinate import panel_tools_add_file
from loader import bot
from states.subordinate import SubordinateRoleState


async def show_chief_panel(user_id):
    pass


async def show_tools_for_add_file(user_id, state: FSMContext):
    msg = await bot.send_message(chat_id=user_id,
                                 text='Инструменты',
                                 reply_markup=panel_tools_add_file)
    data = await state.get_data()
    msg_id = data.get('msg_id_tools_add_file')
    if msg_id:
        await bot.delete_message(chat_id=user_id, message_id=msg_id)
    await state.update_data({'msg_id_tools_add_file': msg.message_id})
    await SubordinateRoleState.ChooseTypeAddFile.set()
