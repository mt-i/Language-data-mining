from django.db import models

# Create your models here.


class Phrase(models.Model):
    tshivenda = models.TextField()
    english = models.TextField()

    def __str__(self) -> str:
        return self.tshivenda


class ComplexPhrase(models.Model):
    tshivenda = models.TextField()
    english = models.TextField()

    def __str__(self) -> str:
        return self.tshivenda


class FreePull(models.Model):
    tshivenda = models.TextField()
    english = models.TextField()

    def __str__(self) -> str:
        return self.tshivenda
