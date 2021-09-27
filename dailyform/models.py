from django.db import models
from datetime import datetime,date
# Create your models here.
class DailyFormModel(models.Model):
    user=models.ForeignKey("auth.user", null=True, blank=False, on_delete=models.CASCADE)
    SELECT=(('1','1'),('2','2'),('3','3'))
    sleeping=models.CharField(choices=SELECT, max_length=3, null=True, blank=False)
    drinkingwater=models.CharField(choices=SELECT, max_length=3, null=True, blank=False)
    steps=models.CharField(choices=SELECT, max_length=3, null=True, blank=False)
    sports=models.CharField(choices=SELECT, max_length=3, null=True, blank=False)
    eating=models.CharField(choices=SELECT, max_length=3, null=True, blank=False)
    study=models.CharField(choices=SELECT, max_length=3, null=True, blank=False)
    created_date=models.DateField(auto_now_add=True, null=True, blank=False)
    class Meta:
        verbose_name_plural="Günlük Kayıt Formu"
    def __str__(self):
        return "{}-{}-{}-{}-{}-{}-{}-{}".format(self.sleeping, self.drinkingwater, self.steps, self.sports, self.eating, self.study, self.created_date, self.user)



class SaveQuestion(models.Model):
    user=models.ForeignKey("auth.user", null=True, blank=False, on_delete=models.CASCADE)
    message=models.TextField(null=True, blank=False, max_length=300)
    class Meta:
        verbose_name_plural="Kullanıcının Eklenmesini İstediği Sorular"
    def __str__(self):
        return "{}".format(self.user)

class LikeApp(models.Model):
    user=models.ForeignKey("auth.user", null=True, blank=False, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural="People Who liked the Site"
    def __str__(self):
        return "{}".format(self.user)