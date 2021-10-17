# django_map
crud‌ de marcadores de mapa usando o folium (falta adicionar os mecanismos de editar e deletar)


# crud-cliente

Repositório criado para uma aplicação com o framework Django que realiza o CRUD (Create, Read, Update, Delete) de marcadores(alvos) no Mapa. (falta adicionar os mecanismos de editar e deletar)

<h2> Configuração necessária para rodar o projeto</h2>

1. Após clonar o repositório em seu computador, mova-se para dentro da pasta do projeto e realize a criação de ambiente virtual para rodar a aplicação:
```
python3 -m venv nome_da_virtualenv
```

2. Ative a máquina virtual
```
.\nome_da_virtualenv\Scripts\activate (CMD/PowerShell) 
source /nome_da_virtualenv/bin/activate (bash/zsh)
```

3. Instale as dependências do projeto:

```
pip install -r requirements.txt
```

4. Execute essa imagem afim de criar e executar um container do banco de dados Postgresql (obs: o DATABASES em settings.py ja se encontra configurado para o db abaixo)
```
docker run --name some-postgres -e POSTGRES_USER=user001 -e POSTGRES_PASS=123456789 -e POSTGRES_DBNAME=django_mp -p 5432:5432 postgres
```

5. Realize as migrações para o banco de dados:
```
python manage.py migrate
```

7. Inicie o projeto:
```
python manage.py runserver
```

8. Pronto, agora é só copiar o link gerado e colocar no navegador para ter acesso ao sistema
```
localhost:8000
```

