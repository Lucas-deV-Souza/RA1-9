# Lucas de Souza Vieira = Lucas-deV-Souza
# RA1 9

import sys
#Onde a analise textual comeca
def estado_inicial(caractere,acumula):
    if caractere.isdigit():
        return estado_inteiro, acumula + caractere
    if caractere == " ":
        return estado_inicial, acumula
    if caractere in "+-*%^":
        return estado_operacao, acumula + caractere
    if caractere in "/":
        return estado_duasbarra, acumula + caractere
    if caractere in "()":
        return estado_parenteses, acumula + caractere
    if caractere.isalpha():
        return estado_palavra, acumula + caractere
    return estado_erro, acumula


#inteiros e ponto
def estado_inteiro(caractere, acumula):
    if caractere.isdigit():
        return estado_inteiro, acumula + caractere
    if caractere == ".":
        return estado_decimal, acumula + caractere
    if caractere == " ":
        token.append(('Numero',acumula))
#        print(f"token salvo de Numero {acumula}")
        return estado_inicial, ""
    return estado_erro, acumula


#decimal
def estado_decimal(caractere, acumula):
    if caractere == ".":
        return estado_erro, acumula
    if caractere.isdigit():
        return estado_decimal, acumula + caractere
    if caractere == " ":
        token.append(('Numero',acumula))
#        print(f"token salvo de Numero {acumula}")
        return estado_inicial, ""
    return estado_erro, acumula

#Algum sinal de operação
def estado_operacao(caractere,acumula):
    token.append(("Operacao", acumula))
    return estado_inicial(caractere, "")

#detecta parenteses
def estado_parenteses(caractere,acumula):
    token.append(("Parenteses", acumula))
#    print(f"Parenteses salvo {acumula}")
    return estado_inicial(caractere, "")

#detecta parlavra
def estado_palavra(caractere,acumula):
    if caractere.isalpha():
        return estado_palavra,acumula + caractere
    if caractere == " ":
        if acumula.isupper():
            token.append(("Palavra", acumula))
            return estado_inicial(caractere, "")
        else:
            return estado_erro, acumula
    return estado_erro, acumula

#detecta a se possui duas barras para o inteiro
def estado_duasbarra(caractere,acumula):
    if caractere == "/":
        token.append(("Divisao inteira", acumula + caractere))
        return estado_inicial, ""
    
    token.append(("Operacao", acumula))
    return estado_inicial(caractere, "")






# PRA CASO ALGUM VALOR SEJA ERRADO
def estado_erro(caractere,acumula):
    print(f"SALA INVALIDA QUEBROU TUDO {caractere}")
    return estado_erro, acumula









def lerArquivo(nomeArquivo):
    linhas = []
    try:
        with open(nomeArquivo, "r") as arquivo:
            for linha_orig in arquivo:
                linha_limpa = linha_orig.strip()
                if linha_limpa != "": # ignora linhas vazias
                    linhas.append(linha_limpa + " ") # adiciona um espaço no final
        return linhas
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nomeArquivo}' não foi encontrado.")
        sys.exit()


def parseExpressao(linha):
    global token # pra puxar do main
    token = []
    num_atual = estado_inicial
    bolso = ""
    abrefecha_parenteses = 0

    for letra in linha:
        if letra == "(": abrefecha_parenteses += 1
        if letra == ")": abrefecha_parenteses -= 1
        num_atual, bolso = num_atual(letra, bolso)
        
    if abrefecha_parenteses != 0:
        print("Erro: Parênteses desbalanceados!")
        return [] 

    return token


def executarExpressao(lista_tokens, memoria, resultado_anterior):
    pilha = []
    ultimo_tk = None
    
    # verifica a ultima palavra antes de res ou mem
    for t, v in lista_tokens:
        if t != "Parenteses":
            ultimo_tk = v

    for tipo, valor in lista_tokens:
        if tipo == "Numero":
            pilha.append(float(valor))
        elif tipo == "Operacao":
            if len(pilha) < 2: continue
            valor2 = pilha.pop()
            valor1 = pilha.pop()
            
            if valor == "+": pilha.append(valor1 + valor2)
            elif valor == "-": pilha.append(valor1 - valor2)
            elif valor == "*": pilha.append(valor1 * valor2)
            elif valor == "/": pilha.append(valor1 / valor2 if valor2 != 0 else 0)
            elif valor == "%": pilha.append(valor1 % valor2)
            elif valor == "^": pilha.append(valor1 ** valor2)
            
        elif tipo == "Divisao inteira":
            if len(pilha) < 2: continue
            valor2 = pilha.pop()
            valor1 = pilha.pop()
            pilha.append(float(valor1 // valor2 if valor2 != 0 else 0))
            
        elif tipo == "Palavra":
            if valor == "RES":
                if len(pilha) > 0:
                    nlinhas = int(pilha.pop())
                    if 0 < nlinhas <= len(resultado_anterior):
                        pilha.append(resultado_anterior[-nlinhas])
                    else:
                        pilha.append(0.0)
            else: # Comando MEM
                if valor == ultimo_tk: # se for A MEM, guarda na mem
                    if len(pilha) > 0:
                        memoria[valor] = pilha.pop()
                else: # se for (A), recupera da mem
                    pilha.append(memoria.get(valor, 0.0))

    # Retorna o topo da pilha ou 0.0 se algo der errado
    return pilha[0] if len(pilha) > 0 else 0.0


def exibirResultados(resultados):
    print("\n--- Resultados Calculados no Python ---")
    for i, res in enumerate(resultados):
        print(f"Linha {i+1}: {res:.1f}")
    print("---------------------------------------\n")


# converter em assembler
def gerarAssembly(lista_tokens, linha_atual):
    # Dicionário de tradução das operações matemáticas para ARMv7 64-bit (VFP)
    operacoes = {
        "+": "    VADD.F64 D2, D1, D0\n",
        "-": "    VSUB.F64 D2, D1, D0\n",
        "*": "    VMUL.F64 D2, D1, D0\n",
        "/": "    VDIV.F64 D2, D1, D0\n"
    }
    
    caixa = ""
    ultimo_tk = None
    
    # Busca quem e a ultima palavra (pra saber se e ou nao)
    for t, v in lista_tokens:
        if t != "Parenteses":
            ultimo_tk = v

    for i in range(len(lista_tokens)):
        tipo, valor = lista_tokens[i][0], lista_tokens[i][1]
        
        if tipo == "Numero":
            if i + 1 < len(lista_tokens) and lista_tokens[i+1][1] == "RES":
                continue 
            
            # NOVO ARMv7: Pega o número direto da seção .data
            v_safe = valor.replace(".", "_")
            caixa += f"    LDR R0, =NUM_{v_safe}\n"
            caixa += f"    VLDR D0, [R0]\n"
            caixa += f"    VPUSH {{D0}}\n" # salvo no ARM!

        elif tipo == "Operacao":
            if valor in operacoes:
                caixa += f"    VPOP {{D0}}\n"   # retira do valor 2
                caixa += f"    VPOP {{D1}}\n"   # retira do valor 1
                caixa += operacoes[valor]       # faz a conta para salvar na memoria D2
                caixa += f"    VPUSH {{D2}}\n"  # salva o resultado

        elif tipo == "Palavra":
            if valor == "RES":
                num_voltas = int(lista_tokens[i-1][1])
                linha_alvo = linha_atual - num_voltas
                caixa += f"    LDR R0, =RES_{linha_alvo}\n"
                caixa += f"    VLDR D0, [R0]\n"
                caixa += f"    VPUSH {{D0}}\n"
            else:
                if valor == ultimo_tk: # salvo o arquivo na memoria
                    caixa += f"    VLDR D0, [SP]\n" # faz a leitura do topo da pilha
                    caixa += f"    LDR R0, ={valor}\n"
                    caixa += f"    VSTR D0, [R0]\n"
                else: # Le o arquivo da memoria
                    caixa += f"    LDR R0, ={valor}\n"
                    caixa += f"    VLDR D0, [R0]\n"
                    caixa += f"    VPUSH {{D0}}\n"
                    
    # Nessa parte, o codigo salva o resultado final da linha no histórico
    caixa += f"    VLDR D0, [SP]\n"
    caixa += f"    LDR R0, =RES_{linha_atual}\n"
    caixa += f"    VSTR D0, [R0]\n"
    
    return caixa

# CODIGO PRINCIPAL
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Erro: faltou o arquivo de texto!\nExemplo: python analisador.py teste1.txt")
        sys.exit()

    nome_arquivo = sys.argv[1]
    arquivo_asm = nome_arquivo.replace(".txt", ".asm")
    
    memoria_python = {}
    resultados_python = []
    tokens_finais = []
    
    linhas = lerArquivo(nome_arquivo)
    
    # começa o codigo em asm com a nomenclatura
    texto_asm = ".data\n"
    
    # loop de mapeamento
    for i, linha in enumerate(linhas):
        texto_asm += f"RES_{i+1}: .double 0.0\n"
        tk_temp = parseExpressao(linha)
        for j in range(len(tk_temp)):
            t, v = tk_temp[j]
            if t == "Palavra" and v != "RES" and f"{v}:" not in texto_asm:
                texto_asm += f"{v}: .double 0.0\n"
            elif t == "Numero":
                # Ignora se for o numero de uma RES
                if j + 1 < len(tk_temp) and tk_temp[j+1][1] == "RES":
                    continue
                v_safe = v.replace(".", "_")
                if f"NUM_{v_safe}:" not in texto_asm:
                    texto_asm += f"NUM_{v_safe}: .double {v}\n"
                
    texto_asm += "\n.text\n.global _start\n_start:\n"

    # Inicializa o ponteiro do ARM
    texto_asm += "    LDR SP, =0x20000\n\n"

    for i, linha in enumerate(linhas):
        tokens = parseExpressao(linha)
        if not tokens: continue
        
        tokens_finais.extend(tokens)
        res_linha = executarExpressao(tokens, memoria_python, resultados_python)
        resultados_python.append(res_linha)
        
        texto_asm += f"// --- Linha {i+1} ---\n"
        texto_asm += gerarAssembly(tokens, i+1)
        texto_asm += "\n"

    texto_asm += "// --- MOSTRANDO NOS LEDS (CPulator) ---\n"
    texto_asm += "    VLDR D0, [SP]\n"          
    texto_asm += "    VCVT.S32.F64 S0, D0\n"       
    texto_asm += "    VMOV R0, S0\n"               
    texto_asm += "    LDR R1, =0xFF200000\n"       
    texto_asm += "    STR R0, [R1]\n"              
    texto_asm += "FIM: B FIM\n"                    

    exibirResultados(resultados_python)

    with open(arquivo_asm, "w") as f:
        f.write(texto_asm)
        
    with open("tokens.txt", "w") as f:
        for t in tokens_finais:
            f.write(f"{t}\n")

    print(f"Sucesso! Arquivo '{arquivo_asm}' gerado e Tokens salvos em 'tokens.txt'.")

#digitar no terminal um exemplo: python analisador.py teste1.txt 
#trocar os numeros do teste, como por exemplo: teste1, teste2, teste3 para ve-los