from __future__ import print_function
import boto3
import time, urllib
import json


s3 = boto3.client('s3')

def lambda_handler(event, context):
    #TODO implementation
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    source_object_key = event['Records'][0]['s3']['object']['key']

    target_bucket = 'test-target-bckt-1'
    copy_source = {'Bucket' :source_bucket, 'Key':source_object_key}

    print("Source bucket : ", source_bucket)
    print("target_bucket : ", target_bucket)
    print("Log Stream name : ", context.log_stream_name)
    print("Log grp name : ",  context.log_group_name)
    print("Request ID : ", context.aws_request_id)
    print("Memory limts(MB) : ", context.memory_limit_in_mb)

    print("event----",event)

    try:
        print("Using waiter to waiting for object to persist through s3 service")
        waiter = s3.get_waiter('object_exists')
        waiter.wait(Bucket=source_bucket, Key=source_object_key)
        s3.copy_object(Bucket=target_bucket, Key=source_object_key, CopySource=copy_source)
        return response['ContentType']

    except Exception as err:
        print("Error -- "+str(err))
        return err