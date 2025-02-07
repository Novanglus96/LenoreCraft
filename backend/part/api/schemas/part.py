from ninja import Schema
from part.api.schemas.part_status import PartStatusOut
from project.api.schemas.project import ProjectOut
from decimal import Decimal
from pydantic import BaseModel, Field


# The class PartOut is a schema for representing Part information
class PartOut(Schema):
    """
    Schema to represent a Part

    Attributes:
        id (int): The id of the Part.  Required.
        quantity (int): The quantity of this part. Required.
        part_name (str): The name of the part. Required. 254 limit.
        part_status (PartStatusOut): A reference to a Part Status. Required.
        rough_thickness_in (Decimal): The rough thickness of the part in inches.
            Required.
        rough_width_in (Decimal): The rough width of the part in inches. Required.
        rough_length_in (Decimal): The rough length of the part in inches. Required.
        finished_thickness_in (Decimal): The finished thickness of the part in inches.
            Required.
        finished_width_in (Decimal): The finished width of the part in inches. Required.
        finished_length_in (Decimal): The finished length of the part in inches. Required.
        project (ProjectOut): A referece to a Project. Required.
    """

    id: int
    quantity: int
    part_name: str
    part_status: PartStatusOut
    rough_thickness_in: Decimal = Field(whole_digits=10, decimal_places=5)
    rough_width_in: Decimal = Field(whole_digits=10, decimal_places=5)
    rough_length_in: Decimal = Field(whole_digits=10, decimal_places=5)
    finished_thickness_in: Decimal = Field(whole_digits=10, decimal_places=5)
    finished_width_in: Decimal = Field(whole_digits=10, decimal_places=5)
    finished_length_in: Decimal = Field(whole_digits=10, decimal_places=5)
    project: ProjectOut


# The class PartIn is a schema for validating Part information.
class PartIn(Schema):
    """
    Schema to validate a Part

    Attributes:
        quantity (int): The quantity of this part. Required.
        part_name (str): The name of the part. Required. 254 limit.
        part_status_id (int): A reference to a Part Status id. Required.
        rough_thickness_in (Decimal): The rough thickness of the part in inches.
            Required.
        rough_width_in (Decimal): The rough width of the part in inches. Required.
        rough_length_in (Decimal): The rough length of the part in inches. Required.
        finished_thickness_in (Decimal): The finished thickness of the part in inches.
            Required.
        finished_width_in (Decimal): The finished width of the part in inches. Required.
        finished_length_in (Decimal): The finished length of the part in inches. Required.
        project_id (int): A referece to a Project id. Required.
    """

    quantity: int
    part_name: str
    part_status_id: int
    rough_thickness_in: Decimal = Field(whole_digits=10, decimal_places=5)
    rough_width_in: Decimal = Field(whole_digits=10, decimal_places=5)
    rough_length_in: Decimal = Field(whole_digits=10, decimal_places=5)
    finished_thickness_in: Decimal = Field(whole_digits=10, decimal_places=5)
    finished_width_in: Decimal = Field(whole_digits=10, decimal_places=5)
    finished_length_in: Decimal = Field(whole_digits=10, decimal_places=5)
    project_id: int
