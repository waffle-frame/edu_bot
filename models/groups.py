from datetime import datetime
from sqlalchemy import Column, Integer, String, \
                    DateTime, VARCHAR, ChoiceType

from settings.database import Base


class Group(Base):
    """
        This table contains the activities of managers. 
        During the creation of the group, the manager's data is saved.
    """
    __tablename__ = 'groups'

    OCCUPATION_TYPES = [
        ('group', 'Групповые')
        ('individual', 'Индивидуальные'),
    ]

    id = Column(Integer, primary_key = True)
    created_at = Column(DateTime(timezone=True), default = datetime.utcnow)
    first_name = Column(VARCHAR(50), nullable = False)
    last_name = Column(VARCHAR(50), nullable = True)
    username = Column(VARCHAR(20), nullable = True)
    userbot = Column(String, nullable = False)
    group_title = Column(VARCHAR(20), nullable = False)
    occupation_type = Column(ChoiceType(OCCUPATION_TYPES), nullable = False)

    def __init__(self, id, created_at, first_name, last_name, username, userbot, group_title, occupation_type):
        self.id = id
        self.created_at = created_at
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.userbot = userbot
        self.group_title = group_title
        self.occupation_type = occupation_type

    def __repr__(self):
        return f"Group(id={self.id!r}, occupation_type={self.occupation_type!r}, title={self.title!r})"
