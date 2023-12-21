from django.db import models

# Create your models here.
class Persons(models.Model):
    Personsid = models.AutoField(primary_key=True)
    LastName = models.CharField(max_length=255,null=False)
    FristName = models.CharField(max_length=225,null=False)
    Age = models.IntegerField(null=True)

    def __str__(self):
        return self.Personsid

    class Meta:
        db_table = "persons"





