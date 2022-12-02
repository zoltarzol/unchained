from django import forms
from . import models

class ChatBotForm(forms.Form):
    name = forms.CharField(
        label='Saisis ton prénom',
        max_length=30)

    question = forms.CharField(
        label='Pose ta question',
        max_length=150)

    response = forms.Textarea()

class InputForm(forms.ModelForm):
    class Meta:
        model = models.InputModel
        fields = "__all__"
        labels = {
            "text_msg" : "Your message:"
        }