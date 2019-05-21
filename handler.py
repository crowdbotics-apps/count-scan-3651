import json


def hello(event, context):
    body = {
        "message": "Congratulations! You just released your first serverless function - count_scan_3651 - with Crowdbotics! Reward yourself! Grab a cup of coffee!"
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
