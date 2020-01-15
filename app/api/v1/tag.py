from flask import request

from app.api_docs.v1 import campaign as api_doc
from app.libs.error_code import Success
from app.libs.redprint import RedPrint
from app.models.tag import Tag
from app.validators.forms import PaginateValidator

api = RedPrint(name='tag', description='tag', api_doc=api_doc)


@api.route('/create_tag')
@api.doc()
def create_tag():
    request_body = request.get_json()
    # user_id = request_body['user_id']
    tag_name = request_body['tag_name']
    tag_entity_type = request_body['tag_entity_type']
    message = Tag.create_tag(
        tag_name=tag_name,
        tag_entity_type=tag_entity_type)
    return message


@api.route('/add_tag_to_topic')
@api.doc()
def add_tag_to_topic():
    request_body = request.get_json()
    # user_id = request_body['user_id']
    editorial_topic_id = request_body['editorial_topic_id']
    editorial_topic_tags = request_body['editorial_topic_tags']
    message = Tag.add_tag_to_topic(
        editorial_topic_id=editorial_topic_id,
        editorial_topic_tags=editorial_topic_tags)
    return message


@api.route('/add_tag_to_article')
@api.doc()
def add_tag_to_article():
    request_body = request.get_json()
    # user_id = request_body['user_id']
    article_id = request_body['article_id']
    article_tags = request_body['article_tags']
    message = Tag.add_tag_to_article(
        article_id=article_id,
        article_tags=article_tags)
    return message
