from ninja import Schema


# The class VersionOut is a schema for representing version information
class VersionOut(Schema):
    """
    Schema to represent a Version

    Attributes:
        id (int): The id of the Version. Required.
        version_number (str): The version number. Required.
    """

    id: int
    version_number: str
