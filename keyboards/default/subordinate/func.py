from keyboards.default.subordinate import panel_tools_with_task
from loader import bot
from states.subordinate import SubordinateRoleState


async def show_tools_with_task(user_id):
    await bot.send_message(chat_id=user_id, text='Инструменты',
                           reply_markup=panel_tools_with_task)
    await SubordinateRoleState.TaskTools.set()
