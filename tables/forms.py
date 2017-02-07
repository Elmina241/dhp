from django import forms

class Delete_form(forms.Form):
    items = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,label="Удалить:")
