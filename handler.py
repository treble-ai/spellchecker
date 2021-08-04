import json

def spell_check(event, context):
    body = {
        "message": "Go Treble!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response





