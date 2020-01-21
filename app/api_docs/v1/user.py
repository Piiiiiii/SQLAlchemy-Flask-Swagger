create_user = {
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
        }
    ],
    "responses": {
        "200": {
            "description": "success",
            "examples": {}
        }
    }
}
