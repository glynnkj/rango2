from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile
# Register models here.

class PageAdmin(admin.ModelAdmin):
	list_display = ('title', 'category','url') 
admin.site.register(Page, PageAdmin)

# Add in this class to customise the admin Interface.
class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}
  

admin.site.register(Category, CategoryAdmin)
admin.site.register(UserProfile)
