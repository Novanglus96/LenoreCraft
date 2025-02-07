from ninja import Schema


# The class PartStatusOut is a schema for representing PartStatus information
class PartStatusOut(Schema):
    """
    Schema to represent a PartStatus

    Attributes:
        id (int): The id of the PartStatus.  Required.
        part_status (str): The text status of a part. Required. Unique.
            254 limit.
    """

    id: int
    part_status: str
