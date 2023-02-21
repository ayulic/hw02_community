from django.contrib import admin

# Register your models here.

from .models import Post, Group



class PostAdmin(admin.ModelAdmin):
    # fields for admin panel
    list_display = (
        'pk', 
        'text', 
        'pub_date', 
        'author',
        'group', 
        )

    list_editable = ('group',)
    # search interface by posts text
    search_fields = ('text',)
    # filter by date
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'

admin.site.register(Post, PostAdmin)
admin.site.register(Group)