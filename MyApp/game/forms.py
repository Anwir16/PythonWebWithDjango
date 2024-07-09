from django import forms

class GameForm(forms.Form):
    choice_level = forms.CharField(max_length=6)
    choice_bet_point = forms.IntegerField()