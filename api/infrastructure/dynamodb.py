import os
import boto3

class Client:
    def __init__(self) -> None:
        self.client = boto3.client(
            "dynamodb",
            endpoint_url=os.environ["DYNAMO_ENDPOINT"]
        )


    def list_tables(self) -> list:
        res = self.client.list_tables()
        if 'TableNames' not in res:
            return []
        return res['TableNames']

