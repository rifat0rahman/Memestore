from django import forms
from Authentication.models import Profile


class ProfileForm(forms.ModelForm):
    picture = forms.ImageField(required=False)
    name = forms.CharField(required=False)
    bio = forms.CharField(required=False)

    class Meta:
        model = Profile
        fields = ('picture','name','bio')