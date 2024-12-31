from ninja import Schema


# The class VersionOut is a schema for representing version information
class VersionOut(Schema):
    id: int
    version_number: str
