def option_input(msg, valid_options):
    while True:
        try:
            valor = int(input(msg))
            if valor in valid_options:
                return valor
            else:
                print(f"Opção inválida. Escolha entre: {valid_options}")
        except ValueError:
            print(f"Opção inválida. Escolha entre: {valid_options}")