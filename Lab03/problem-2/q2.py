import asyncio
import json

import boto3


async def batch_write(table_name, contents):
    table = dynamodb.Table(table_name)

    with table.batch_writer() as batch:
        for item in contents:
            batch.put_item(Item=item)


async def main():
    with open(r"data\web_access_log.json", "r") as f:
        d = json.load(f)
    for i in range(len(d) // 25):
        await batch_write("WebAccessLog", d[i * 25:(i + 1) * 25])


dynamodb = boto3.resource('dynamodb', region_name='ap-south-1', endpoint_url="http://localhost:8000")
asyncio.run(main())
