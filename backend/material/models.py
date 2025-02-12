from django.db import models
from project.models import Project

# Create your models here.


class MaterialStatus(models.Model):
    """
    Model representing a status for materials.

    Attributes:
        material_status (CharField): The text status of a material. Required.
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

    Attributes:
        wood_species_name (CharField): The name of a species of wood. Required.
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

    Attributes:
        store_name (CharField): The name of a store. Required. Unique.
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

    Attributes:
        material_object_name (CharField): The name of a material object. Required.
        thickness_in (Optional[DecimalField]): The thickness of the object. Defaults to None.
        width_in (Optional[DecimalField]): The width of the object. Defaults to None.
        length_in (Optional[DecimalField]): The length of the object. Defaults to None.
        wood_species (Optional[ForeignKey]): A refernce to a Wood Species object. Defaults to None.
        store (Optional[ForeignKey]): A refrence to a Store. Defaults to None.
        store_aisle (Optional[CharField]): The aisle of Store this material object can be
        found. Defaults to None.
        store_bin (Optional[CharField]): The bin of the aisle. Defaults to None.
        store_price (Optional[DecimalField]): The price of this material object. Defaults to 0.00.
        material_object_full_name (CharField): The full name of the object. Unique. Defaults to None.
            Limit 512. On save, set to dimensions + wood species name + material_object_name
    """

    material_object_name = models.CharField(max_length=254)
    thickness_in = models.DecimalField(
        max_digits=10, decimal_places=5, null=True, blank=True, default=None
    )
    width_in = models.DecimalField(
        max_digits=10, decimal_places=5, null=True, blank=True, default=None
    )
    length_in = models.DecimalField(
        max_digits=10, decimal_places=5, null=True, blank=True, default=None
    )
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
    store_aisle = models.CharField(
        max_length=254, null=True, blank=True, default=None
    )
    store_bin = models.CharField(
        max_length=254, null=True, blank=True, default=None
    )
    store_price = models.DecimalField(
        max_digits=12, decimal_places=2, default=0.00, blank=True, null=True
    )
    material_object_full_name = models.CharField(
        max_length=512, unique=True, null=True, blank=True, default=None
    )

    def save(self, *args, **kwargs):
        """
        Override save method to compute material_full_name before saving.
        """
        dimensions = "x".join(
            str(value)
            for value in [self.thickness_in, self.width_in, self.length_in]
            if value is not None
        )
        wood_species_name = (
            self.wood_species.wood_species_name if self.wood_species else ""
        )
        components = filter(
            None, [dimensions, wood_species_name, self.material_object_name]
        )
        self.material_object_full_name = " ".join(components)
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns:
            (String): The Material Object Name
        """
        return self.material_object_full_name


class Material(models.Model):
    """
    Model representing a material.

    Attributes:
        material_object (MaterialObject): A reference to a Material Object. Required.
        quantity (IntegerField): The quantity of material objects. Required.
        material_status (Optional[ForeignKey]): A reference to a Material Status.
            Defaults to None.
        project (Optional[ForeignKey]): A refrence to a Project. Defaults to None.
    """

    material_object = models.ForeignKey(
        MaterialObject, on_delete=models.CASCADE
    )
    quantity = models.IntegerField(default=1)
    material_status = models.ForeignKey(
        MaterialStatus,
        null=True,
        on_delete=models.SET_NULL,
        blank=True,
        default=None,
    )
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, null=True, blank=True, default=None
    )

    def __str__(self):
        """
        Returns:
            (String): The Material Object Name
        """
        return self.material_object.material_object_name
