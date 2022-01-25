from sqlalchemy import ARRAY, Boolean, Column, Date, Integer, String
# from sqlalchemy.orm import relationship

from .database import Base


class Article(Base):
    __tablename__ = 'Articles'

    id = Column('ID', Integer, primary_key=True, index=True)
    featured = Column('Featured', Boolean, default=False)
    title = Column('Title', String(200), unique=True, index=True)
    url = Column('Url', String(200), unique=True)
    imageUrl = Column('ImageUrl', String(200))
    newSite = Column('NewSite', String(200))
    summary = Column('Summary', String(500))
    publishedAt = Column('PublishedAt', Date)
    launches = Column('Launches', ARRAY(Integer))

    def __init__(self, featured, title, url, imageUrl, newSite, summary, publishedAt, launches):
        self.title = title
        self.featured = featured
        self.url = url
        self.imageUrl = imageUrl
        self.newSite = newSite
        self.summary = summary
        self.publishedAt = publishedAt
        self.launches = launches
