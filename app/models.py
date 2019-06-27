from django.db import models

# Create your models here.
class Autor(models.Model):
    nome = models.CharField(max_length=100)
    dt_nascimento = models.DateField()
    vivo = models.BooleanField(default=True)
    pais_origem = models.CharField(max_length=50)

    def __str__(self):
        return self.nome #Pra nao aparecer obj1 etc
    
class Livro(models.Model):

    genero_opcoes = {
        ('tr', 'Terror'), #O primeiro é como fica escrito no banco de dados, o outro é como aparece
        ('rm', 'Romance'),
        ('aj', 'Autoajuda'),
        ('av', 'Aventura'),
        ('mg', 'Mangá'),
        ('hq', 'História em Quadrinho'),
        ('bg', 'Biografia')
    }

    titulo = models.CharField(max_length=100)           #CharField é pra determinar q é texto
    ediora = models.CharField(max_length=50)            #max_length é o limite de caracteres
    dt_lancamento = models.DateField()          #DateField serve pra dizer q é data
    preco = models.DecimalField(decimal_places=2, max_digits=10, default=30)  #DecimalField
    paginas = models.IntegerField()
    idioma = models.CharField(max_length=30)
    resumo = models.TextField(default='')          #TextField Não precisa definir limite de caracteres e panz
    genero = models.CharField(max_length=2, choices=genero_opcoes)
    nome = models.ForeignKey(Autor, on_delete=models.SET_DEFAULT, default='')          #ForeignKey serve para relacionar as coisas ... on_delete é pra definir como vai ser apagado do bancO. SET_DEFAULT é para deixar vazio mas ainda manter a relação
    
    def __str__(self):
        return self.titulo
