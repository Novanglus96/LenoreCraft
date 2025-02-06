from ninja import Schema
from decimal import Decimal
from material.api.schemas.store import StoreOut
from material.api.schemas.wood_species import WoodSpeciesOut
from typing import List, Optional, Dict, Any, TYPE_CHECKING
from pydantic import BaseModel, Field


# The class MaterialObjectOut is a schema for representing MaterialObject information
class MaterialObjectOut(Schema):
    """
    Schema to represent a MaterialObject

    Attributes:
        id (int): The id of the MaterialObject. Required.
        material_object_name (str): The name of the material object. Required.
        thickness_in (Optional[Decimal]): The thickness of the material object in inches.
            Defaults to None.
        width_in (Optional[Decimal]): The width of the material object in inches. Defaults
            to None.
        length_in (Optional[Decimal]): The length of the material object in inches. Defaults to
            None.
        wood_species (Optional[WoodSpeciesOut]): An instance of WoodSpecies. Defaults to None.
        store (Optioanl[StoreOut]): An instance of Store. Defaults to None.
        store_aisle (Optional[str]): The aisle of Store this material object is found. Defaults
            to None.
        store_bin (Optional[str]): The bin of the aisle this material object is found. Defaults to
            None.
        store_price (Optional[Decimal]): The price at the store of this material object. Defaults to
            0.00.
    """

    id: int
    material_object_name: str
    thickness_in: Decimal = Field(
        whole_digits=10, decimal_places=5, default=None
    )
    width_in: Decimal = Field(whole_digits=10, decimal_places=5, default=None)
    length_in: Decimal = Field(whole_digits=10, decimal_places=5, default=None)
    wood_species: Optional[WoodSpeciesOut] = None
    store: Optional[StoreOut] = None
    store_aisle: Optional[str] = None
    store_bin: Optional[str] = None
    store_price: Decimal = Field(
        whole_digits=10, decimal_places=2, default=0.00
    )


# The class MaterialObjectIn is a schema for validating MaterialObject information.
class MaterialObjectIn(Schema):
    """
    Schema to validate a MaterialObject

    Attributes:
        material_object_name (str): The name of the material object. Required.
        thickness_in (Optional[Decimal]): The thickness in inches. Defaults to None.
        thickness_in (Optional[Decimal]): The thickness of the material object in inches.
            Defaults to None.
        width_in (Optional[Decimal]): The width of the material object in inches. Defaults
            to None.
        length_in (Optional[Decimal]): The length of the material object in inches. Defaults
            to None.
        wood_species_id (Optional[int]): An instance of WoodSpecies.  Defaults to None.
        store_id (Optional[int]): An instance of Store.  Defaults to None.
        store_aisle (Optional[str]): The aisle of Store this material object is found. Defaults
            to None.
        store_bin (Optional[str]): The bin of the aisle this material object is found. Defaults
            to None.
        store_price (Optional[Decimal]): The price at the store of this material object. Defaults
            to None.
    """

    material_object_name: str
    thickness_in: Decimal = Field(
        whole_digits=10, decimal_places=5, default=None
    )
    width_in: Decimal = Field(whole_digits=10, decimal_places=5, default=None)
    length_in: Decimal = Field(whole_digits=10, decimal_places=5, default=None)
    wood_species_id: Optional[int]
    store_id: Optional[int] = None
    store_aisle: Optional[str] = None
    store_bin: Optional[str] = None
    store_price: Decimal = Field(
        whole_digits=10, decimal_places=2, default=0.00
    )
