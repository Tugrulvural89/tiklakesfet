from django.contrib import admin
from .models import Image, Tag, Post, Categories, Posten, language



admin.site.register(Post)
admin.site.register(Image)
admin.site.register(Tag)
admin.site.register(Categories)
admin.site.register(Posten)
admin.site.register(language)
