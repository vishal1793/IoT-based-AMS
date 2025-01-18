from django import forms

class UIDForm(forms.Form):
    kitid = forms.CharField(label='Kit ID', max_length=100)
    loc = forms.CharField(label='Location', max_length=100)
    uid = forms.CharField(label='UID', max_length=100)  