def saudacao(horas):
    if horas <= 12:
        return 'Bom dia'
    elif horas > 12 and horas <= 16:
        return 'Boa tarde'
    elif horas > 16 and horas < 24:
        return 'Boa noite'
    else:
        return 'Valor inválido!'


horario = int(input('Digite a horas atual no formato 24h: '))
print(saudacao(horario))
