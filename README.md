# Amicci Briefing API

_API criada para propósitos de testes_

![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

No contexto da Amicci, um Briefing é o documento que descreve um projeto a ser desenvolvido por um Fornecedor, a partir do levantamento realizado com o Cliente, onde descreve as premissas contratuais e atributos de cada um dos produtos a serem produzidos.

## Configuração

Toda a configuração da aplicação é feita através do arquivo de variáveis de ambiente, `.env`. As propriedades utilizadas podem ser encontradas no arquivo `.env.example`.
Um Django superuser tentará ser criado com `DJANGO_SUPERUSER_USERNAME`, `DJANGO_SUPERUSER_EMAIL` e `DJANGO_SUPERUSER_PASSWORD`, porém as variáveis podem ser omitidas caso não deseje superuser.

## Executando com Docker

A aplicação Briefing API já está pronta para ser executada em container.

Por padrão, a imagem Docker irá expor a porta 8000, podendo ser alterada no Dockerfile. Estando tudo pronto, utilize o Dockerfile para construir a imagem.

```sh
docker build -t amicci/briefing-api:latest . 
```

O comando irá criar a imagem e carregar as dependências necessárias. O repositório `amicci/briefing-api` e tag `latest` podem ser modificados de acordo com a necessidade.

Feito isso, rode a imagem Docker e mapeie a porta para a que desejar no host. No exemplo a seguir, mapeamos a mesma porta exportada pelo container para o host:

```sh
docker run -d -p 8000:8000 --restart=always --name=amicci-briefing-api amicci/briefing-api:latest
```

### Docker Compose

O método preferido para rodar essa aplicação e já subir uma instância PostgreSQL, é utilizando docker-compose. Por padrão, a porta 8000 é exposta e é usado Postgres 13. Para executar, pode-se utilizar o seguinte comando:

```sh
docker compose up -d
```

Por fim, verifique o deployment acessando o servidor em um navegador de sua preferência:

```sh
127.0.0.1:8000/api/
```

## Endpoints

### [Briefing](docs/briefing.md)

### [Retailer](docs/retailer.md)

### [Vendor](docs/vendors.md)

### [Category](docs/category.md)
