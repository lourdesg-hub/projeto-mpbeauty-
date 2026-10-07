from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import request
from django.shortcuts import redirect, render

from .forms import (
    FormularioAgendamento,
    FormularioAvaliacaoProduto,
    FormularioAvaliacaoProfissional,
)

from .models import (
    Appointment,
    Package,
    Product,
    ProductReview,
    Professional,
    ProfessionalReview,
    PurchaseItem,
)


def inicio(request):

    produtos = Product.objects.filter(
        active=True
    )[:6]

    profissionais = Professional.objects.all()[:4]

    pacotes = Package.objects.filter(
        active=True
    )[:3]

    return render(
        request,
        'beauty/inicio.html',
        {
            'produtos': produtos,
            'profissionais': profissionais,
            'pacotes': pacotes,
        }
    )


def produtos(request):

    categoria = request.GET.get(
        'categoria'
    )

    lista_produtos = Product.objects.filter(
        active=True
    )

    if categoria:
        lista_produtos = lista_produtos.filter(
            category=categoria
        )

    return render(
        request,
        'beauty/produtos.html',
        {
            'produtos': lista_produtos,
            'categoria': categoria,
        }
    )


def produtos_detalhes(request, produto_id):

    produto = Product.objects.get(
        id=produto_id
    )

    avaliacoes = ProductReview.objects.filter(
        product=produto
    )

    if request.method == 'POST':

        if not request.user.is_authenticated:

            messages.error(
                request,
                'Você precisa entrar na sua conta.'
            )

            return redirect(
                'produtos_detalhes',
                produto_id=produto.id
            )

        comprou_produto = PurchaseItem.objects.filter(
            purchase__user=request.user,
            product=produto
        ).exists()

        if not comprou_produto:

            messages.error(
                request,
                'Você só pode avaliar produtos que comprou.'
            )

            return redirect(
                'produtos_detalhes',
                produto_id=produto.id
            )

        formulario = FormularioAvaliacaoProduto(
            request.POST
        )

        if formulario.is_valid():

            avaliacao = formulario.save(
                commit=False
            )

            avaliacao.product = produto
            avaliacao.user = request.user

            avaliacao.save()

            messages.success(
                request,
                'Sua avaliação foi publicada!'
            )

            return redirect(
                'produtos_detalhes',
                produto_id=produto.id
            )

    else:

        formulario = FormularioAvaliacaoProduto()

    return render(
        request,
        'beauty/produtos_detalhes.html',
        {
            'produto': produto,
            'avaliacoes': avaliacoes,
            'formulario': formulario,
        }
    )


def profissionais(request):

    lista_profissionais = Professional.objects.all()

    return render(
        request,
        'beauty/profissionais.html',
        {
            'profissionais':
                lista_profissionais,
        }
    )


def profissionais_detalhes(
    request,
    profissional_id
):

    profissional = Professional.objects.get(
        id=profissional_id
    )

    avaliacoes = ProfessionalReview.objects.filter(
        professional=profissional
    )

    return render(
        request,
        'beauty/profissionais_detalhes.html',
        {
            'profissional': profissional,
            'avaliacoes': avaliacoes,
        }
    )


@login_required
def agendamento(
    request,
    profissional_id
):

    profissional = Professional.objects.get(
        id=profissional_id
    )

    if request.method == 'POST':

        formulario = FormularioAgendamento(
            request.POST
        )

        formulario.fields[
            'service'
        ].queryset = profissional.services.all()

        if formulario.is_valid():

            novo_agendamento = formulario.save(
                commit=False
            )

            novo_agendamento.user = request.user
            novo_agendamento.professional = profissional

            novo_agendamento.save()

            messages.success(
                request,
                'Agendamento solicitado com sucesso!'
            )

            return redirect(
                'profissionais_detalhes',
                profissional_id=profissional.id
            )

    else:

        formulario = FormularioAgendamento()

        formulario.fields[
            'service'
        ].queryset = profissional.services.all()

    return render(
        request,
        'beauty/agendamento.html',
        {
            'profissional': profissional,
            'formulario': formulario,
        }
    )


def pacotes(request):

    lista_pacotes = Package.objects.filter(
        active=True
    )

    return render(
        request,
        'beauty/pacotes.html',
        {
            'pacotes': lista_pacotes,
        }
    )