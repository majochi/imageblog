from django.contrib import admin
from core.models import Site, Article, Gallery, GalImage

admin.site.register(Site)
admin.site.register(Article)
admin.site.register(Gallery)
admin.site.register(GalImage)
