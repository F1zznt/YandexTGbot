from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from db import session
from db.data import PhotoToTask
from handlers.subordinate.func import show_tools_for_add_file
from loader import dp
from states.subordinate import AddFileToTaskState


@dp.message_handler(content_types=['photo'], state=AddFileToTaskState.AddPhoto)
async def add_photo(msg: Message, state: FSMContext):
    data = await state.get_data()
    data['photo_id'] = data.get('photo_id', []) + [msg.photo[-1].file_id]
    await state.set_data(data)


@dp.message_handler(Text(equals=['Сохранить']), state=AddFileToTaskState.AddPhoto)
async def save_photo(msg: Message, state: FSMContext):
    data = await state.get_data()
    task_id = data['task_id']
    photos = data.get('photo_id', [])
    for photo_id in photos:
        photo = PhotoToTask(task_id=task_id,
                            photo_id=photo_id)
        session.add(photo)
    session.commit()
    await msg.answer('Фотографии добавлены')
    await show_tools_for_add_file(msg.from_user.id, state)