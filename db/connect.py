from .data import db_session, Roles


def add_role():
    data_roles = {'none': 'Нету',
                  'chief': 'Начальник',
                  'subordinate': 'Подчиненный'}
    roles = session.query(Roles).all()
    if not roles:
        for tag, name in data_roles.items():
            role = Roles(tag=tag,
                         name=name)
            session.add(role)
        session.commit()


db_session.global_init("db/notice.db")
session = db_session.create_session()
add_role()
