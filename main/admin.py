from django.contrib import admin
from .models import *
from django.views.decorators.csrf import csrf_exempt
# Register your models here.
admin.site.register(Home)
admin.site.register(Portfolio)


class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 1

class SocialInLine(admin.TabularInline):
    model = Social
    extra = 1

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [ProfileInline,SocialInLine]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','message']


class SkillInline(admin.TabularInline):
    model = Skills
    extra = 2


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [SkillInline]