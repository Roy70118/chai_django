from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to='profile_pics/', blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.username
# onetoonefield ensures that each user has one profile
# we can extends the fields user.userprofile


class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICES = [
        ('ML', 'MASALA'),
        ('GI', 'GINGER'),
        ('KL', 'KIWI'),
        ('PL', 'PLAIN'),
        ('EL', 'ELAICHI'),
    ]
    name = models.CharField(max_length=100, default=' ')
    # image = models.ImageField(upload_to='chai_images/')
    data_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(
        max_length=2, choices=CHAI_TYPE_CHOICES, default='ML')
    description = models.TextField(default=" ")
    # type is a charField that stores the type of the chaivariety (e.g-'ML','KL',..)

    def __str__(self):
        return self.name  # return a strin representation of the object


class ChaiReview(models.Model):
    chai = models.ForeignKey(
        ChaiVariety, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.username} review for {self.chai.name}'


class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varieties = models.ManyToManyField(ChaiVariety, related_name='stores')

    def __str__(self):
        return self.name

    # many to many raltionship
    # r used when yu have a models that has a mny-to-mny  relationship
    # with another model.each instances of one models can be associated
    # with multiple instances of another models


# one to one relationship
# one to one relationship are used when you have a models that has a one-to-one raltionship with another models
# each instance of one model is associated with one and only one instance of another models.each chaiVariety
class ChaiCertificate(models.Model):
    chai = models.OneToOneField(
        ChaiVariety, on_delete=models.CASCADE, related_name='certificate')
    certificate_name = models.CharField(max_length=100)
    issued_date = models.DateField(default=timezone.now)
    valid_until = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.certificate_name} for {self.chai.name}'


class ChaiProducer(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
