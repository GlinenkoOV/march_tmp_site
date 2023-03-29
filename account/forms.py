from django import forms
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'required': "", }))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
         'required': "", }))




    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user or not user.check_password(password):
                raise forms.ValidationError('Логін фбо пароль не співпадають')
        return super().clean() # Якщо не потрапляємо в exeption викликаємо метод clean базового класу






class RegistrationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', )

    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
                                                        'class': "form-control shadow-0 px-0 border-0 border-bottom",
                                                        'type': "text",
                                                        'required': "",}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
                                                        'class': "form-control shadow-0 px-0 border-0 border-bottom",
                                                        'type': "text",
                                                        'required': "",}))
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
                                                        'class': "form-control shadow-0 px-0 border-0 border-bottom",
                                                        'type': "text",
                                                        'required': "",}))

    def clean_password2(self):
        if self.cleaned_data['password'] == self.cleaned_data['password2']:
            return self.cleaned_data['password2']
        raise forms.ValidationError('Паролі не співпадають')
