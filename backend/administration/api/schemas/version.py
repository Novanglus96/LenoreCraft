from ninja import Schema


# The class VersionOut is a schema for representing version information
class VersionOut(Schema):
    """
    Schema to represent a Version

    Args:
        id (int): The id of the Version
        version_number (str): The version number
    """

    id: int
    version_number: str
