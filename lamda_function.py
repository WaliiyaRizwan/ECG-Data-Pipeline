import json
import boto3
import datetime

def lambda_handler(event, context):
    
    # Get the data from the incoming HTTP POST request
    # Extract the relevant data from the request
    
    sensor_id = str(datetime.datetime.utcnow())
    pulse = event['pulse']
    
    # Write the data to DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('data-table')
    response = table.put_item(
        Item={
            'id': sensor_id,
            'pulse' : str(pulse),

        }
    )
    
    # Return a success response
    return {
        'statusCode': 200,
        'body': json.dumps('Data written to DynamoDB successfully')
    }
