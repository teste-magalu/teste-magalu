# A sample schema, like what we'd get from json.load()
schema_message = {
    "type" : "object",
    "properties" : {
    "recipient" : {"type" : "string", "error_msg": "invalid input"},
		"message" : {"type" : "string", "error_msg": "invalid input"},
		"date_time" : {"type" : "string", "error_msg": "invalid input"},
    },
    "required": ["recipient", "message", "date_time"]
}
