# Projeto de Catálogo de Filmes

## 🛠️ Tecnologias Utilizadas

- Python 3.10+
- Django 5.2
- SQLite (padrão) / PostgreSQL (opcional)
- HTML5, CSS3 (Grid, Flexbox, scroll customizado)


## 📦 Setup do Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/luciomessiassantos/catalogo-filmes-flix.git
cd catalogo-filmes-flix
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

#### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure seu banco de dados

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'catalogo_filmes',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

```

### 5. Execute as migrações

```bash
python manage.py migrate
```

### 6. Carregue os dados 

```bash
python manage.py loaddata fixtures/fixture_filmes.json
```

### 7. Rode o projeto

```bash
python manage.py runserver
```

