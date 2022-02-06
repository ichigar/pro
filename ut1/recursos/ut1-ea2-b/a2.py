def cc2sc(identifier):
    """
    Converts text in camelCase format to snake_case format
    """
    # Pasar primer caracter a minúscula
    first_char = identifier[0].lower()
    result = first_char

    aux = identifier[1:]
    
    # Recorremos por caracter

    for caracter in aux:        
        if caracter != caracter.lower():
            result += '_' + caracter.lower()
        else:
            result += caracter

    # Recorremos por índice
    
    # for i in range(1, len(identifier)):
    #     caracter = identifier[i]
    #     if caracter != caracter.lower():
    #         result += '_' + caracter.lower()
    #     else:
    #         result += caracter
       
    return result
    
print(cc2sc("nomVariable"))            # 'nom_variable'
print(cc2sc("NomVariable"))            # 'nom_variable'
print(cc2sc("nomVariableCompuesto"))   # 'nom_variable_compuesto'
print(cc2sc("variable"))               # 'variable'