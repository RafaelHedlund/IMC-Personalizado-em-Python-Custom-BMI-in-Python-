def calcular_imc(peso, altura):
    """Calcula o índice de massa corporal (IMC) com base no peso e altura."""
    imc = peso / altura ** 2
    return imc

def exibir_classificacao(imc):
    """Exibe a classificação do IMC de acordo com o valor calculado."""
    if imc < 18.5:
        print('Seu IMC é {:.1f}. Você está abaixo do peso normal.'.format(imc))
    elif imc < 25:
        print('Seu IMC é {:.1f}. Parabéns! Você está dentro do peso normal.'.format(imc))
    elif imc < 30:
        print('Seu IMC é {:.1f}. Attenção! Você está acima do peso normal.'.format(imc))
    else:
        print('Seu IMC é {:.1f}. Cuidado! Você está obeso.'.format(imc))

def exibir_menu():
    """Exibe um menu de opções para o usuário escolher o sistema de unidades."""
    print('Selecione o sistema de unidades para inserir seu peso e altura:')
    print('1 - Métrico (quilogramas e metros)')
    print('2 - Imperial (libras e polegadas)')

def converter_para_metrico(peso, altura):
    """Converte peso e altura do sistema imperial para métrico."""
    peso = peso / 2.205  # converte libras para quilogramas
    altura = altura * 0.0254  # converte polegadas para metros
    return peso, altura

while True:
    exibir_menu()
    opcao = int(input('Opção escolhida: '))

    if opcao == 1:
        peso = float(input('Digite seu peso em quilogramas: '))
        altura = float(input('Digite sua altura em metros: '))
    else:
        peso = float(input('Digite seu peso em libras: '))
        altura = float(input('Digite sua altura em polegadas: '))
        peso, altura = converter_para_metrico(peso, altura)

    if peso <= 0 or altura <= 0:
        print('Valores inválidos. O peso e a altura devem ser maiores que zero.')
        continue

    imc = calcular_imc(peso, altura)
    exibir_classificacao(imc)

    opcao_repetir = input('Deseja calcular novamente? (s/n)')
    if opcao_repetir.lower() != 's':
        break
