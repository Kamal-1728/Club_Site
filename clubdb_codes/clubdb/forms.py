from django import forms
from clubdb.models import club
from clubdb.models import events
from clubdb.models import club_address
class clubforms(forms.ModelForm):
    class Meta:
        model = club
        fields = "__all__"

class eventforms(forms.ModelForm):
    class Meta:
        model = events
        fields = "__all__"

class clubaddressforms(forms.ModelForm):
    class Meta:
        model = club_address
        fields = "__all__"  