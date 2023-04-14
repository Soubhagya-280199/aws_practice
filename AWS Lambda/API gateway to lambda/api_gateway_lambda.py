from __future__ import print_function

import json
import urllib
import boto3

print("Function is loading .........")
#Json input format will be
# {"transactionId" : "121212",
#  "transactionType" : "PURCHASE",
# "transactionAmount" : "500" }

def api_gateway_handler(event, context):

    try:
        #1. parsing all the input parameters
        transactionID = event["queryStringParameters"]["transactionId"]
        transactionType = event["queryStringParameters"]["type"]
        transactionAmount = event["queryStringParameters"]["amount"]

        #2. Create response object
        response = {}

        response["transactionID"] = transactionID
        response["transactionType"] = transactionType
        response["transactionAmount"] = transactionAmount
        response["message"] = "Hello from Lambda function "

        #3. Create http response Object
        responseObject = {}
        responseObject["statusCode"]  = 200
        responseObject["headers"]  = {}
        responseObject["headers"]["Content-Type"] = "application/json"
        responseObject["body"] = json.dumps(response)

        return responseObject

    except Exception as err:
        print(err)

        return err




