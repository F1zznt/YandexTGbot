import sqlalchemy

from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class PhotoToTask(SqlAlchemyBase):
    __tablename__ = 'photo_to_task'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    task_id = sqlalchemy.Column(sqlalchemy.ForeignKey('tasks.id'))
    photo_id = sqlalchemy.Column(sqlalchemy.String)

    task = orm.relation('Tasks', back_populates='photos')