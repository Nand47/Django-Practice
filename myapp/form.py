from django import forms
class inputuser(from.forms):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    phone = forms.IntegerField()

    