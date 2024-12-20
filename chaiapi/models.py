from django.db import models
from django.utils import timezone

# Create your models here.


class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICES = [
        ('ML', 'MASALA'),
        ('GI', 'GINGER'),
        ('KL', 'KIWI'),
        ('PL', 'PLAIN'),
        ('EL', 'ELAICHI'),
    ]
    name = models.CharField(max_length=100),
    image = models.ImageField(upload_to='chais/')
    data_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(
        max_length=2, choices=CHAI_TYPE_CHOICES, default='ML')
    # type is a charField that stores the type of the chaivariety (e.g-'ML','KL',..)

    def __str__(self):
        return self.name  # return a strin representation of the object
