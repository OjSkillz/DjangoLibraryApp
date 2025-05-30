from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = " "
    summary = models.TextField()
    isbn = models.CharField(max_length=11, unique=True)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    language = models.ForeignKey('Language', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Genre(models.Model):
    GENRE_CHOICES = (
        ("R", "ROMANCE"),
        ("C", "COMEDY"),
        ("P", "POLITICS"),
        ("F", "FINANCE"),
    )
    name = models.CharField(max_length=1, choices=GENRE_CHOICES, default="F")
    def __str__(self):
        return self.name


class Language(models.Model):
    LANGUAGE_CHOICES = (
        ("EN", "English"),
        ("FR", "French"),
        ("CN", "Chinese"),
        ("YR", "Yoruba"),
        ("HS", "Hausa"),
    )
    name = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default="EN")
    def __str__(self):
        return self.name