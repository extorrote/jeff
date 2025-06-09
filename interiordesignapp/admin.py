from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import PostIndex,PostProject, JobOpening

@admin.register(PostIndex)
class PostIndexAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(PostProject)
class PostProjectAdmin(admin.ModelAdmin):
    list_display = ('title',)
    
    
@admin.register( JobOpening)
class  JobOpeningAdmin(admin.ModelAdmin):
    list_display = ('title',)