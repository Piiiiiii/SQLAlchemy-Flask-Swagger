from flask import request

from app.api_docs.v1 import campaign as api_doc
from app.libs.error_code import Success
from app.libs.redprint import RedPrint
from app.models.article import Article
from app.validators.forms import PaginateValidator

api = RedPrint(name='article', description='Article', api_doc=api_doc)


@api.route('/upload_and_parse_url', methods=['GET'])
@api.doc()
def upload_and_parse_url():
    request_body = request.get_json()
    # user_id = request_body['user_id']
    editorial_topic_id = request_body['editorial_topic_id']
    target_url = request_body['target_url']
    message = Article.upload_and_parse_url(
        editorial_topic_id=editorial_topic_id,
        target_url=target_url)
    return message


@api.route('/create_article', methods=['GET'])
@api.doc()
def create_article():
    request_body = request.get_json()
    # user_id = request_body['user_id']
    editorial_topic_id = request_body['editorial_topic_id']
    article_id = request_body['article_id']
    message = Article.create_article(
        editorial_topic_id=editorial_topic_id,
        article_id=article_id)
    return message


@api.route('/delete_tag_from_article', methods=['GET'])
@api.doc()
def delete_tag_from_article():
    request_body = request.get_json()
    # user_id = request_body['user_id']
    article_id = request_body['article_id']
    article_tags = request_body['article_tags']
    message = Article.delete_tag_from_article(
        article_id=article_id,
        article_tags=article_tags)
    return message


@api.route('/edit_article_importance', methods=['GET'])
@api.doc()
def edit_article_importance():
    request_body = request.get_json()
    # user_id = request_body['user_id']
    article_id = request_body['article_id']
    article_importance = request_body['article_importance']
    message = Article.edit_article_importance(
        article_id=article_id,
        article_importance=article_importance)
    return message
