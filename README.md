# web-CNAB

O web CNAB é um projeto para processamento de arquivos CNAB . Com ele, é possível fazer upload de arquivos CNAB e armazenar as informações das transações em um banco de dados.

## Tecnologias utilizadas

- Python
- Django
- Django Rest Framework (DRF)
- SQLite
- Bibliotecas: Decimal e datetime

## Instalação

Após clonar o repositório, sega os seguintes passos:

1. crie seu ambiente virtual:

```shell
python -m venv venv
```

2. Ative seu venv:

```shell
# linux:
source venv/bin/activate

# windows:
.\venv\Scripts\activate
```

3. Instale as dependências

```shell
pip install -r requirements.txt
```

4. Em seguida, execute as migrações

```shell
python manage.py migrate
```

- Para iniciar o servidor utilize o comando `python manage.py runserver`

## Utilização

Para fazer o upload de um arquivo CNAB, acesse a rota /api/upload/ e faça o upload do arquivo. As informações serão armazenadas no banco de dados.

Para visualizar a lista de transações importadas e o saldo total por loja, acesse a rota /api/list/.

### Endpoints

POST /api/upload/: Faz o upload de um arquivo CNAB.

GET /api/list/: Retorna a lista de transações importadas e o saldo total por loja.
