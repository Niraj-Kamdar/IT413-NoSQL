from pprint import pprint

import boto3
from boto3.dynamodb.conditions import Key

if __name__ == "__main__":
    dynamodb = boto3.resource('dynamodb', region_name='ap-south-1', endpoint_url="http://localhost:8000")
    table = dynamodb.Table("Users")
    response = table.query(
            KeyConditionExpression=Key("email").eq("opensource@mozilla.org") & Key("username").eq("mozilla"),
            ProjectionExpression="members")
    members = response["Items"][0]["members"]
    table = dynamodb.Table("Repositories")
    response = table.query(KeyConditionExpression=Key("owner").eq("mozilla") & Key("name").eq("pdf.js"),
                           ProjectionExpression="id")
    rid = response["Items"][0]["id"]
    table = dynamodb.Table("Commits")
    data = []
    for author in members:
        response = table.scan(FilterExpression=Key("project_id").eq(rid) & Key("author").eq(author))
        data.extend(response["Items"])
    pprint(data)
