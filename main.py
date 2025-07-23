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

def menu():
    print("\n--- Menu de Circulação ---")
    print("1. Localidade")
    print("2. Fora da localidade")
    print("3. Autoestrada")
    print("0. Sair")

def main():
    while True:
        menu()
        opcao = input("Escolha o tipo de circulação (0 para sair): ")
        if opcao == "0":
            print("Programa terminado.")
            break
        velocidade = float(input("Introduza a velocidade do carro (km/h): "))
        if opcao == "1":
            multa = multa_localidade(velocidade)
            local = "Localidade"
        elif opcao == "2":
            multa = multa_fora_localidade(velocidade)
            local = "Fora da localidade"
        elif opcao == "3":
            multa = multa_autoestrada(velocidade)
            local = "Autoestrada"
        else:
            print("Opção inválida. Tente novamente.")
            continue
        
        if multa == 0:
            print(f"Sem multa a pagar em {local}.")
        else:
            print(f"Multa a pagar em {local}: {multa}€")

if __name__ == "__main__":
    main()