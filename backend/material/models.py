from django.db import models
from project.models import Project

# Create your models here.


class MaterialStatus(models.Model):
    """
    Model representing a status for materials.

    Fields:
        - material_status (CharField): The text status of a material.
    """

    material_status = models.CharField(max_length=254, unique=True)

    class Meta:
        verbose_name_plural = "Material statuses"

    def __str__(self):
        """
        Returns:
            (String): The Material Status
        """
        return self.material_status


class WoodSpecies(models.Model):
    """
    Model representing a wood species for materials.

    Fields:
        - wood_species_name (CharField): The name of a species of wood.
    """

    wood_species_name = models.CharField(max_length=254, unique=True)

    class Meta:
        verbose_name_plural = "Wood species"

    def __str__(self):
        """
        Returns:
            (String): The Wood Species Name
        """
        return self.wood_species_name


class Store(models.Model):
    """
    Model representing a store

    Fields:
        - store_name (CharField): The name of a store.
    """

    store_name = models.CharField(max_length=254, unique=True)

    def __str__(self):
        """
        Returns:
            (String): The Store Name
        """
        return self.store_name


class MaterialObject(models.Model):
    """
    Model representing a material object.

    Fields:
        - material_object_name (CharField): The name of a material object.
        - thickness_in (DecimalField): The thickness of the object
        - width_in (DecimalField): The width of the object
        - length_in (DecimalField): The length of the object
        - wood_species (ForeignKey): A refernce to a Wood Species object
        - store (ForeignKey): A refrence to a Store
        - store_aisle (CharField): The aisle of Store this material object can be
        found.
        - store_bin (CharField): The bin of the aisle.
        - store_price (DecimalField): The price of this material object.
    """

    material_object_name = models.CharField(max_length=254, unique=True)
    thickness_in = models.DecimalField(max_digits=10, decimal_places=5)
    width_in = models.DecimalField(max_digits=10, decimal_places=5)
    length_in = models.DecimalField(max_digits=10, decimal_places=5)
    wood_species = models.ForeignKey(
        WoodSpecies,
        null=True,
        on_delete=models.SET_NULL,
        blank=True,
        default=None,
    )
    store = models.ForeignKey(
        Store, null=True, on_delete=models.SET_NULL, blank=True, default=None
    )
    store_aisle = models.CharField(max_length=254)
    store_bin = models.CharField(max_length=254)
    store_price = models.DecimalField(
        max_digits=12, decimal_places=2, default=0.00, null=True
    )

    def __str__(self):
        """
        Returns:
            (String): The Material Object Name
        """
        return self.material_object_name


class Material(models.Model):
    """
    Model representing a material.

    Fields:
        - material_object (ForeignKey): A reference to a Material Object
        - quantity (IntegerField): The quantity of material objects
        - material_status (ForeignKey): A reference to a Material Status
        - project (ForeignKey): A refrence to a Project
    """

    material_object = models.ForeignKey(
        MaterialObject, on_delete=models.CASCADE
    )
    quantity = models.IntegerField()
    material_status = models.ForeignKey(
        MaterialStatus,
        null=True,
        on_delete=models.SET_NULL,
        blank=True,
        default=None,
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        """
        Returns:
            (String): The Material Object Name
        """
        return self.material_object.material_object_name
