from ninja import Schema


# The class ProjectStatusOut is a schema for representing ProjectStatus information
class ProjectStatusOut(Schema):
    """
    Schema to represent a ProjectStatus

    Attributes:
        id (int): The id of the ProjectStatus.  Required.
        project_status (str): The text status of a project. Required. Unique.
    """

    id: int
    project_status: str
