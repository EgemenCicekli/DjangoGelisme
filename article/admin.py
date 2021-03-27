from django.contrib import admin
from .models import Article,Comment

# Register your models here.

admin.site.register(Comment)

#Modeli adminde görünüm özelleştirme
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","author","created_date"]
    #Basıldığı zaman siteye gitme
    list_display_links = ["title"]
    #Arama çubuğu ile arattırma
    search_fields = ["title"]
    #Filtreleme
    list_filter = ["created_date"]
    class Meta:
        model = Article

        