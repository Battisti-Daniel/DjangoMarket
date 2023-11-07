from django.db import models
import uuid

class MarketRole(models.Model):
    
    id = models.UUIDField(
        primary_key = True, 
        default = uuid.uuid4, 
        editable = False,
    )
    name = models.CharField(
        max_length = 30,
        blank = False,
        null = False,
    )
    accessibility = models.PositiveIntegerField(
        default=1,
        choices=((i,i) for i in range(1, 11))
        )
    
    def __str__(self):
        return f'{self.name}'
    
class User(models.Model):
        
    id = models.UUIDField(
        primary_key = True, 
        default = uuid.uuid4, 
        editable = False,
    )
    name = models.CharField(
        max_length = 100,
        blank = False,
        null = False,
    )
    lastName = models.CharField(
        max_length = 150,
        blank = False,
        null = False,
    )
    cpf = models.CharField(
        max_length = 11,
        blank = False,
        null = False,
    )
    born = models.DateField(
        null = False,
        blank = False,
    )
    registeredDate = models.DateField(
        auto_now_add=True,
        blank=True
    )
    role = models.ForeignKey(
        to = MarketRole,
        on_delete = models.PROTECT
    )
    
    def __str__(self):
        return f'{self.name} {self.lastName} - {self.role}'