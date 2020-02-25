# app_create.py
import boto3


def create_table(_table_name):
    dynamodb.create_table(
            TableName=_table_name,
            KeySchema=[
                {
                    'AttributeName': 'publisher',
                    'KeyType': 'HASH'  # Partition key
                },
                {
                    'AttributeName': 'title',
                    'KeyType': 'RANGE'  # Sort key
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'publisher',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'title',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'isbn',
                    'AttributeType': 'S'
                }
            ],
            GlobalSecondaryIndexes=[
                {
                    'IndexName': 'isbn-index',
                    'KeySchema': [
                        {
                            'KeyType': 'HASH',
                            'AttributeName': 'isbn'
                        }
                    ],
                    'Projection': {
                        'ProjectionType': 'ALL'
                    },
                    'ProvisionedThroughput': {
                        'ReadCapacityUnits': 10,
                        'WriteCapacityUnits': 10
                    }
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
    )


if __name__ == "__main__":
    dynamodb = boto3.resource('dynamodb', region_name='ap-south-1', endpoint_url="http://localhost:8000")
    table_name = "Books"
    try:
        resp = dynamodb.Table(table_name).load()
        print("Table Books already exists")

    except boto3.exceptions.ResourceNotFoundException:
        create_table(table_name)
