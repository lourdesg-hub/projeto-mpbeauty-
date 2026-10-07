from django import forms

from .models import (
    Appointment,
    ProductReview,
    ProfessionalReview,
)


class FormularioAvaliacaoProduto(
    forms.ModelForm
):

    class Meta:
        model = ProductReview

        fields = [
            'rating',
            'comment',
        ]

        labels = {
            'rating': 'Nota',
            'comment': 'Comentário',
        }

        widgets = {
            'rating': forms.NumberInput(
                attrs={
                    'min': 0,
                    'max': 5,
                }
            ),

            'comment': forms.Textarea(
                attrs={
                    'placeholder':
                        'Conte o que achou do produto...',
                    'rows': 4,
                }
            ),
        }


class FormularioAvaliacaoProfissional(
    forms.ModelForm
):

    class Meta:
        model = ProfessionalReview

        fields = [
            'rating',
            'comment',
        ]

        labels = {
            'rating': 'Nota',
            'comment': 'Comentário',
        }

        widgets = {
            'rating': forms.NumberInput(
                attrs={
                    'min': 0,
                    'max': 5,
                }
            ),

            'comment': forms.Textarea(
                attrs={
                    'placeholder':
                        'Conte como foi seu atendimento...',
                    'rows': 4,
                }
            ),
        }


class FormularioAgendamento(forms.ModelForm):

    class Meta:
        model = Appointment

        fields = [
            'service',
            'location',
            'date',
            'time',
            'client_name',
            'whatsapp',
        ]

        labels = {
            'service': 'Serviço',
            'location': 'Local do atendimento',
            'date': 'Data',
            'time': 'Horário',
            'client_name': 'Nome do cliente',
            'whatsapp': 'WhatsApp',
        }

        widgets = {
            'date': forms.DateInput(
                attrs={
                    'type': 'date',
                }
            ),

            'time': forms.TimeInput(
                attrs={
                    'type': 'time',
                }
            ),

            'client_name': forms.TextInput(
                attrs={
                    'placeholder':
                        'Digite seu nome completo',
                }
            ),

            'whatsapp': forms.TextInput(
                attrs={
                    'placeholder':
                        '(84) 99999-9999',
                }
            ),
        }