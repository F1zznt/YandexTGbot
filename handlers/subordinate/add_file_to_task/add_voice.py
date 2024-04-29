from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from db import session
from db.data import VoiceToTask
from handlers.subordinate.func import show_tools_for_add_file
from loader import dp
from states.subordinate import AddFileToTaskState, SubordinateRoleState


@dp.message_handler(content_types=['voice'], state=AddFileToTaskState.AddVoice)
async def add_voice(msg: Message, state: FSMContext):
    data = await state.get_data()
    data['voice_id'] = data.get('voice_id', []) + [msg.voice.file_id]
    await state.set_data(data)


@dp.message_handler(Text(equals=['Сохранить']), state=AddFileToTaskState.AddVoice)
async def save_voice(msg: Message, state: FSMContext):
    data = await state.get_data()
    task_id = data['task_id']
    voices = data.get('voice_id', [])
    for voice_id in voices:
        voice = VoiceToTask(task_id=task_id,
                            voice_id=voice_id)
        session.add(voice)
    session.commit()
    await msg.answer('Аудиосообщения добавлены')
    await show_tools_for_add_file(msg.from_user.id, state)