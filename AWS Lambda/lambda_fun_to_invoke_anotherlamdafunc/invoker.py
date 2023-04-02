import json
import boto3

client = boto3.client('lambda')


def lambda_handler(event, context):
    inputforInvoker = {'CustomerId': 123, 'amount': 50}

    response = client.invoke(
        FunctionName='arn:aws:lambda:ap-south-1:872877685050:function:lamdatoinvoker',
        InvocationType='RequestResponse',  # event
        Payload=json.dumps(inputforInvoker)
    )

    responseJson = json.load(response['Payload'])

    print('\n')
    print(responseJson)
    print('\n')