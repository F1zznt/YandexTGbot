from datetime import datetime

import sqlalchemy

from .db_session import SqlAlchemyBase
from sqlalchemy import orm

class Users(SqlAlchemyBase):
    __tablename__ = 'users'

    user_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    user_name = sqlalchemy.Column(sqlalchemy.String)
    name = sqlalchemy.Column(sqlalchemy.String)
    role_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('roles.id'))
    chief_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.user_id'))
    modifited_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now())

    role = orm.relation('Roles')
    subordinates = orm.relation('Users', backref=orm.backref('chief', remote_side=[user_id]))
    tasks = orm.relation('Tasks', primaryjoin='Tasks.user_id==Users.user_id')

    def __repr__(self):
        return '{\n' + f'id: {self.user_id}, user_name: {self.user_name}, role: {self.role}' + '}'