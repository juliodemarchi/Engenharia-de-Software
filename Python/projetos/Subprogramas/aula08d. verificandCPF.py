def validar_cpf(cpf):
    # Removendo caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))

    # verificando se o CPF possui 11 dígitos
    if len(cpf) != 11:
        return False
    
    # Verificando se todos os digitos são iguais (caso raro, mas inválido)
    if cpf == cpf[0] * 11:
        return False
    
    # calculando o primeiro digito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = soma % 11
    if resto < 2:
        digito_verificador_1 = 0
    else: 
        digito_verificador_1 = 11 - resto

    # Verificando o primeiro dígito verificador
    if int(cpf[9])  != digito_verificador_1:
        return False
    
    # CPF Válido
    return True

    # Testando a função
    cpf = "123.456.789-09"
    if validar_cpf(cpf):
        print(f'O CPF {cpf} é válido.')
    else:
        print(f'O CPF {cpf} é inválido.')