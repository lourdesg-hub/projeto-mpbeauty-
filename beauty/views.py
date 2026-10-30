
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

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
    produtos = Product.objects.filter(active=True)[:6]
    profissionais = Professional.objects.all()[:4]
    pacotes = Package.objects.filter(active=True)[:3]

    return render(request, "beauty/home.html", {
        "produtos": produtos,
        "profissionais": profissionais,
        "pacotes": pacotes,
    })


def produtos(request):
    categoria = (
        request.GET.get("categoria")
        or request.GET.get("category")
    )

    lista = Product.objects.filter(active=True)

    if categoria:
        lista = lista.filter(category=categoria)

    return render(request, "beauty/produtos.html", {
        "produtos": lista,
        "categoria": categoria,
    })


def produtos_detalhes(request, produto_id):
    produto = get_object_or_404(
        Product,
        id=produto_id,
        active=True
    )

    formulario = FormularioAvaliacaoProduto()

    if request.method == "POST":

        if not request.user.is_authenticated:
            return redirect("login")

        comprou = PurchaseItem.objects.filter(
            purchase__user=request.user,
            product=produto
        ).exists()

        if not comprou:
            messages.error(
                request,
                "Você precisa comprar o produto para avaliá-lo."
            )

        elif ProductReview.objects.filter(
            product=produto,
            user=request.user
        ).exists():
            messages.warning(
                request,
                "Você já avaliou este produto."
            )

        else:
            formulario = FormularioAvaliacaoProduto(request.POST)

            if formulario.is_valid():
                avaliacao = formulario.save(commit=False)
                avaliacao.product = produto
                avaliacao.user = request.user
                avaliacao.save()

                messages.success(
                    request,
                    "Avaliação enviada com sucesso!"
                )

                return redirect(
                    "produtos_detalhes",
                    produto_id=produto.id
                )

    return render(request, "beauty/produtos_detalhes.html", {
        "produto": produto,
        "avaliacoes": produto.reviews.all(),
        "formulario": formulario,
    })


def profissionais(request):
    lista = Professional.objects.all()

    return render(request, "beauty/profissionais.html", {
        "profissionais": lista,
    })


def profissionais_detalhes(request, profissional_id):
    profissional = get_object_or_404(
        Professional,
        id=profissional_id
    )

    formulario = FormularioAvaliacaoProfissional()

    if request.method == "POST":

        if not request.user.is_authenticated:
            return redirect("login")

        ja_avaliou = ProfessionalReview.objects.filter(
            professional=profissional,
            user=request.user
        ).exists()

        if ja_avaliou:
            messages.warning(
                request,
                "Você já avaliou esta profissional."
            )

        else:
            formulario = FormularioAvaliacaoProfissional(
                request.POST
            )

            if formulario.is_valid():
                avaliacao = formulario.save(commit=False)
                avaliacao.professional = profissional
                avaliacao.user = request.user
                avaliacao.save()

                messages.success(
                    request,
                    "Avaliação enviada com sucesso!"
                )

                return redirect(
                    "profissionais_detalhes",
                    profissional_id=profissional.id
                )

    return render(request, "beauty/profissional_detalhes.html", {
        "profissional": profissional,
        "avaliacoes": profissional.reviews.all(),
        "formulario": formulario,
    })


@login_required
def agendamento(request, profissional_id):

    profissional = get_object_or_404(
        Professional,
        id=profissional_id
    )

    formulario = FormularioAgendamento(
        request.POST or None
    )

    formulario.fields["service"].queryset = (
        profissional.services.all()
    )

    if request.method == "POST" and formulario.is_valid():

        novo = formulario.save(commit=False)

        novo.user = request.user
        novo.professional = profissional

        if novo.date < timezone.localdate():

            formulario.add_error(
                "date",
                "Escolha uma data futura."
            )

        elif (
            novo.location == "home"
            and not profissional.home_service
        ):

            formulario.add_error(
                "location",
                "Esta profissional não atende a domicílio."
            )

        elif (
            novo.location == "studio"
            and not profissional.studio_service
        ):

            formulario.add_error(
                "location",
                "Esta profissional não atende no estabelecimento."
            )

        else:

            conflito = Appointment.objects.filter(
                professional=profissional,
                date=novo.date,
                time=novo.time,
                status__in=["pending", "confirmed"],
            ).exists()

            if conflito:
                formulario.add_error(
                    "time",
                    "Este horário já está reservado."
                )

            if not formulario.errors:
                novo.save()

                messages.success(
                    request,
                    "Agendamento solicitado com sucesso!"
                )

                return redirect(
                    "profissionais_detalhes",
                    profissional_id=profissional.id
                )

    return render(request, "beauty/agendamento.html", {
        "profissional": profissional,
        "formulario": formulario,
    })


def pacotes(request):
    lista = Package.objects.filter(active=True)

    return render(request, "beauty/pacotes.html", {
        "pacotes": lista,
    })


def cadastro(request):

    formulario = UserCreationForm(
        request.POST or None
    )

    if request.method == "POST" and formulario.is_valid():

        usuario = formulario.save()

        login(request, usuario)

        messages.success(
            request,
            "Cadastro realizado com sucesso!"
        )

        return redirect("inicio")

    return render(request, "registration/cadastro.html", {
        "formulario": formulario,
    })
