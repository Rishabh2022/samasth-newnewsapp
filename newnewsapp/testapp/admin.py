from django.contrib import admin
from testapp.models import signup,Bookmark
# Register your models here.
class signadmin(admin.ModelAdmin):
    list_display=['name','username','mobile','email','password']
admin.site.register(signup,signadmin)

class Bookmarknews(admin.ModelAdmin):
    list_display=["sno","user","title","image","readmore"]
admin.site.register(Bookmark,Bookmarknews)
