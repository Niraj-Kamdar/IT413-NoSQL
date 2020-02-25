from collections import Counter
from pprint import pprint

import boto3
from boto3.dynamodb.conditions import Key

if __name__ == "__main__":
    dynamodb = boto3.resource('dynamodb', region_name='ap-south-1', endpoint_url="http://localhost:8000")
    table = dynamodb.Table("WebAccessLog")
    response = table.query(KeyConditionExpression=Key("ipaddr").eq("191.182.199.16") & Key("req_no").gte(0),
                           ProjectionExpression="#ts, bytes",
                           ExpressionAttributeNames={"#ts": "timestamp"})
    c = Counter()
    c += Counter(dict(map(lambda a: (a["timestamp"][:11], a["bytes"]), response["Items"])))
    pprint(c)
