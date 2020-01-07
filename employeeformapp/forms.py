from django import forms
class employeeforms(forms.Form):
    eno=forms.IntegerField(
        label='enter your roll no:',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'your roll number'
            }
        )
    )
    ename=forms.CharField(
        label='enter your name:',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your name'
            }
        )
    )
    eposition = forms.CharField(
        label='enter your position:',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your position'
            }
        )

    )
    eaddress = forms.CharField(
        label='enter your address:',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'your address'
            }
        )
    )
    eproject = forms.CharField(
        label='enter your project:',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your project'
            }
        )
    )
    esalary = forms.FloatField(
        label='enter your salary:',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your salary'
            }
        )
    )
    eusername = forms.CharField(
        label='enter your user name:',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your user name'
            }
        )
    )
    epassword = forms.CharField(
        label='enter your password:',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your password'
            }
        )
    )
    eemail = forms.EmailField(
        label='enter your email:',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your email'
            }
        )
    )
    ebalaji = forms.IntegerField(
        label='enter your balaji:',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your salary'
            }
        )
    )

