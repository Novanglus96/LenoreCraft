from ninja import Schema


# The class StoreOut is a schema for representing store information
class StoreOut(Schema):
    """
    Schema to represent a Store

    Attributes:
        id (int): The id of the Store. Required.
        store_name (str): The name of the Store. Required.
    """

    id: int
    store_name: str


# The class StoreIn is a schema for validating Store information.
class StoreIn(Schema):
    """
    Schema to validate a Store

    Attributes:
        store_name (str): The name of the Store. Required.
    """

    store_name: str
