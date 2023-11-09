from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class CustumUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        # fields = UserCreationForm.Meta.fields => fields = ('username',) 이미지는 불러오지 못함
        fields = ('username','profile_image')

class CustumAuthenticationForm(AuthenticationForm):
    pass