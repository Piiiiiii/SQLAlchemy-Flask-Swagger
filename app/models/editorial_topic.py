from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.models.base import Base, db
from app.models.campaign import Campaign

# If a table exists, create_all will not update the changed table. So you should delete this table first.

editorial_topic_tag = db.Table('editorial_topic_tag',
              Column('editorial_topic_id', Integer, ForeignKey('editorial_topic.editorial_topic_id')),
              Column('tag_index', Integer, ForeignKey('tag.index')),
              )

editorial_topic_article = db.Table('editorial_topic_article',
              Column('editorial_topic_id', Integer, ForeignKey('editorial_topic.editorial_topic_id')),
              Column('article_id', Integer, ForeignKey('article.article_id')),
              )


# user is a keyword for pqsql
class Editorial_topic(Base):
    __tablename__ = 'editorial_topic'
    index = Column(Integer, primary_key=True, autoincrement=True)
    # TODO: list campaign table schema here
    editorial_topic_id = Column(Integer, unique=True)
    editorial_topic_name = Column(String)
    editorial_topic_description = Column(String)
    tags = db.relationship('Tag', secondary=editorial_topic_tag, backref=db.backref('editorial_topics', lazy='dynamic'))
    articles = db.relationship('Article', secondary=editorial_topic_article, backref=db.backref('editorial_topics', lazy='dynamic'))

    def keys(self):
        self.hide('editorial_topic_id')
        return self.fields

    @staticmethod
    def create_editorial_topic(campaign_id, editorial_topic_id, editorial_topic_name, editorial_topic_description, editorial_topic_tags=None):
        with db.auto_commit():
            new_editorial_topic = Editorial_topic(editorial_topic_id=editorial_topic_id, editorial_topic_name=editorial_topic_name,
                                                  editorial_topic_description=editorial_topic_description)
            linked_campaign = Campaign.query.filter_by(campaign_id=campaign_id).first()
            new_editorial_topic.campaigns.append(linked_campaign)
            db.session.add(new_editorial_topic)
        return 'create editorial_topic success'

    @staticmethod
    def delete_topic(editorial_topic_id):
        with db.auto_commit():
            delete_editorial_topic = Editorial_topic.query.filter_by(editorial_topic_id=editorial_topic_id).first()
            db.session.delete(delete_editorial_topic)
        return 'delete topic success'

    @staticmethod
    def delete_article_from_topic(editorial_topic_id, article_id):
        with db.auto_commit():
            target_editorial_topic = Editorial_topic.query.filter_by(editorial_topic_id=editorial_topic_id).first()
            for article in target_editorial_topic.articles:
                if article.article_id == article_id:
                    target_editorial_topic.articles.remove(article)
                    return 'delete article from topic success'
        return 'this article is not found'

