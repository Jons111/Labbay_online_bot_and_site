from django.contrib import admin

from myfiles.models import *
# Register your models here.
class AdminTur(admin.ModelAdmin):
    list_display = ['id','nomi']
class AdminMenu(admin.ModelAdmin):
    list_display = ['id','nomi']
class AdminPro(admin.ModelAdmin):
    list_display = ['id','nomi','narxi','tur','malumot','rasm1','rasm2','rasm3']

class AdminAnketa(admin.ModelAdmin):
    list_display = ['id','username','ism','tel']

class AdminSotib(admin.ModelAdmin):
    list_display = ['id','username','nomi','narxi','miqdori']
admin.site.register(Sotib_olingan_maxsulotlar,AdminSotib)
admin.site.register(Type,AdminTur)
admin.site.register(Menu,AdminMenu)
admin.site.register(Product,AdminPro)
admin.site.register(Anketa,AdminAnketa)