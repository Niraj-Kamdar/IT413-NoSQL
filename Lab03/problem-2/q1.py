import boto3

dynamodb = boto3.resource('dynamodb', region_name='ap-south-1', endpoint_url="http://localhost:8000")
dynamodb.create_table(
        TableName="WebAccessLog",
        KeySchema=[
            {
                'AttributeName': 'ipaddr',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'req_no',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[{'AttributeName': 'req_no', 'AttributeType': 'N'},
                              {'AttributeName': 'ipaddr', 'AttributeType': 'S'}],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
)
