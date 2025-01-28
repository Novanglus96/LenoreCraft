from ninja import Schema


# The class StoreOut is a schema for representing store information
class StoreOut(Schema):
    id: int
    store_name: str


# The class StoreIn is a schema for validating Store information.
class StoreIn(Schema):
    store_name: str
