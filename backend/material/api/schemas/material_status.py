from ninja import Schema


# The class <model>Out is a schema for representing <model> information
class MaterialStatusOut(Schema):
    """
    Schema to represent a material status

    Attributes:
        id (int): The id of the material status. Required.
        material_status (str): The material status name. Required.
    """

    id: int
    material_status: str
