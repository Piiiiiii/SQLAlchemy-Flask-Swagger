create_campaign = {
    "parameters": [
        {
            "name": "token",
            "type": "string",
            "description": "access token"
        },
        {
            "name": "user_id",
            "type": "integer",
            "description": "UUID string for user creating campaign (later versions of API should check "
                           "if user has permission to create campaign)"
        },
        {
            "name": "campaign_name",
            "type": "string",
            "description": "name of campaign"
        },
        {
            "name": "campaign_obj_type",
            "type": "string",
            "enum": [
                    "私域促活/留存",
                    "私域拉新",
                    "裂变"
                  ],
            "description": "campaign objective type"
        },
        {
            "name": "campaign_time_start",
            "type": "string",
            "description": "ISO date format, YYYY-MM-DD"
        },
        {
            "name": "campaign_time_end",
            "type": "string",
            "description": "ISO date format, YYYY-MM-DD"
        }
    ],
    "responses": {
        "200": {
            "description": "success",
            "examples": {}
        }
    }
}

get_campaigns = {
    "parameters": [
        {
            "name": "token",
            "type": "string",
            "description": "access token"
        },
        {
            "name": "user_id",
            "type": "integer",
            "description": "UUID string for user creating campaign (later versions of API should check "
                           "if user has permission to create campaign)"
        },
        {
            "name": "items_per_page",
            "type": "integer",
            "description": "number of items per page (default: 15, if no value)"
        },
        {
            "name": "page_number",
            "type": "integer",
            "description": "page number (default: 1, if no value)"
        },
    ],
    "responses": {
        "200": {
            "description": "success",
            "examples": {}
        }
    }
}
