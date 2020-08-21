from django import forms
from . import models

class ToDoForm(forms.ModelForm):
    class Meta():
        model = models.ToDo
        fields = ('task',)

        widgets = {
            'task':forms.TextInput(attrs={'autocomplete':'off',
                                            'class':'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(ToDoForm, self).__init__(*args, **kwargs)
        self.label_suffix = ''
