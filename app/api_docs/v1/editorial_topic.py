create_editorial_topic = {
    "parameters": [
        {
            "name": "token",
            "type": "string",
            "description": "access token"
        },
        {
            "name": "campaign_id",
            "type": "integer",
            "description": "UUID string of ID, corresponding to campaign that topic is being added to"
        },
        {
            "name": "editorial_topic_id",
            "type": "integer",
            "description": "UUID string of topic"
        },
        {
            "name": "editorial_topic_name",
            "type": "string",
            "description": "name of editorial topic"
        },
        {
            "name": "editorial_topic_description",
            "type": "string",
            "description": "descriptions of topic"
        }
    ],
    "responses": {
        "200": {
            "description": "success",
            "examples": {}
        }
    }
}

delete_topic = {
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
        }
    ],
    "responses": {
        "200": {
            "description": "success",
            "examples": {}
        }
    }
}

delete_article_from_topic = {
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
            "name": "article_id",
            "type": "integer",
            "description": "UUID string of article"
        }
    ],
    "responses": {
        "200": {
            "description": "success",
            "examples": {}
        }
    }
}
