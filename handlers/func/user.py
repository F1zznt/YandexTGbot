from keyboards.default.chief import panel_chief
from keyboards.default.subordinate import panel_subordinate
from loader import bot

from db import session
from db.data import Users
from keyboards.default import panel_no_role
from states import NoRoleState, ChiefRoleState, SubordinateRoleState


def register_user(user_id, user_name, name):
    user = Users(user_id=user_id,
                 user_name=user_name,
                 name=name,
                 role_id=1)
    session.add(user)
    session.commit()


async def get_user_panel(user_id):
    user = session.query(Users).get(user_id)
    if not user:
        return
    tag = user.role.tag
    panel = panel_no_role
    await NoRoleState.Start.set()
    if tag == 'chief':
        panel = panel_chief
        await ChiefRoleState.Start.set()
    elif tag == 'subordinate':
        panel = panel_subordinate
        await SubordinateRoleState.Start.set()
    return panel


async def show_panel_role(user_id, text=''):
    panel = await get_user_panel(user_id)
    await bot.send_message(chat_id=user_id,
                           text=text,
                           reply_markup=panel
                           )
