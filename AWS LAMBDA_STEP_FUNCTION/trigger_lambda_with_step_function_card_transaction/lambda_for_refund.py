from __future__ import print_function

import json
import boto3
import urllib
import datetime

#input format:
#{'TransactionType' : 'REFUND'}

def refund_handler(message, context):
    try:
        # 1.log intput message
        print("Message has been received into Lambda function REFUND, now IN progresssss....")
        print(message)


        #2. construct response object
        response = {}
        response['TransactionType'] = message['TransactionType']
        response['time']  = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        response['msg'] = "Hello from Lambda function you are in REFUND process .."

        return response
    except Exception as err:
        print(err)

        return err
