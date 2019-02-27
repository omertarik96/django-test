from django.db import models


class Product(models.Model):
    title       = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=1000)
    summary     = models.TextField(blank=True)
    featured    = models.BooleanField(default=False, help_text="Please check if you want your product <em>featured</em>.")

    def __str__(self):
        return self.title
