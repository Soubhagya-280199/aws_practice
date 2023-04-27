import ast
import boto3
import json

#get s3 client
s3_client = boto3.client('s3')

#get dynamodb resource
dynamodb = boto3.resource('dynamodb')

def jsons3todynamodb_handler(event, context):
    try:
        # get the bucket name and key name
        buckt_name = event['Records'][0]['s3']['bucket']['name']
        json_file_nm = event['Records'][0]['s3']['object']['key']


        # get the json data from s3 bucket
        json_objct = s3_client.get_object(Bucket=buckt_name, Key=json_file_nm)

        # read the json file
        json_file_reader = json_objct['Body'].read().decode('utf-8')

        #convert the json file into dict
        json_dict = ast.literal_eval(json_file_reader)

        # get the table name
        table_nm = dynamodb.Table('table_db')

        # put the items into the table
        table_nm.put_item(Item = json_dict)

        return "Lambda Function successfully completed"

    except Exception as e:
        return e




