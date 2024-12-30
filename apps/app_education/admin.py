from django.contrib import admin
from .models import IspKeywords

# Register your models here.
@admin.register(IspKeywords)
class IspKeywordsAdmin(admin.ModelAdmin):
    list_display = (
        'term',
        'searches',
        'orders',
        'sales'
    )