# GasFinder

GasFinder é uma aplicação web projetada para ajudar os usuários a encontrar postos de combustível próximos com base em preço e distância. Além disso, a aplicação permite que os usuários visualizem o histórico de abastecimento, façam avaliações e deixem comentários sobre os postos de combustível.

## Funcionalidades

- **Pesquisa de Postos de Combustível**: Encontre postos de combustível próximos com base em preço e distância.
- **Avaliações e Comentários**: Os usuários podem avaliar e comentar sobre os postos de combustível.
- **Histórico de Abastecimento**: Visualize o histórico de abastecimento dos usuários.
- **Perfis de Usuários e Postos**: Perfis detalhados para usuários e postos de combustível.
- **Páginas de Erro Personalizadas**: Páginas de erro 404 e 500 customizadas.

## Requisitos

- Python 3.8+
- Django 3.2+
- PostgreSQL

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/seu-usuario/gasfinder.git
    cd gasfinder
    ```

2. Crie e ative um ambiente virtual:

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4. Configure as variáveis de ambiente:

    Crie um arquivo `.env` na raiz do projeto e adicione suas configurações:

    ```env
    SECRET_KEY=your_secret_key
    DEBUG=True
    DATABASE_URL=postgres://usuario:senha@localhost:5432/GasFinder
    ```

5. Realize as migrações do banco de dados:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. Crie um superusuário:

    ```bash
    python manage.py createsuperuser
    ```

7. Execute o servidor de desenvolvimento:

    ```bash
    python manage.py runserver
    ```

## Uso

1. Acesse o servidor de desenvolvimento em seu navegador:

    ```
    http://localhost:8000
    ```

2. Utilize as funcionalidades da aplicação, como pesquisa de postos, avaliações, e visualização do histórico de abastecimento.

## Testes Automatizados

Para executar os testes automatizados:


python manage.py test

Despliegue no Heroku

1.Instale a CLI do Heroku e faça login:

```bash
  heroku login
```

2.Crie um novo aplicativo Heroku:

```bash
  heroku create nome-do-seu-aplicativo
```

3.Configure as variáveis de ambiente no Heroku:

```bash
  heroku config:set SECRET_KEY=your_secret_key
    heroku config:set DEBUG=False
```

4.Envie o código para o Heroku:

```bash
git push heroku main
```

5.Realize as migrações no Heroku:
```bash
heroku run python manage.py migrate
```

6.Crie um superusuário no Heroku:
```
heroku run python manage.py createsuperuser
```

Contribuição
Faça um fork do projeto
Crie uma branch para sua feature (git checkout -b feature/nome-da-feature)
Commit suas mudanças (git commit -am 'Adiciona nova feature')
Envie para a branch (git push origin feature/nome-da-feature)
Crie um novo Pull Request

Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

Contato
Email: mateus.m.matos@hotmail.com
GitHub: MateusMMatos

### Passos Adicionais

- Certifique-se de que todas as variáveis de ambiente e configurações mencionadas no README estejam corretas e seguras antes de compartilhar ou implantar o projeto.
- Atualize o link do repositório GitHub e suas informações de contato no README conforme necessário.

Se precisar de mais alguma coisa, estou à disposição!
