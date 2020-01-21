from flask import request

from app.api_docs.v1 import tag as api_doc
from app.libs.error_code import Success
from app.libs.redprint import RedPrint
from app.models.tag import Tag
from app.validators.forms import PaginateValidator

api = RedPrint(name='tag', description='Tag', api_doc=api_doc)


@api.route('/create_tag', methods=['POST'])
@api.doc()
def create_tag():
    request_body = request.get_json()
    # user_id = request_body['user_id']
    tag_name = request_body['tag_name']
    if 'tag_entity_type' in request_body:
        tag_entity_type = request_body['tag_entity_type']
    else:
        tag_entity_type = 'none'
    message = Tag.create_tag(
        tag_name=tag_name,
        tag_entity_type=tag_entity_type)
    return message


@api.route('/add_tag_to_topic', methods=['POST'])
@api.doc()
def add_tag_to_topic():
    request_body = request.get_json()
    # user_id = request_body['user_id']
    editorial_topic_id = request_body['editorial_topic_id']
    editorial_topic_tags = request_body['editorial_topic_tags']
    linked_editorial_topic = Tag.add_tag_to_topic(
        editorial_topic_id=editorial_topic_id,
        editorial_topic_tags=editorial_topic_tags)
    return Success(linked_editorial_topic)


@api.route('/add_tag_to_article', methods=['POST'])
@api.doc()
def add_tag_to_article():
    request_body = request.get_json()
    # user_id = request_body['user_id']
    article_id = request_body['article_id']
    article_tags = request_body['article_tags']
    linked_article = Tag.add_tag_to_article(
        article_id=article_id,
        article_tags=article_tags)
    return Success(linked_article)
