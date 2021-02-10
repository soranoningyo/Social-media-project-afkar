from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from fluent_comments.models import FluentComment
# from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import Essays,Tarh,User
from django.utils.html import format_html
class EssayAdmin(admin.ModelAdmin):
    pass
admin.site.register(Essays, EssayAdmin)

class TarhAdmin(admin.ModelAdmin):
    pass
admin.site.register(Tarh, TarhAdmin)

class CommentsAdmin(admin.ModelAdmin):
    pass
admin.site.register(FluentComment, CommentsAdmin)

class UserAdmin(UserAdmin):
    # form=UserChangeForm
    # add_form=UserCreationForm
    ordering = ["email"]
    #fields=('email','first_name','last_name','groups','user_permissions','date_join','is_staff','is_admin')
    list_display = ['email','name','get_essays']

    ordering = ('email',)
    fieldsets = ((None, {'fields': ('email', 'password')}),('Personal info', {'fields': ('name','groups','joined_at','last_login',"BirthDate","gender","countries","Mbti")}),('Permissions', {'fields': ('is_superuser','is_staff')}),)
    add_fieldsets = ((None, {'fields': ('email', 'password')}),('Personal info', {'fields': ('name','groups','joined_at',"BirthDate","gender","countries","Mbti")}),('Permissions', {'fields': ('is_superuser','is_staff')}),)

    def get_essays(self,obj):
        return obj.name
admin.site.register(User, UserAdmin)
# class UserProfileAdmin(admin.ModelAdmin):
#     readonly_fields = ("user",)
# admin.site.register(UserProfile,UserProfileAdmin)
# class UserProfileAdmin(admin.ModelAdmin):
#     # list_display = ["user","image"]
#     def image_tag(self, obj):
#         return format_html('<img src="{}" />'.format(obj.image.url))

#     image_tag.short_description = 'Image'

#     list_display = ['image_tag',]
# admin.site.register(UserProfile,UserProfileAdmin)