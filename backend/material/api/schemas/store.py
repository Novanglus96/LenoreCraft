from ninja import Schema


# The class StoreOut is a schema for representing store information
class StoreOut(Schema):
    """
    Schema to represent a Store

    Args:
        id (int): The id of the Store
        store_name (str): The name of the Store
    """

    id: int
    store_name: str


# The class StoreIn is a schema for validating Store information.
class StoreIn(Schema):
    """
    Schema to validate a Store

    Args:
        store_name (str): The name of the Store
    """

    store_name: str
