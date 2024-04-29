from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, CallbackQuery

from db import session
from db.data import Tasks
from keyboards.default import panel_exit
from keyboards.default.subordinate.func import show_tools_with_task
from keyboards.inline.callback_data import task
from keyboards.inline.chief import inline_show_file_to_task
from keyboards.inline.subordinate import inline_new_task, inline_progress_task
from loader import dp, bot
from states.subordinate import SubordinateRoleState


@dp.message_handler(Text(equals=['Новые']), state=SubordinateRoleState.TaskTools)
async def show_new_task(msg: Message, state: FSMContext):
    user_id = msg.from_user.id
    tasks = session.query(Tasks).filter(Tasks.user_id == user_id, Tasks.progress == 'todo').all()
    await msg.answer(text=f'Кличество: {len(tasks)}',
                     reply_markup=panel_exit)
    for task in tasks:
        panel = inline_new_task(task.id)
        await msg.answer(text=f'Содержание: {task.title}',
                         reply_markup=panel)
    await SubordinateRoleState.NewTask.set()


@dp.callback_query_handler(task.filter(type='todo', attribute='start'), state="*")
async def start_new_task(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.message.delete()
    task_id = callback_data['info']
    task = session.query(Tasks).get(task_id)
    task.progress = 'in_progress'
    chief_id = task.user.chief.user_id
    await bot.send_message(chat_id=chief_id, text=f'{call.from_user.full_name} \n'
                                                  f'Начал выполнять задание: {task.title}')
    session.commit()


@dp.message_handler(Text(equals=['В процессе']), state=SubordinateRoleState.TaskTools)
async def show_progress_task(msg: Message, state: FSMContext):
    user_id = msg.from_user.id
    tasks = session.query(Tasks).filter(Tasks.user_id == user_id,
                                        Tasks.progress == 'in_progress').all()
    await msg.answer(text=f'Кличество: {len(tasks)}',
                     reply_markup=panel_exit)
    for i, task in enumerate(tasks):
        panel = inline_progress_task(task.id)
        await msg.answer(text=f'Номер: {i + 1}\n'
                              f'Название: {task.title}',
                         reply_markup=panel)
    await SubordinateRoleState.ProgressTask.set()


@dp.callback_query_handler(task.filter(type='in_progress', attribute='voices'),
                           state=SubordinateRoleState.ProgressTask)
async def send_voice(call: CallbackQuery, callback_data: dict, state: FSMContext):
    task_id = callback_data['info']
    task = session.query(Tasks).get(task_id)
    voices = task.chief_voices
    for voice in voices:
        await call.message.answer_voice(voice=voice.voice_id)


@dp.callback_query_handler(task.filter(type='done'), state='*')
async def done_task(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.message.delete()
    task_id = callback_data['info']
    task = session.query(Tasks).get(task_id)
    task.progress = 'done'
    session.commit()
    user = task.user
    chief_id = user.chief.user_id
    await bot.send_message(chat_id=chief_id,
                           text=f'Подчиненный: {user.name} выполнил задание\n'
                                f'Название: {task.title}',
                           reply_markup=inline_show_file_to_task(task_id))


@dp.message_handler(Text(equals=['Назад']),
                    state=[SubordinateRoleState.NewTask, SubordinateRoleState.ProgressTask])
async def exit_tools_task(msg: Message, state: FSMContext):
    await show_tools_with_task(msg.from_user.id)
