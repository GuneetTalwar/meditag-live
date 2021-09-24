from django import forms
from django.forms import ModelForm
#from django.contrib.auth.models import User
from .models import UserProfile,UploadDocument,DeliverSticker

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'date'

class addUserInfo(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(addUserInfo, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = UserProfile
        exclude = ('user','path','created_at')
        widgets = {
            'dob': DateInput(),
        }


class UploadDocumentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UploadDocumentForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = UploadDocument
        exclude = ('user',)

class deliverStickerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(deliverStickerForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = DeliverSticker
        exclude = ('user_profile','path',)

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']
