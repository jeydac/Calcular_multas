# Este programa calcula a multa de acordo com a velocidade do veículo
# e o tipo de via (localidade, fora da localidade ou autoestrada).
# As multas são definidas por faixas de velocidade.

def multa_localidade(velocidade):
    if velocidade < 50:
        return 0
    elif velocidade >= 120:
        return 320
    elif velocidade >= 90:
        return 120
    elif velocidade > 50:
        return 60
    return 0

def multa_fora_localidade(velocidade):
    if velocidade < 50:
        return 0
    elif velocidade >= 120:
        return 120
    elif velocidade > 90:
        return 60
    return 0

def multa_autoestrada(velocidade):
    if velocidade < 50:
        return 0
    elif velocidade > 175:
        return 360
    elif velocidade > 150:
        return 120
    elif velocidade > 120:
        return 60
    return 0
