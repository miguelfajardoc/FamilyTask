from django.db import models
from django.contrib.auth.hashers import Argon2PasswordHasher

class CommonInfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Family(CommonInfo):
    
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class User(CommonInfo):

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, null=False)
    password = models.CharField(max_length=100)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + "-" + self.email

class Rol(CommonInfo):

    name = models.CharField(max_length=50)
    abreviation = models.CharField(max_length=10)
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.abreviation

class GeneralTask(CommonInfo):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    estimatedTime = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class AsignedTask(CommonInfo):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    generalTask = models.ForeignKey(GeneralTask, on_delete=models.CASCADE)
    asignationDate = models.DateTimeField()
    realizationTime = models.FloatField(null=True)
    state = models.IntegerField()
    
    def __str__(self):
        return self.generalTask.name + self.user.name



