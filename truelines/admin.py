from django.contrib import admin

# Register your models here.
from truelines.models import RegisterTable, QuotesPost

admin.site.register(RegisterTable)
admin.site.register(QuotesPost)