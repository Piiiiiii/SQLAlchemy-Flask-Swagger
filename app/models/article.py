from sqlalchemy import Column, Integer, String, ForeignKey, Float, Text, Date
from sqlalchemy.dialects.postgresql import UUID

from app.models.base import Base, db
from app.models.editorial_topic import Editorial_topic

# If a table exists, create_all will not update the changed table. So you should delete this table first.

article_tag = db.Table('article_tag',
              Column('article_id', Integer, ForeignKey('article.article_id')),
              Column('tag_index', Integer, ForeignKey('tag.index')),
              )


# user is a keyword for pqsql
class Article(Base):
    __tablename__ = 'article'
    index = Column(Integer, primary_key=True, autoincrement=True)
    # TODO: list campaign table schema here
    article_id = Column(Integer, unique=True)
    article_importance = Column(Float)
    author = Column(String)
    source = Column(String)
    title = Column(String)
    url = Column(Text)
    time_created = Column(Date)
    thumbnail_url = Column(Text)
    abstract = Column(Text)
    tags = db.relationship('Tag', secondary=article_tag, backref=db.backref('articles', lazy='dynamic'))

    def keys(self):
        self.hide('id')
        return self.fields

    @staticmethod
    def upload_and_parse_url(editorial_topic_id, target_url):
        with db.auto_commit():
            linked_editorial_topic = Editorial_topic.query.filter_by(editorial_topic_id=editorial_topic_id).first()
            linked_article = Article(url=target_url)
            linked_editorial_topic.articles.append(linked_article)
        return 'upload and parse url success'

    @staticmethod
    def create_article(editorial_topic_id, article_id):
        with db.auto_commit():
            linked_editorial_topic = Editorial_topic.query.filter_by(editorial_topic_id=editorial_topic_id).first()
            new_article = Article(article_id=article_id)
            new_article.editorial_topics.append(linked_editorial_topic)
            db.session.add(new_article)
        return 'create article success'

    @staticmethod
    def delete_tag_from_article(article_id, article_tags):
        with db.auto_commit():
            target_article = Article.query.filter_by(article_id=article_id).first()
            for delete_tag in article_tags:
                for exist_tag in target_article.tags:
                    if exist_tag.index == delete_tag['tag_id']:
                        target_article.tags.remove(exist_tag)
                        break
        return 'delete tag from article success'

    @staticmethod
    def edit_article_importance(article_id, article_importance):
        with db.auto_commit():
            target_article = Article.query.filter_by(article_id=article_id).first()
            target_article.article_importance = article_importance
        return 'edit article importance success'
