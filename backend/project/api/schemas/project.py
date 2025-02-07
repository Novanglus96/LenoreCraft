from ninja import Schema
from project.api.schemas.project_status import ProjectStatusOut
from pydantic import HttpUrl, Field
from typing import List, Optional, Dict, Any, TYPE_CHECKING
from datetime import date
from decimal import Decimal


# The class ProjectOut is a schema for representing Project information
class ProjectOut(Schema):
    """
    Schema to represent a Project

    Attributes:
        id (int): The id of the Project.  Required.
        project_name (str): The name of the poject. Required. Unique. 254 limit.
        project_status (ProjectStatusOut): A reference to a Project Status. Required.
        project_image (Optional[HttpUrl]): An image for the project. Defaults to None.
        start_date (Optional[date]): The date this project started. Defaults to None.
        due_date (Optional[date]): The date this project is due. Defaults to None.
        completed_date (Optional[date]): The date this project completed. Defaults to None.
        depth_in (Optional[Decimal]): The depth in inches. Defaults to 0.
        width_in (Optional[Decimal]): The width in inches. Defaults to 0.
        height_in (Optional[Decimal]): The height in inches. Defaults to 0.
    """

    id: int
    project_name: str
    project_status: ProjectStatusOut
    project_image: HttpUrl = None
    start_date: Optional[date] = None
    due_date: Optional[date] = None
    completed_date: Optional[date] = None
    depth_in: Decimal = Field(whole_digits=10, decimal_places=5, default=None)
    width_in: Decimal = Field(whole_digits=10, decimal_places=5, default=None)
    height_in: Decimal = Field(whole_digits=10, decimal_places=5, default=None)


# The class ProjectIn is a schema for validating Project information.
class ProjectIn(Schema):
    """
    Schema to validate a Project

    Attributes:
        project_name (str): The name of the poject. Required. Unique. 254 limit.
        project_status (ProjectStatusOut): A reference to a Project Status. Required.
        start_date (Optional[date]): The date this project started. Defaults to None.
        due_date (Optional[date]): The date this project is due. Defaults to None.
        completed_date (Optional[date]): The date this project completed. Defaults to None.
        depth_in (Optional[Decimal]): The depth in inches. Defaults to 0.
        width_in (Optional[Decimal]): The width in inches. Defaults to 0.
        height_in (Optional[Decimal]): The height in inches. Defaults to 0.
    """

    project_name: str
    project_status: ProjectStatusOut
    start_date: Optional[date] = None
    due_date: Optional[date] = None
    completed_date: Optional[date] = None
    depth_in: Decimal = Field(whole_digits=10, decimal_places=5, default=None)
    width_in: Decimal = Field(whole_digits=10, decimal_places=5, default=None)
    height_in: Decimal = Field(whole_digits=10, decimal_places=5, default=None)
