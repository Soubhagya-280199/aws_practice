import json

def lambda_handler(event, context):
    
    #print the event which trggred by SQS
    print("SQS triggred lambda") 
    
    results = event['Records']
    
    for result in results:
        print(result['body'])
    
    
    #return statement
    # return {
    #     'statusCode': 200,
    #     'body': json.dumps('SUccessfull')
    # }




#In this SQS and Lambda trigger operation
# 1.we have to create lambda finction first then we need to add configuration as policies under it and give the services
# as SQS and its related stuffs
# 2. after that we need to create SQS and add lambda on it so that trigger will be created .
# 3.after all set up we need to send a message manually via the sqs whcih will trigger the AWS lambda
# 4. if we want to check the successfull operations then we need to check the cloud watch LOG


