from django import forms
from cats.models import Breed
class MakeForm(forms.ModelForm):
    class Meta:
        model = Breed
        fields = '__all__'
