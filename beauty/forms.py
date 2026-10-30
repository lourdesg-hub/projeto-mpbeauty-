
from django import forms
from .models import (
    Appointment,
    ProductReview,
    ProfessionalReview,
)


class FormularioAvaliacaoProduto(forms.ModelForm):

    class Meta:
        model = ProductReview
        fields = ["rating", "comment"]

        labels = {
            "rating": "Nota de 0 a 5",
            "comment": "Comentário",
        }

        widgets = {
            "rating": forms.NumberInput(attrs={
                "min": 0,
                "max": 5,
                "step": 1,
            }),
            "comment": forms.Textarea(attrs={
                "rows": 4,
                "placeholder": "Conte o que achou do produto...",
            }),
        }


class FormularioAvaliacaoProfissional(forms.ModelForm):

    class Meta:
        model = ProfessionalReview
        fields = ["rating", "comment"]

        labels = {
            "rating": "Nota de 0 a 5",
            "comment": "Comentário",
        }

        widgets = {
            "rating": forms.NumberInput(attrs={
                "min": 0,
                "max": 5,
                "step": 1,
            }),
            "comment": forms.Textarea(attrs={
                "rows": 4,
                "placeholder": "Conte como foi seu atendimento...",
            }),
        }


class FormularioAgendamento(forms.ModelForm):

    class Meta:
        model = Appointment

        fields = [
            "service",
            "location",
            "date",
            "time",
            "client_name",
            "whatsapp",
        ]

        labels = {
            "service": "Serviço desejado",
            "location": "Local do atendimento",
            "date": "Data",
            "time": "Horário",
            "client_name": "Nome completo",
            "whatsapp": "WhatsApp",
        }

        widgets = {
            "date": forms.DateInput(attrs={
                "type": "date",
            }),
            "time": forms.TimeInput(attrs={
                "type": "time",
            }),
            "client_name": forms.TextInput(attrs={
                "placeholder": "Digite seu nome completo",
            }),
            "whatsapp": forms.TextInput(attrs={
                "placeholder": "(84) 99999-9999",
            }),
        }
