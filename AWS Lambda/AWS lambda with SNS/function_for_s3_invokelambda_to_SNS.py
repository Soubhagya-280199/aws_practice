"""
Description : Code describes the process, if a file dropped at S3 bucket,
then it will invoke it's related lambda function and using lambda function we have to perform a SNS publish as well
1. Create a s3 bucket,Create a SNS topic, create a lambda fucntion and add the trigger as well, give the lambda 3 access s3 fullacess,
    cloud watch logs , sns full access.
2 .
3 . read the s3 bucket name and file name
4 . store that file name and path in a variable
5 . create an additional function which will perform as SNS publisher.
6 . the fucnction will take two parameters one is message with path and Subject of the message line
7.  Configure the SNS arn
"""

import boto3


#sns_topic_arn = "arn:aws:sns:ap-south-1:793849647146:sns_first"
sns_topic_arn = ""
def sns_send(msg, sub):
    try:
        sns_client = boto3.client('sns')
        result = sns_client.publish(TopicArn=sns_topic_arn,  Message=msg, Subject = sub)

        if result['ResponseMetadata']['HTTPStatusCode'] == 200:
            print(result)
            print("Notification sent successfully ")
            return True
    except Exception as err:
        print(err)

def lambda_handler(event,context):
    try:
        print(f"Event Collected : {event}")

        for record in event['Records']:
            s3_bucket = record['s3']['bucket']['name']
            print(f"S3_bucket name : {s3_bucket}")
            s3_key = record['s3']['bucket']
            print(f"File present in bucket: {s3_key}")
            file_path = f"s3://{s3_bucket}{s3_key}"

            message  = f"HuRray file {s3_key} dropped at {file_path} loation"
            subject = "Process Completion Notification"

            sns_res = sns_send(message,subject)

            if sns_res:
                print("Notification sent successfully ")
                return sns_res
            else:
                return False

    except Exception as err:
        print(err)


