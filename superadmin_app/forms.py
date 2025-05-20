from datetime import date
from django import forms

from superadmin_app.models import Task, User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    role = forms.ChoiceField(choices=[
        (2, "admin"),
        (3, "user")
    ], widget=forms.Select)
    
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password', 'role']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','assigned_to','due_date','status','completion_report','worked_hours']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['assigned_to'].queryset = User.objects.filter(role=3)

    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        if due_date and due_date < date.today():
            raise forms.ValidationError("Due date must be today or a future date.")
        return due_date
        