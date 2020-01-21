from flask import request

from app.api_docs.v1 import article as api_doc
from app.libs.error_code import Success
from app.libs.redprint import RedPrint
from app.models.article import Article
from app.validators.forms import PaginateValidator

api = RedPrint(name='article', description='Article', api_doc=api_doc)


@api.route('/upload_and_parse_url', methods=['POST'])
@api.doc()
def upload_and_parse_url():
    request_body = request.get_json()
    # user_id = request_body['user_id']
    editorial_topic_id = request_body['editorial_topic_id']
    target_url = request_body['target_url']
    linked_editorial_topic = Article.upload_and_parse_url(
        editorial_topic_id=editorial_topic_id,
        target_url=target_url)
    return Success(linked_editorial_topic)


@api.route('/create_article', methods=['POST'])
@api.doc()
def create_article():
    request_body = request.get_json()
    # user_id = request_body['user_id']
    editorial_topic_id = request_body['editorial_topic_id']
    article_id = request_body['article_id']
    linked_editorial_topic = Article.create_article(
        editorial_topic_id=editorial_topic_id,
        article_id=article_id)
    return Success(linked_editorial_topic)


@api.route('/delete_tag_from_article', methods=['POST'])
@api.doc()
def delete_tag_from_article():
    request_body = request.get_json()
    # user_id = request_body['user_id']
    article_id = request_body['article_id']
    article_tags = request_body['article_tags']
    article = Article.delete_tag_from_article(
        article_id=article_id,
        article_tags=article_tags)
    return Success(article)


@api.route('/edit_article_importance', methods=['POST'])
@api.doc()
def edit_article_importance():
    request_body = request.get_json()
    # user_id = request_body['user_id']
    article_id = request_body['article_id']
    article_importance = request_body['article_importance']
    article = Article.edit_article_importance(
        article_id=article_id,
        article_importance=article_importance)
    return Success(article)
