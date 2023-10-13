from django.db import models
from uuid import uuid4

# Create your models here.

class Books(models.Model):
    id_book = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255) # nome do livro
    authot = models.CharField(max_length=255) # autor do livro
    release_year = models.IntegerField() # ano de lançamento
    state = models.CharField(max_length=50) #novo ou usado
    pages = models.IntegerField() # quantidade de páginas
    publishing_company = models.CharField(max_length=255) # editora
    create_at = models.DateField(auto_now_add=True) #quando foi criado