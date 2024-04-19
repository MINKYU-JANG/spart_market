from django.contrib.auth.forms import UserChangeForm
from accounts.models import User


class RegisterForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username',)
