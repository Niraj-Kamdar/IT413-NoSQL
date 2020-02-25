# app_update.py
import boto3


def update_item(table_name, _key_val, _updated_val):
    key, value = _updated_val
    table = dynamodb.Table(table_name)
    table.update_item(
            Key=_key_val,
            UpdateExpression="SET #key = :val",
            ExpressionAttributeNames={
                "#key": key,
            },
            ExpressionAttributeValues={
                ":val": value
            }
    )


if __name__ == "__main__":
    dynamodb = boto3.resource('dynamodb', region_name='ap-south-1', endpoint_url="http://localhost:8000")

    keyVal = {
        "title": "Git Pocket Guide",
        "publisher": "O'Reilly Media"
    }

    updatedVal = ["pages", 268]
    update_item("Books", keyVal, updatedVal)
