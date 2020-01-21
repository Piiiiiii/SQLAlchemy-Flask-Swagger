upload_and_parse_url = {
    "parameters": [
        {
            "name": "token",
            "type": "string",
            "description": "access token"
        },
        {
            "name": "editorial_topic_id",
            "type": "integer",
            "description": "UUID of topic"
        },
        {
            "name": "target_url",
            "type": "string",
            "description": "url of source content to parse"
        }
    ],
    "responses": {
        "200": {
            "description": "success",
            "examples": {}
        }
    }
}

create_article = {
    "parameters": [
        {
            "name": "token",
            "type": "string",
            "description": "access token"
        },
        {
            "name": "editorial_topic_id",
            "type": "integer",
            "description": "UUID of topic"
        },
        {
            "name": "article_id",
            "type": "integer",
            "description": "UUID of article"
        }
    ],
    "responses": {
        "200": {
            "description": "success",
            "examples": {}
        }
    }
}

delete_tag_from_article = {
    "parameters": [
        {
            "name": "token",
            "type": "string",
            "description": "access token"
        },
        {
            "name": "article_id",
            "type": "integer",
            "description": "UUID of article"
        },
        {
            "name": "article_tags",
            "type": "object[]",
            "description": "elements: tag_id(integer)"
        }
    ],
    "responses": {
        "200": {
            "description": "success",
            "examples": {}
        }
    }
}

edit_article_importance = {
    "parameters": [
        {
            "name": "token",
            "type": "string",
            "description": "access token"
        },
        {
            "name": "article_id",
            "type": "integer",
            "description": "UUID of article"
        },
        {
            "name": "article_importance",
            "type": "float",
            "description": "float number of article importance level"
        }
    ],
    "responses": {
        "200": {
            "description": "success",
            "examples": {}
        }
    }
}
