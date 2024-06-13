from django.db import models

# Create your models here.
class Comment(models.Model):
    id_comment = models.AutoField(primary_key=True)
    id_publicacion = models.IntegerField()
    id_usuario = models.IntegerField()
    content = models.TextField()
    creation_date = models.DateTimeField()
