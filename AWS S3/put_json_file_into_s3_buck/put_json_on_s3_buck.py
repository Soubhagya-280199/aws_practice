import boto3
import json


s3_client = boto3.client('s3')

def put_json_on_s3_handler(event, context):

    try:
        buck_name = "store-json-object"

        file_name = "store" + ".json"

        transactiondet = {}

        transactiondet['name'] = 'Raja'
        transactiondet['age'] = '23'
        transactiondet['class'] = '10th'
        transactiondet['address'] = 'Cuttack'

        data = bytes(json.dumps(transactiondet).encode('utf-8'))
        reqst = s3_client.put_object(Bucket=buck_name, Key=file_name, Body=data)

        print("Put successfully complete")

    except Exception as err:
        print(err)