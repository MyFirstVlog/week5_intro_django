from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
# Solo agregamos clase meta porque debemos de decirte al .py como queremos que se comporten los formularios
    class Meta:
        model = Comment

        fields = ('text', ) #el unico dato ecesario por llenar por parte del usuario, se pone una tupla