# app_get.py
from pprint import pprint

import boto3


def get_item(table_name, key):
    table = dynamodb.Table(table_name)
    response = table.get_item(Key=key)
    return response["Item"]


if __name__ == "__main__":
    dynamodb = boto3.resource('dynamodb', region_name='ap-south-1', endpoint_url="http://localhost:8000")
    obj = dict(title="Designing Evolvable Web APIs with ASP.NET", publisher="O'Reilly Media")
    pprint(get_item("Books", obj))
