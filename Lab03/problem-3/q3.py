from pprint import pprint
from datetime import datetime as dt
import boto3
from boto3.dynamodb.conditions import Key


def to_epoch(x):
    x["epoch"] = dt.strptime(x["timestamp"], "%Y-%m-%dT%H:%M:%SZ").timestamp()
    return x


if __name__ == "__main__":
    dynamodb = boto3.resource('dynamodb', region_name='ap-south-1', endpoint_url="http://localhost:8000")
    table = dynamodb.Table("Repositories")
    response = table.query(KeyConditionExpression=Key("name").eq("linux") & Key("owner").eq("torvalds"),
                           ProjectionExpression="id")
    rid = response["Items"][0]["id"]
    table = dynamodb.Table("Commits")
    response = table.scan(FilterExpression=Key("project_id").eq(rid))
    pprint(max(map(to_epoch, response["Items"]), key=lambda x: x["epoch"]))
