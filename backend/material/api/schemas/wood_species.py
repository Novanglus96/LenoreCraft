from ninja import Schema


# The class WoodSpeciesOut is a schema for representing WoodSpecies information
class WoodSpeciesOut(Schema):
    """
    Schema to represent a WoodSpecies

    Attributes:
        id (int): The id of the WoodSpecies. Required.
        wood_species_name (str): The name of the WoodSpecies. Required.
    """

    id: int
    wood_species_name: str
