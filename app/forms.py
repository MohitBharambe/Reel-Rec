from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import  User
from .models import Contact
import pandas as pd
import os

top_movies_dataset = os.path.join(os.path.dirname(__file__), '..', 'datasets', 'topmovies.csv')  # Top movies dataset
top_movies_df = pd.read_csv(top_movies_dataset)
movie_choices = [(title, title) for title in top_movies_df['title'].to_list()]


# Custom User Registration Form
class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Movie Selection Form
class MovieForm(forms.Form):
    titles = forms.MultipleChoiceField(
        choices=movie_choices,
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    
# Contact Form
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']