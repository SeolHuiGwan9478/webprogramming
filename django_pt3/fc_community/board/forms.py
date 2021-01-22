from django import forms
from django.contrib.auth.hashers import check_password

class Boardform(forms.Form):
    title = forms.CharField(max_length=128, label="제목", error_messages={'required':"제목을 입력해주세요."})
    contents = forms.CharField(widget=forms.Textarea, label="내용", error_messages={'required':'내용을 입력해주세요.'})


        