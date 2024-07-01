# Importa a classe Fraction do módulo fractions para lidar com frações
from fractions import Fraction
# Importa o módulo de expressões regulares (não utilizado aqui, mas pode ser útil para validações)
import re

# Função para calcular a fração geratriz de uma dízima periódica simples
def geratriz_dizima_simples(periodo):
    # Calcula o número de dígitos no período
    n = len(periodo)
    # Converte o período para um número inteiro
    numerador = int(periodo)
    # Calcula o denominador que é 10^n - 1, onde n é o número de dígitos no período
    denominador = 10**n - 1
    # Retorna a fração simplificada
    return Fraction(numerador, denominador)

# Função para calcular a fração geratriz de uma dízima periódica composta
def geratriz_dizima_composta(nao_periodica, periodo):
    # Calcula o número de dígitos na parte não periódica
    n = len(nao_periodica)
    # Calcula o número de dígitos no período
    m = len(periodo)
    # Converte a parte não periódica para um número inteiro
    parte_nao_periodica = int(nao_periodica)
    # Converte o período para um número inteiro
    parte_periodica = int(periodo)
    # Calcula o numerador da fração geratriz
    numerador = parte_nao_periodica * (10**m - 1) + parte_periodica
    # Calcula o denominador da fração geratriz
    denominador = (10**n) * (10**m - 1)
    # Retorna a fração simplificada
    return Fraction(numerador, denominador)

# Função para calcular a dízima a partir de uma fração
def dizima_a_partir_de_fracao(fracao):
    # Calcula a parte inteira da divisão do numerador pelo denominador
    inteiro = fracao.numerator // fracao.denominator
    # Calcula o resto da divisão do numerador pelo denominador
    resto = fracao.numerator % fracao.denominator
    # Inicia o resultado com a parte inteira seguida de um ponto
    resultado = f"{inteiro}."
    
    # Lista para armazenar os restos já encontrados
    restos = []
    # String para armazenar os dígitos decimais
    decimais = ""
    # Variável para indicar se o período foi encontrado
    periodo_encontrado = False
    
    # Loop para calcular os dígitos decimais até encontrar um período
    while resto != 0 and not periodo_encontrado:
        # Se o resto atual já foi encontrado, temos um período
        if resto in restos:
            # Encontra o índice do início do período
            indice_periodo = restos.index(resto)
            # Forma a string decimal com o período entre parênteses
            decimais = f"{decimais[:indice_periodo]}({decimais[indice_periodo:]})"
            # Marca que o período foi encontrado
            periodo_encontrado = True
        else:
            # Adiciona o resto atual à lista de restos encontrados
            restos.append(resto)
            # Multiplica o resto por 10 para continuar a divisão
            resto *= 10
            # Calcula o próximo dígito decimal
            decimal_atual = resto // fracao.denominator
            # Adiciona o dígito decimal à string de decimais
            decimais += str(decimal_atual)
            # Atualiza o resto da divisão
            resto %= fracao.denominator
    
    # Se não encontrou um período, adiciona todos os dígitos decimais ao resultado
    if not periodo_encontrado:
        resultado += decimais
    else:
        resultado += decimais
    
    # Retorna o resultado com a dízima periódica
    return resultado

# Função principal que gerencia a entrada do usuário e chama as funções apropriadas
def main():
    # Solicita ao usuário que informe o tipo de dízima ou conversão desejada
    tipo = input("Digite 'simples' para dízima periódica simples, 'composta' para dízima periódica composta, ou 'fracao' para converter uma fração para dízima: ").strip().lower()
    
    # Se o tipo for dízima periódica simples
    if tipo == 'simples':
        # Solicita ao usuário que informe o período da dízima
        periodo = input("Digite o período da dízima (ex: para 0.333..., digite '3'): ").strip()
        # Calcula a fração geratriz
        resultado = geratriz_dizima_simples(periodo)
        # Exibe o resultado
        print(f"A geratriz de 0.{periodo}... é: {resultado}")
    
    # Se o tipo for dízima periódica composta
    elif tipo == 'composta':
        # Solicita ao usuário que informe a parte não periódica da dízima composta
        nao_periodica = input("Digite a parte não periódica (ex: para 0.1234..., digite '12'): ").strip()
        # Solicita ao usuário que informe o período da dízima composta
        periodo = input("Digite o período da dízima (ex: para 0.1234..., digite '34'): ").strip()
        # Calcula a fração geratriz
        resultado = geratriz_dizima_composta(nao_periodica, periodo)
        # Exibe o resultado
        print(f"A geratriz de 0.{nao_periodica}({periodo})... é: {resultado}")
    
    # Se o tipo for conversão de fração para dízima
    elif tipo == 'fracao':
        # Solicita ao usuário que informe o numerador da fração
        numerador = int(input("Digite o numerador da fração: ").strip())
        # Solicita ao usuário que informe o denominador da fração
        denominador = int(input("Digite o denominador da fração: ").strip())
        # Cria uma fração com o numerador e o denominador fornecidos
        fracao = Fraction(numerador, denominador)
        # Converte a fração em dízima periódica
        resultado = dizima_a_partir_de_fracao(fracao)
        # Exibe o resultado
        print(f"A dízima periódica de {numerador}/{denominador} é: {resultado}")
    
    # Se o tipo informado for inválido
    else:
        # Exibe uma mensagem de erro
        print("Tipo inválido.")

# Executa a função principal se o script for executado diretamente
if __name__ == "__main__":
    main()
