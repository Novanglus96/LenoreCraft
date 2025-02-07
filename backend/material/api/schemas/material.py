from ninja import Schema
from material.api.schemas.material_object import MaterialObjectOut
from material.api.schemas.material_status import MaterialStatusOut
from typing import List, Optional, Dict, Any, TYPE_CHECKING
from project.api.schemas.project import ProjectOut


# The class MaterialOut is a schema for representing Material information
class MaterialOut(Schema):
    """
    Schema to represent a Material

    Attributes:
        id (int): The id of the Material.  Required.
        material_object (MaterialObjectOut): A reference to a MaterialObject. Required.
        quantity (int): The number of MaterialObjects. Required. Defaults to 1.
        material_status (Optional[MaterialStatusOut]): A reference to a MaterialStatus. Defaults
            to None.
        project (Optional[ProjectOut]): A reference to a Project. Defaults to None.
    """

    id: int
    material_object: MaterialObjectOut
    quantity: int = 1
    material_status: MaterialStatusOut = None
    project: ProjectOut


# The class MaterialIn is a schema for validating Material information.
class MaterialIn(Schema):
    """
    Schema to validate a Material

    Attributes:
        material_object_id (int): The ID of a MaterialObject. Required.
        quantity (int): The number of MaterialObjects. Required. Defaults to 1.
        material_status_id (Optional[int]): The ID of a MaterialStatus. Defaults
            to None.
        project_id (Optional[int]): The ID of a Project. Defaults to None.
    """

    material_object_id: int
    quantity: int = 1
    material_status_id: Optional[int] = None
    project_id: Optional[int] = None
