from typing import Any
from loguru import logger
from datetime import datetime

from sqlalchemy.orm import scoped_session
from sqlalchemy import insert, select, desc
from sqlalchemy_utils.types import ChoiceType
from sqlalchemy.exc import IntegrityError, DBAPIError
from sqlalchemy import Column, String, Integer, DateTime, VARCHAR, BigInteger

from models import Base


class Group(Base):
    """
        This table contains the activities of managers. 
        During the creation of the group, the manager"s data is saved.
    """
    __tablename__ = "groups"

    OCCUPATION_TYPES = [
        ("Групповые", "Групповые"),
        ("Индивидуальные", "Индивидуальные"),
    ]

    id = Column(BigInteger, primary_key = True)
    created_at = Column(DateTime(timezone=True), default = datetime.utcnow)
    user_id = Column(BigInteger, nullable = False)
    group_id = Column(BigInteger, nullable = False)
    first_name = Column(VARCHAR(50), nullable = False)
    last_name = Column(VARCHAR(50), nullable = True)
    username = Column(VARCHAR(20), nullable = True)
    userbot = Column(String, nullable = False)
    link = Column(String, nullable = False)
    group_title = Column(VARCHAR(20), nullable = False)
    occupation_type = Column(ChoiceType(OCCUPATION_TYPES), nullable = False)

    @classmethod
    async def create(self, db: scoped_session, **kwargs: Any) -> bool:
        try:
            query = insert(self).values(**kwargs)
            await db.execute(query)
            await db.commit()
        except IntegrityError as e:
            logger.error(e)
            return False
        except Exception as e:
            logger.error("ROLLBACK: ", e, kwargs)
            await db.rollback()
            return False

        return True

    @classmethod
    async def select_history_tail(self, db: scoped_session, **kwargs: Any):
        limit = 10
        if kwargs.get('limit', None):
            limit = kwargs.get('limit')

        query = select(
            self.group_title, self.link, self.occupation_type, self.created_at, self.username 
        ).order_by(desc(self.created_at)
        ).limit(limit)

        data = await db.execute(query)
        await db.commit()

        return data.fetchall()

    @classmethod
    async def get_user_groups_by_id(self, db: scoped_session, user_id: int):
        query = select(self.group_id).where(self.user_id == user_id)

        data = await db.execute(query)
        await db.commit()

        return data.fetchall()

    @classmethod
    async def search(self, db: scoped_session, title: str, limit: int):
        users_query = "SELECT max(user_id), max(first_name) || ' ' || max(last_name), '@'||max(username), count(*) " + \
                f"FROM groups WHERE lower(first_name) ILIKE lower('%{title}%') or lower(last_name) ILIKE lower('%{title}%') or lower(username) ILIKE lower('%{title}%') " + \
                "GROUP BY user_id;"
        groups_query = "SELECT group_id, group_title, '('||SUBSTRING(occupation_type, 0, 6)||'.)', link, '@'||username, TO_CHAR(created_at, 'dd.mm.yyyy') FROM groups " + \
                f"WHERE lower(username) ILIKE lower('%{title}%') or lower(link) ILIKE lower('%{title}%') or lower(occupation_type) ILIKE lower('%{title}%') or lower(group_title) ILIKE lower('%{title}%') ORDER BY created_at asc LIMIT {limit}"

        users = await db.execute(users_query)
        groups = await db.execute(groups_query)
        await db.commit()

        data = {}
        data['Пользователь'] = [ i for i in users.all() ]
        data['Группа'] = [ j for j in groups.all()]

        return data
