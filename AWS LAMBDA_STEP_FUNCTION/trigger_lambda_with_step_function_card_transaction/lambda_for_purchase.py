from __future__ import print_function

import json
import boto3
import urllib
import datetime

#input format example
#{'TransactionType' : 'PURCHASE'}

def purchase_handler(message, context):
    try:
        #1.log intput message
        print("Message has been received into Lambda function PURCHASE, now IN progresssss....")
        print(message)

        #2. construct the response object
        response = {}
        response['TransactionType'] = message['TransactionType']
        response['time'] = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%')
        response['msg'] = "Hello from Lambda function you are in PURCHASE process .."

        return response

    except Exception as err:
        print(err)

        return err




# arn:aws:lambda:ap-south-1:872877685050:function:lambda_for_purchase


# arn:aws:lambda:ap-south-1:872877685050:function:lambda_for_refund