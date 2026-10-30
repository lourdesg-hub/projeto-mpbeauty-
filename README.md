# MPBeauty

## Sobre o projeto

O MPBeauty é um sistema web desenvolvido para facilitar o acesso a produtos, serviços e profissionais da área da beleza. A plataforma permite que os usuários conheçam produtos, consultem profissionais, visualizem pacotes de serviços e realizem agendamentos.

## Funcionalidades

- Página inicial com destaques.
- Catálogo de produtos.
- Detalhes dos produtos e avaliações.
- Listagem de profissionais.
- Detalhes dos profissionais e seus serviços.
- Agendamento de atendimentos.
- Catálogo de pacotes de beleza.
- Cadastro e login de usuários.
- Painel administrativo para gerenciamento das informações.

## Tecnologias utilizadas

- Python
- Django
- HTML5
- CSS3
- JavaScript
- SQLite
- Git e GitHub

## Como executar o projeto

1. Clone o repositório:

   ```bash
   git clone URL_DO_REPOSITORIO
   ```

2. Entre na pasta do projeto:

   ```bash
   cd projeto-mpbeauty-
   ```

3. Crie e ative um ambiente virtual:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

4. Instale as dependências:

   ```bash
   pip install django
   ```

5. Execute as migrações:

   ```bash
   python manage.py migrate
   ```

6. Inicie o servidor:

   ```bash
   python manage.py runserver
   ```

7. Acesse no navegador:

   http://127.0.0.1:8000/

## Administração

Para acessar o painel administrativo, crie um superusuário:

```bash
python manage.py createsuperuser
```

Depois, acesse:

http://127.0.0.1:8000/admin/

## Objetivo

O objetivo do MPBeauty é oferecer uma plataforma organizada e acessível para aproximar clientes e profissionais da área da beleza, facilitando a consulta de serviços e a realização de agendamentos.