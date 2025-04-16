from django.db import models

class Words(models.Model):
    word = models.CharField(max_length=100)
    definition = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.word}-{self.definition}"
