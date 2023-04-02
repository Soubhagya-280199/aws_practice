import json
import uuid


def lambda_handler(event, context):
    # 1 -read off the input arguments
    customerId = event['CustomerId']

    # 2 -Generate a random ID
    transactionId = str(uuid.uuid1())

    # 3 -do the stuff i.e. save to S3, write to database etc..

    # 4 -Format and return response
    return {'CustomerId': customerId, 'Success': 'True', 'TractionId': transactionId}

