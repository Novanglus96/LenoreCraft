from ninja import Schema


# The class ProjectPhaseOut is a schema for representing ProjectPhase information
class ProjectPhaseOut(Schema):
    """
    Schema to represent a ProjectPhase

    Attributes:
        id (int): The id of the ProjectPhase.  Required.
        project_phase (str): The text phase of a project. Required. Unique.
    """

    id: int
    project_phase: str
