from django import forms
from .models import Comments


class EmailSendForm(forms.Form):
    name = forms.CharField(max_length=120, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
        }
    ))
    to = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
        }
    ))
    comments = forms.CharField(required=False, widget=forms.Textarea(
        attrs={
            'class': 'form-control',
        }
    ))


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['name', 'email', 'body']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'body': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows':5

                }
            )
        }
