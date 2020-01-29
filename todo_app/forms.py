from django import forms


class NewTodo(forms.Form):
    task = forms.CharField(min_length=3, max_length=60, widget=forms.TextInput(attrs={"name": "task"}))
