from django import forms
from . models import DailyFormModel,SaveQuestion
from datetime import datetime
class DailyFormModelForm(forms.ModelForm):
    sleeping = forms.ChoiceField(required=True, choices=DailyFormModel.SELECT, widget=forms.RadioSelect())
    drinkingwater = forms.ChoiceField(required=True, choices=DailyFormModel.SELECT, widget=forms.RadioSelect())
    steps = forms.ChoiceField(required=True, choices=DailyFormModel.SELECT, widget=forms.RadioSelect())
    sports = forms.ChoiceField(required=True, choices=DailyFormModel.SELECT, widget=forms.RadioSelect())
    eating= forms.ChoiceField(required=True, choices=DailyFormModel.SELECT, widget=forms.RadioSelect())
    study = forms.ChoiceField(required=True, choices=DailyFormModel.SELECT, widget=forms.RadioSelect())
    class Meta:
        model=DailyFormModel
        fields=['sleeping', 'drinkingwater', 'steps', 'sports', 'eating', 'study']



class SaveQuestionForm(forms.ModelForm):
    message = forms.CharField(max_length=300, widget=forms.Textarea(attrs={"class":"form-control2", 'rows':2,
                'cols':2}))
    class Meta:
        model=SaveQuestion
        fields=['message']