from datetime import datetime

import sqlalchemy

from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class Tasks(SqlAlchemyBase):
    __tablename__ = 'tasks'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.ForeignKey('users.user_id'))
    title = sqlalchemy.Column(sqlalchemy.String)
    progress = sqlalchemy.Column(sqlalchemy.String, default='todo')
    date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now())

    user = orm.relation('Users', back_populates='tasks')
    chief_voices = orm.relation('ChiefVoiceToTask', primaryjoin='Tasks.id==ChiefVoiceToTask.task_id')
    voices = orm.relation('VoiceToTask', primaryjoin='Tasks.id==VoiceToTask.task_id')
    photos = orm.relation('PhotoToTask', primaryjoin='Tasks.id==PhotoToTask.task_id')
    documents = orm.relation('DocumentToTask', primaryjoin='Tasks.id==DocumentToTask.task_id')
