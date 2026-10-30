
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),

    path("produtos/", views.produtos, name="produtos"),
    path(
        "produtos/<int:produto_id>/",
        views.produtos_detalhes,
        name="produtos_detalhes",
    ),

    path("profissionais/", views.profissionais, name="profissionais"),
    path(
        "profissionais/<int:profissional_id>/",
        views.profissionais_detalhes,
        name="profissionais_detalhes",
    ),
    path(
        "profissionais/<int:profissional_id>/agendamento/",
        views.agendamento,
        name="agendamento",
    ),

    path("pacotes/", views.pacotes, name="pacotes"),
    path("cadastro/", views.cadastro, name="cadastro"),

    path(
        "entrar/",
        auth_views.LoginView.as_view(
            template_name="registration/login.html"
        ),
        name="login",
    ),

    path(
        "sair/",
        auth_views.LogoutView.as_view(),
        name="logout",
    ),
]
