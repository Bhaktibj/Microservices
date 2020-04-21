import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean,ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class Base(object):
    """Created Base class model """
    created_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        nullable=False
    )

    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
        nullable=False
    )


DeclarativeBase = declarative_base(cls=Base)


class Notes(DeclarativeBase):
    """ Notes class is used to create note information table in database"""
    __tablename__ = 'notes1'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    description = Column(String(50), nullable=True)
    color = Column(String(20), nullable=False)
    created_by = Column(String(30), nullable=False, default=None)
    is_archived = Column(Boolean, nullable=False, default=False)
    is_deleted = Column(Boolean, nullable=False, default=False)
    is_trashed = Column(Boolean, nullable=False, default=False)
    is_restored = Column(Boolean, nullable=False, default=False)
    is_pinned = Column(Boolean, nullable=False, default=False)
    label = Column(Integer, ForeignKey('labels.id'))

    def __init__(self, created_by, label_id, **kwargs):
        self.title = kwargs.get('title')
        self.description = kwargs.get('description')
        self.color = kwargs.get('color')
        self.is_trashed = kwargs.get('is_trashed')
        self.is_deleted = kwargs.get('is_deleted')
        self.is_archived = kwargs.get('is_archived')
        self.is_restored = kwargs.get('is_restored')
        self.is_pinned = kwargs.get('is_pinned')
        self.label = label_id
        self.created_by = created_by


class Labels(DeclarativeBase):
    __tablename__ = "labels"
    id = Column(Integer, primary_key=True)
    label = Column(String(50), nullable=False)

    def __init__(self, label):
        self.label = label


