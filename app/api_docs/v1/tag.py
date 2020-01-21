create_tag = {
    "parameters": [
        {
            "name": "token",
            "type": "string",
            "description": "access token"
        },
        {
            "name": "tag_name",
            "type": "string",
            "description": "name of tag"
        },
        {
            "name": "tag_entity_type",
            "type": "string",
            "description": "entity type of tag "
                           "(default value to none when uploading to backend, if no value has been passed)"
        }
    ],
    "responses": {
        "200": {
            "description": "success",
            "examples": {}
        }
    }
}

add_tag_to_topic = {
    "parameters": [
        {
            "name": "token",
            "type": "string",
            "description": "access token"
        },
        {
            "name": "editorial_topic_id",
            "type": "integer",
            "description": "UUID string of topic"
        },
        {
            "name": "editorial_topic_tags",
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

add_tag_to_article = {
    "parameters": [
        {
            "name": "token",
            "type": "string",
            "description": "access token"
        },
        {
            "name": "article_id",
            "type": "integer",
            "description": "UUID string of article"
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