from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=False)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(blank=False, null=False)
    icon = models.ImageField(upload_to="user_icons/", blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "date_of_birth"]