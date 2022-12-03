
class Table:
    def __init__(self, client) -> None:
        self.client = client

    def list_tables(self) -> list:
        return self.client.list_tables()
