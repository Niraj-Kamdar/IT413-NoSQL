# app_batch_write.py
import json

import boto3


def batch_write(table_name, contents):
    table = dynamodb.Table(table_name)

    with table.batch_writer() as batch:
        for item in contents:
            batch.put_item(Item=item)


if __name__ == "__main__":
    dynamodb = boto3.resource('dynamodb', region_name='ap-south-1', endpoint_url="http://localhost:8000")

    with open(r"data\books.json", "r") as fd:
        books_obj = json.loads(fd.read())

        obj = books_obj["books"][1:100]
        batch_write("Books", obj)
