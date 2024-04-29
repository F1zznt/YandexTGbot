import sqlalchemy

from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class DocumentToTask(SqlAlchemyBase):
    __tablename__ = 'document_to_task'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    task_id = sqlalchemy.Column(sqlalchemy.ForeignKey('tasks.id'))
    document_id = sqlalchemy.Column(sqlalchemy.String)

    task = orm.relation('Tasks', back_populates='documents')