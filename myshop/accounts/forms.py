from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms



class SignUpForm(UserCreationForm):
    # dept_choices = (
    #     ("cs", "Computer"),
    #     ("it", "IT"),
    # )
    # department = forms.ChoiceField(choices=dept_choices)


# f = UserCreationForm()
# f.save()
    pass


class LoginForm(AuthenticationForm):
    pass