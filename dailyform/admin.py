from django.contrib import admin
from . models import DailyFormModel,SaveQuestion,LikeApp
# Register your models here.

admin.site.register(DailyFormModel)
admin.site.register(SaveQuestion)
admin.site.register(LikeApp)
