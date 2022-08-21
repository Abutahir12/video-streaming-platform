import json


def video_streaming_input(event, context):
    event = {"Greetings": "Hello World!"}
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }

    return {"statusCode": 200, "body": json.dumps(body)}
