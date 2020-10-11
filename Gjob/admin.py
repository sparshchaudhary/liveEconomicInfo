from django.contrib import admin
from Gjob.models import GovJobPost, BookPost

# Register your models here.
# admin.site.register(GovJobPost)

admin.site.register(BookPost)

@admin.register(GovJobPost)
class GovJobPostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinject.js',)

