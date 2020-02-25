# app_put.py
import boto3
import json


def put_item(table_name, content):
    table = dynamodb.Table(table_name)
    response = table.put_item(Item=content)
    return response["ResponseMetadata"]['HTTPStatusCode'] == 200


if __name__ == "__main__":
    dynamodb = boto3.resource('dynamodb', region_name='ap-south-1', endpoint_url="http://localhost:8000")

    fd = open(r"data\books.json", "r")
    books_obj = json.loads(fd.read())
    obj = books_obj["books"][0]
    print(put_item("Books", obj))
