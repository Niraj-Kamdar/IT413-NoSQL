import boto3

if __name__ == "__main__":
    dynamodb = boto3.resource('dynamodb', region_name='ap-south-1', endpoint_url="http://localhost:8000")
    table = dynamodb.Table("Commits")
    commit = {
        "sha": "K9QTUE0U3SKDFFKFVP7PMTMQF6GZNEB8NSFH1K",
        "author": "lisa",
        "message": "Resolved an issue from pdf.js",
        "project_id": 4243,
        "timestamp": "2020-02-19T20:40:38Z"
    }
    table.put_item(Item=commit)

    table = dynamodb.Table("Issues")
    table.update_item(Key=dict(repo_id=4243, title="No Documentation for installation"),
                      UpdateExpression="set is_resolved = :ir",
                      ExpressionAttributeValues={":ir": True}
                      )
