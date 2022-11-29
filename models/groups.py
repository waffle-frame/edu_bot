from typing import Any
from loguru import logger
from datetime import datetime

from sqlalchemy import insert
from sqlalchemy.orm import scoped_session
from sqlalchemy_utils.types import ChoiceType
from sqlalchemy.exc import IntegrityError, DBAPIError
from sqlalchemy import Column, String, Integer, DateTime, VARCHAR

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

    id = Column(Integer, primary_key = True)
    created_at = Column(DateTime(timezone=True), default = datetime.utcnow)
    first_name = Column(VARCHAR(50), nullable = False)
    last_name = Column(VARCHAR(50), nullable = True)
    username = Column(VARCHAR(20), nullable = True)
    userbot = Column(String, nullable = False)
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
        except DBAPIError as e:
            logger.error("ROLLBACK: ", e)
            await db.rollback()
            raise False

        return True
