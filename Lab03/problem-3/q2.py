from pprint import pprint

import boto3
from boto3.dynamodb.conditions import Key

if __name__ == "__main__":
    dynamodb = boto3.resource('dynamodb', region_name='ap-south-1', endpoint_url="http://localhost:8000")
    table = dynamodb.Table("Repositories")
    response = table.get_item(Key={"name": "2048", "owner": "janet"})
    rid = response["Item"]["id"]
    table = dynamodb.Table("Issues")
    response = table.scan(FilterExpression=Key("repo_id").eq(rid) & Key("is_resolved").eq(False))
    pprint(response["Items"])