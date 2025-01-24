from django import forms
from . import models, parser_book


class BookForm(forms.ModelForm):
    MEDIA_CHOICES = (
        ('mybook', 'mybook'),
    )