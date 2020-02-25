import boto3
from boto3.dynamodb.conditions import Key

if __name__ == "__main__":
    dynamodb = boto3.resource('dynamodb', region_name='ap-south-1', endpoint_url="http://localhost:8000")
    table = dynamodb.Table("WebAccessLog")
    response = table.query(Select="COUNT",
                           KeyConditionExpression=Key("ipaddr").eq("188.45.108.168") & Key("req_no").gte(0),
                           FilterExpression=Key("status").gt(200) | Key("status").lt(200))
    print(f"For IP address 188.45.108.168, count of requests that have not returned status 200 is {response['Count']}")
