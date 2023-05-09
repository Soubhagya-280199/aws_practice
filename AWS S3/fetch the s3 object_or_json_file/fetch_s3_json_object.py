import boto3
import json

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    try :
        buck_name = "json-holder-obj"
        json_file = "newjson.json"

        response = s3_client.get_object(Bucket =buck_name,Key= json_file)

        content = response['Body']

        json_data = json.loads(content.read())

        widget = json_data['widget']
        #here we can play with the data

        for res in widget:
            print(res,"\n")
            print("------")

    except Exception as err:
        print(err)