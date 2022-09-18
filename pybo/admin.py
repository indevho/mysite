from django.contrib import admin
from .models import Question

# ver 1 admin.site.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Question, QuestionAdmin)
# Register your models here.
