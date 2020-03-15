# app_get_second.py
from pprint import pprint

import boto3
from boto3.dynamodb.conditions import Key


def query_item(table_name, val):
    table = dynamodb.Table(table_name)
    response = table.query(IndexName="isbn-index", KeyConditionExpression=Key("isbn").eq(val))
    return response["Items"]


if __name__ == "__main__":
    dynamodb = boto3.resource('dynamodb', region_name='ap-south-1', endpoint_url="http://localhost:8000")
    pprint(query_item("Books", "9781449337711"))
