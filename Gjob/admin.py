from django.contrib import admin
from Gjob.models import BookPost, LatestGovJobPost, GjobPageContact

# Register your models here.
# admin.site.register(GovJobPost)

admin.site.register(BookPost)
admin.site.register(GjobPageContact)

@admin.register(LatestGovJobPost)
class LatestGovJobPostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinject.js',)

