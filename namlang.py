import re

def transpilador_nam(codigo_fonte):
    linhas = codigo_fonte.split('\n')
    codigo_final = []
    
    # Mapeamento de palavras-chave
    substituicoes = {
        'namif ': 'elif ',
        'namelse:': 'else:',
        'namdef ': 'def ',
        'namfor ': 'for ',
        'namwhile ': 'while ',
        'namback ': 'return ',
        'namport ': 'import '
    }

    for linha in linhas:
        nova_linha = linha
        
        # 1. Trata o 'nif' (para não confundir com 'namif')
        if nova_linha.strip().startswith('nif '):
            nova_linha = nova_linha.replace('nif ', 'if ', 1)

        # 2. Trata as outras palavras-chave
        for nam, py in substituicoes.items():
            if nam in nova_linha:
                nova_linha = nova_linha.replace(nam, py)

        # 3. Trata nam(...) e namput(...)
        nova_linha = nova_linha.replace('nam(', 'print(')
        nova_linha = nova_linha.replace('namput(', 'input(')

        # 4. Trata comandos de Design (Simulação)
        if 'namresolution' in nova_linha:
            res = re.search(r'"(.*?)"', nova_linha).group(1)
            nova_linha = f'print("--- Canvas Criado: {res} ---")'
        
        if 'namarredont.square' in nova_linha:
            tam = re.search(r'"(.*?)"', nova_linha).group(1)
            nova_linha = f'print("--- Quadrado Arredondado Desenhado: {tam}px ---")'

        codigo_final.append(nova_linha)
    
    return "\n".join(codigo_final)

# Exemplo de teste
meu_codigo_nam = """
nif 10 > 5:
    nam("Dez é maior que cinco")
namresolution "1080x1080":
    namarredont.square "500"
"""

print(transpilador_nam(meu_codigo_nam))
