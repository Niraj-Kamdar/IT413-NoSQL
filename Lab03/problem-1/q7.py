from pprint import pprint
from boto3.dynamodb.conditions import Key

import boto3

# Write Code here
if __name__ == "__main__":
    dynamodb = boto3.resource('dynamodb', region_name='ap-south-1', endpoint_url="http://localhost:8000")
    books = dynamodb.Table("Books")
    data = books.scan(FilterExpression=Key("pages").gt(300))
    pprint(data["Items"])
