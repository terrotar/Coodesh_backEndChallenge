from sqlalchemy import ARRAY, Boolean, Column, Date, Integer, String, DateTime
# from sqlalchemy.orm import relationship

from sqlalchemy.dialects.postgresql import JSON

from .database import Base


class Article(Base):
    __tablename__ = 'Articles'

    id = Column('ID', Integer, primary_key=True, index=True)
    featured = Column('Featured', Boolean, default=False)
    title = Column('Title', String, unique=True, index=True)
    url = Column('Url', String)
    imageUrl = Column('ImageUrl', String)
    newsSite = Column('NewsSite', String, default='')
    summary = Column('Summary', String, default='')
    publishedAt = Column('PublishedAt', DateTime)
    launches = Column('Launches', JSON, default='')
    events = Column('Events', JSON, default='')
    # events = Column('Events', ARRAY(String), default='')

    def __init__(self, featured, title, url, imageUrl, newsSite, summary, publishedAt, launches, events):
        self.title = title
        self.featured = featured
        self.url = url
        self.imageUrl = imageUrl
        self.newsSite = newsSite
        self.summary = summary
        self.publishedAt = publishedAt
        self.launches = launches
        self.events = events
