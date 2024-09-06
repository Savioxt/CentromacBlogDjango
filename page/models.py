from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    capa = models.FileField()
    resumo = RichTextField() 
    conteudo = RichTextUploadingField()
    autor = models.ForeignKey(User,on_delete=models.PROTECT)
    data = models.DateField(auto_now_add=True)
    post_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.titulo
    

