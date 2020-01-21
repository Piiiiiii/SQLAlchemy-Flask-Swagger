from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.models.base import Base, db
from app.models.editorial_topic import Editorial_topic
from app.models.article import Article

# If a table exists, create_all will not update the changed table. So you should delete this table first.


# user is a keyword for pqsql
class Tag(Base):
    __tablename__ = 'tag'
    index = Column(Integer, primary_key=True, autoincrement=True)
    # TODO: list campaign table schema here
    tag_name = Column(String)
    tag_entity_type = Column(String)

    def keys(self):
        self.hide('index')
        return self.fields

    @staticmethod
    def create_tag(tag_name, tag_entity_type):
        with db.auto_commit():
            new_tag = Tag(tag_name=tag_name, tag_entity_type=tag_entity_type)
            db.session.add(new_tag)
        return 'create tag success'

    @staticmethod
    def add_tag_to_topic(editorial_topic_id, editorial_topic_tags):
        with db.auto_commit():
            linked_editorial_topic = Editorial_topic.query.filter_by(editorial_topic_id=editorial_topic_id).first_or_404()
            for tag in editorial_topic_tags:
                linked_tag = Tag.query.filter_by(index=tag['tag_id']).first()
                linked_editorial_topic.tags.append(linked_tag)
        return linked_editorial_topic

    @staticmethod
    def add_tag_to_article(article_id, article_tags):
        with db.auto_commit():
            linked_article = Article.query.filter_by(article_id=article_id).first_or_404()
            for tag in article_tags:
                linked_tag = Tag.query.filter_by(index=tag['tag_id']).first()
                linked_article.tags.append(linked_tag)
        return linked_article
