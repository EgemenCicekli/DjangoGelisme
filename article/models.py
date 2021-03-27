from django.db import models
from ckeditor.fields import RichTextField

#Makaleler tablosu
class Article(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,verbose_name="Yazar")
    title =  models.CharField(max_length=50,verbose_name="Başlık")
    content = RichTextField(verbose_name="Metin")
    created_date = models.DateTimeField(auto_now_add=True)
    article_image = models.FileField(blank=True,null=True,verbose_name="Görsel")
    #Admindeki arayüz için
    def __str__(self):
        return self.title
class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="Makale",related_name="comments")
    comment_author = models.CharField(max_length=30,verbose_name="İsim")
    comment_content = models.CharField(max_length=70,verbose_name="Yorum")
    def __str__(self):
        return self.comment_content