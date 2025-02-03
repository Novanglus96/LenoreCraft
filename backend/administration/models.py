from django.db import models

# Create your models here.


class SingletonModel(models.Model):
    """
    A Singleton model that ensures there is only one instance
    of this model that can not be deleted.

    """

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """
        Overrides save for model to ensure there is only ever 1 instance.

        Raises:
            ValidationError (String): Raises an error if there is already an instance
                of this model.

        Returns:
            self (Model): Returns itself on save.
        """
        if not self.pk and self.__class__.objects.exists():
            raise ValidationError("There is already one instance of this model")
        return super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """
        Overrides delete, not allowing deletions.

        Raises:
            ValidationError (String): On deletion attemp, returns an error not allowing
                deletions.
        """
        raise ValidationError("You cannot delete this object")


class Version(SingletonModel):
    """
    Model representing app version.

    Args:
        version_number (CharField): The current version of the app.
    """

    version_number = models.CharField(max_length=10)

    def __str__(self):
        """
        Returns:
            (String): The version number of the app.
        """
        return self.version_number
