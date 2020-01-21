from flask import request

from app.api_docs.v1 import editorial_topic as api_doc
from app.libs.error_code import Success
from app.libs.redprint import RedPrint
from app.models.editorial_topic import Editorial_topic
from app.validators.forms import PaginateValidator

api = RedPrint(name='editorial_topic', description='Editorial_topic', api_doc=api_doc)


@api.route('/create_editorial_topic', methods=['POST'])
@api.doc()
def create_editorial_topic():
    request_body = request.get_json()
    # user_id = request_body['user_id']
    campaign_id = request_body['campaign_id']
    editorial_topic_id = request_body['editorial_topic_id']
    editorial_topic_name = request_body['editorial_topic_name']
    editorial_topic_description = request_body['editorial_topic_description']
    linked_campaign = Editorial_topic.create_editorial_topic(
        # user_id=user_id,
        campaign_id=campaign_id,
        editorial_topic_id=editorial_topic_id,
        editorial_topic_name=editorial_topic_name,
        editorial_topic_description=editorial_topic_description)
    return Success(linked_campaign)


@api.route('/delete_topic', methods=['POST'])
@api.doc()
def delete_topic():
    request_body = request.get_json()
    # user_id = request_body['user_id']
    editorial_topic_id = request_body['editorial_topic_id']
    delete_editorial_topic = Editorial_topic.delete_topic(
        # user_id=user_id,
        editorial_topic_id=editorial_topic_id)
    return Success(delete_editorial_topic)


@api.route('/delete_article_from_topic', methods=['POST'])
@api.doc()
def delete_article_from_topic():
    request_body = request.get_json()
    # user_id = request_body['user_id']
    editorial_topic_id = request_body['editorial_topic_id']
    article_id = request_body['article_id']
    target_editorial_topic = Editorial_topic.delete_article_from_topic(
        # user_id=user_id,
        editorial_topic_id=editorial_topic_id,
        article_id=article_id)
    return Success(target_editorial_topic)
