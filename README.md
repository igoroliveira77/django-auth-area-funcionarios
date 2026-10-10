
# Área Restrita de Funcionários

Sistema web desenvolvido com Django e PostgreSQL para a disciplina de Web 1.

## Funcionalidades

- Página inicial pública.
- Login e logout de usuários.
- Painel restrito a funcionários autenticados.
- Perfil com informações do usuário conectado.
- Cadastro e gerenciamento de usuários pelo Django Admin.
- Proteção de páginas com `LoginRequiredMixin`.
- Exibição condicional de links com `user.is_authenticated`.
- Interface estilizada com HTML e CSS.

## Tecnologias utilizadas

- Python
- Django 5.2
- PostgreSQL
- HTML5
- CSS3
- Git e GitHub

## Requisitos

- Python compatível com as dependências do projeto.
- PostgreSQL instalado e em execução.
- Git (opcional, para clonar o repositório).

## Instalação

### 1. Clonar o repositório

```bash
git clone https://github.com/igoroliveira77/django-auth-area-funcionarios.git
cd django-auth-area-funcionarios
```

### 2. Criar e ativar o ambiente virtual

No Windows:

```bash
py -m venv .venv
.venv\Scripts\activate
```

### 3. Instalar as dependências

```bash
python -m pip install -r requirements.txt
```

### 4. Configurar as variáveis de ambiente

Crie um arquivo `.env` na mesma pasta do `manage.py`, usando o `.env.example` como modelo.

Preencha as variáveis com as configurações locais do PostgreSQL e gere uma chave secreta própria para o Django.

Não compartilhe o arquivo `.env` nem suas credenciais.

### 5. Criar o banco de dados

No PostgreSQL, crie um banco de dados chamado `django_auth` ou ajuste `DB_NAME` no arquivo `.env` para o nome escolhido.

Configure também o usuário, a senha, o host e a porta.

### 6. Executar as migrações

```bash
python manage.py migrate
```

### 7. Criar o administrador

```bash
python manage.py createsuperuser
```

### 8. Iniciar o servidor

```bash
python manage.py runserver
```

Acesse o sistema em:

- Página inicial: http://127.0.0.1:8000/
- Login: http://127.0.0.1:8000/login/
- Painel: http://127.0.0.1:8000/painel/
- Perfil: http://127.0.0.1:8000/perfil/
- Administração: http://127.0.0.1:8000/admin/

## Observações

As páginas do painel e do perfil exigem autenticação. Os usuários funcionários podem ser cadastrados pelo Django Admin.

O arquivo `.env` contém configurações locais e não deve ser enviado ao GitHub.

## Autor

Igor Oliveira
