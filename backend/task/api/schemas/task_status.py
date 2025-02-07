from ninja import Schema


# The class TaskStatusOut is a schema for representing TaskStatus information
class TaskStatusOut(Schema):
    """
    Schema to represent a TaskStatus

    Attributes:
        id (int): The id of the TaskStatus.  Required.
        task_status (str): The status text of a task. Required. Unique. 254 limit.
    """

    id: int
    task_status: str
