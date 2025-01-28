from django.contrib import admin
from django.contrib.admin import AdminSite
from truelines.models import RegisterTable, QuotesPost

class MyAdminSite(AdminSite):
    site_header = 'Quotes'
    site_title = 'Quotes Portal'
    index_title = 'Welcome to Quotes Admin'

admin_site = MyAdminSite(name='myadmin')
admin.site = admin_site

class RegisterTableAdmin(admin.ModelAdmin):
    list_display = ('username', 'mobileno', 'email')
    list_filter = ('username', 'email')
    search_fields = ('username', 'email')
    ordering = ('email',)
    list_per_page = 25

admin.site.register(RegisterTable, RegisterTableAdmin)

# Custom Admin for QuotesPost Model
class QuotesPostAdmin(admin.ModelAdmin):
    list_display = ('topic', 'mobileno', 'username')
    search_fields = ('username', 'topic')
    list_per_page = 25

admin.site.register(QuotesPost, QuotesPostAdmin)
