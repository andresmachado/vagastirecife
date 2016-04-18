#!-*- coding: utf8 -*-

from django import forms

from .models import Job


class CreateJobForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CreateJobForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "Título da vaga"
        self.fields['company'].label = "Empresa"
        self.fields['url'].label = "Url da vaga"
        self.fields['site'].label = "Website"
        self.fields['email'].label = "Email para contato"
        self.fields['category'].label = "Contratação"
        self.fields['job_type'].label = "Modalidade"
        self.fields['salary'].label = "Salário"
        self.fields['description'].label = "Descrição da vaga"
        self.fields['about'].label = "Sobre a empresa"
        self.fields['skills'].label = "Habilidades necessárias"

    class Meta:
        model = Job
        fields = ('title', 'company', 'url', 'site', 'email', 'category', 'job_type', 'salary', 'description', 'about', 'skills',)
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Digite o título da vaga'}),
            'company': forms.TextInput(attrs={'placeholder': 'Digite o nome da empresa'}),
            'url': forms.TextInput(attrs={'placeholder': 'Digite aqui a url da vaga para o processo de seleção', 'required': False}),
            'site': forms.URLInput(attrs={'placeholder': 'Digite o endereço web da empresa', 'required': False}),
            'email': forms.EmailInput(attrs={'placeholder': 'Digite o endereço de email para contato'}),
            'category': forms.Select(),
            'job_type': forms.Select(),
            'salary': forms.NumberInput(attrs={'required': True}),
            'description': forms.Textarea(attrs={'placeholder': 'Digite a descrição da vaga, o mais detalhado possivel.'}),
            'about': forms.Textarea(attrs={'placeholder': 'Fale um pouco da empresa e sua cultura.'}),
            'skills': forms.Textarea(attrs={'placeholder': 'Descreva detalhadamente o que é necessário para se candaditar a vaga.'})
        }
