from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from db import session
from db.data import Tasks
from keyboards.inline.callback_data import task
from loader import dp


@dp.callback_query_handler(task.filter(type='task_file', attribute='documents'), state='*')
async def show_document(call: CallbackQuery, callback_data: dict, state: FSMContext):
    task_id = callback_data['info']
    task = session.query(Tasks).get(task_id)
    documents = task.documents
    for document in documents:
        await call.message.answer_document(document=document.document_id)