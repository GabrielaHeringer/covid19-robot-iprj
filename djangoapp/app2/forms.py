# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from app2.models import Profile

class UserModelForm(forms.ModelForm):
	User._meta.get_field('first_name').blank = False
	User._meta.get_field('last_name').blank = False
	User._meta.get_field('email').blank = False

	confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'maxlenght': 255}))
	
	class Meta:
		model = User
		fields = ['password', 'username', 'first_name', 'last_name','email']
		widgets = {
			'password': forms.PasswordInput(attrs={'class': 'form-control', 'minlenght': 8, 'maxlenght': 255}),
			'username': forms.TextInput(attrs={'class': 'form-control', 'maxlenght': 255}),
			'first_name': forms.TextInput(attrs={'class': 'form-control', 'maxlenght': 255}),
			'last_name': forms.TextInput(attrs={'class': 'form-control', 'maxlenght': 255}),
			'email': forms.EmailInput(attrs={'class': 'form-control', 'maxlenght': 255}),
		}

	def save(self, commit=True):
		user = super(UserModelForm, self).save(commit=False)
		user.set_password(self.cleaned_data['password'])
		if commit:
			user.save()

		return user
	
	def clean(self):
		cleaned_data = super(UserModelForm, self).clean()
		password = cleaned_data.get("password")
		confirm_password = cleaned_data.get("confirm_password")

		if password != confirm_password:
			raise forms.ValidationError("Senhas incompatíveis.")


class ProfileForm(forms.ModelForm):
        Profile._meta.get_field('pais').blank = True

        class Meta:
                model = Profile
                fields = ['telefone', 'profissao', 'pais', 'organizacao']
                widgets = {
                        #'telefone': forms.TextInput(attrs={'class': 'form-control', 'pattern': '\[0-9]{2}\ [0-9]{4,6}-[0-9]{3,4}$', 'OnKeyPress': 'formatar("###########-####", this)', 'maxlength': 19}),
                        'profissao': forms.TextInput(attrs={'class': 'form-control', 'maxlenght': 255}),
                        'pais': forms.TextInput(attrs={'class': 'form-control', 'maxlenght': 255}),
                        'telefone': forms.TextInput(attrs={'class': 'form-control', 'OnKeyPress': 'formatar("## \#####-####", this)', 'maxlenght':19}),
                        'organizacao': forms.TextInput(attrs={'class': 'form-control', 'maxlenght': 255}),
                                        }
