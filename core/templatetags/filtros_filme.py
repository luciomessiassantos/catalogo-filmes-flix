from django import template

register = template.Library()

@register.filter
def formata_duracao(segundos):
    if not segundos:
        return "Duração não informada"
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    return f"{horas}h {minutos}min" if horas > 0 else f"{minutos}min"