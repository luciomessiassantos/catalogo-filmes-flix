from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Categoria(models.Model):
    class Opcoes(models.TextChoices):
        ACAO = 'AC', 'Ação'
        COMEDIA = 'CO', 'Comédia'
        DRAMA = 'DR', 'Drama'
        TERROR = 'TE', 'Terror'
        FICCAO = 'FI', 'Ficção Científica'
        ROMANCE = 'RO', 'Romance'
        SUSPENSE = 'SU', 'Suspense'
        AVENTURA = 'AV', 'Aventura'
        FANTASIA = 'FA', 'Fantasia'
        MISTERIO = 'MI', 'Misterio'
        CRIMINAL = 'CR', 'Criminal'
        

    nome = models.CharField(
        max_length=2,
        choices=Opcoes.choices,
        unique=True
    )

    def __str__(self):
        return self.get_nome_display() # type: ignore

class Filme(models.Model):


    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    categorias = models.ManyToManyField(Categoria, related_name='filmes')
    ano_lancamento = models.IntegerField()
    nota = models.DecimalField(
        max_digits=3,          
        decimal_places=1,
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
        null=True,             
        blank=True,
        help_text="Nota de 0.0 a 10.0"
    )
    duracao_segundos = models.PositiveIntegerField(
        help_text="Duração total em segundos (ex: 7200 para 2 horas)",
        null=True, blank=True
    )
    imagem = models.ImageField(upload_to="filmes/")

    def __str__(self):
        return self.titulo
    