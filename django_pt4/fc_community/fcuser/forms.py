from django import forms
from django.contrib.auth.hashers import check_password
from .models import Fcuser

class LoginForm(forms.Form):
    username = forms.CharField(max_length=32, label="사용자 이름", error_messages={'required':"아이디를 입력해주세요."})
    password = forms.CharField(widget=forms.PasswordInput, label="비밀번호", error_messages={'required':'비밀번호를 입력해주세요.'})

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            try:
                fcuser = Fcuser.objects.get(username=username)
            except Fcuser.DoesNotExist:
                self.add_error('username', "아이디가 없습니다")
                return
            if not (check_password(password, fcuser.password)):
                self.add_error('password', "비밀번호를 틀렸습니다.")
            else:
                self.user_id = fcuser.id
        