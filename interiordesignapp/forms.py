from django import forms

from .models import PostIndex,PostProject,JobOpening

class PostIndexForm(forms.ModelForm):
        class Meta:
            model=PostIndex
            fields='__all__'


class PostProjectForm(forms.ModelForm):
    class Meta:
        model=PostProject
        fields='__all__'
        
        
        


class JobOpeningForm(forms.ModelForm):
    class Meta:
        model = JobOpening
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'requirements': forms.Textarea(attrs={'rows': 4}),
        }


from django.core.validators import RegexValidator
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()    
    phone = forms.CharField(
        max_length=15, 
        validators=[RegexValidator(
            regex=r'^\+?1?\d{9,15}$', 
            message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
        )]
    )
    message = forms.CharField(widget=forms.Textarea)