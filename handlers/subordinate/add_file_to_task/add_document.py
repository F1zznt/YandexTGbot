from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from db import session
from db.data.document_to_task import DocumentToTask
from handlers.subordinate.func import show_tools_for_add_file
from loader import dp
from states.subordinate import AddFileToTaskState


@dp.message_handler(content_types=['document'], state=AddFileToTaskState.AddDocument)
async def add_document(msg: Message, state: FSMContext):
    data = await state.get_data()
    data['document_id'] = data.get('document_id', []) + [msg.document.file_id]
    await state.set_data(data)


@dp.message_handler(Text(equals=['Сохранить']), state=AddFileToTaskState.AddDocument)
async def save_document(msg: Message, state: FSMContext):
    data = await state.get_data()
    task_id = data['task_id']
    documents = data.get('document_id', [])
    for document_id in documents:
        document = DocumentToTask(task_id=task_id,
                                  document_id=document_id)
        session.add(document)
    session.commit()
    await msg.answer('Документы добавлены')
    await show_tools_for_add_file(msg.from_user.id, state)
