from scipy.optimize import linprog
def calcular_valor_area_marinha(biodiversidade, recursos_naturais, atividades_economicas):
    """
    Calcula o valor de uma área marinha com base em vários fatores.

    Args:
    biodiversidade (float): Índice de biodiversidade da área.
    recursos_naturais (float): Valor dos recursos naturais presentes na área.
    atividades_economicas (float): Valor das atividades econômicas na área.

    Retorna:
    float: Valor total da área marinha.
    """
    # Pesos fictícios para cada fator
    peso_biodiversidade = 0.4
    peso_recursos_naturais = 0.3
    peso_atividades_economicas = 0.3

    # Calcula o valor total
    valor_total = (
            peso_biodiversidade * biodiversidade +
            peso_recursos_naturais * recursos_naturais +
            peso_atividades_economicas * atividades_economicas
    )

    return valor_total

def otimizar_alocacao_recursos(valores_areas, recursos_disponiveis, custos):
    """
    Otimiza a alocação de recursos para maximizar o valor das áreas marinhas.

    Args:
    valores_areas (list): Lista dos valores das áreas marinhas.
    recursos_disponiveis (float): Total de recursos disponíveis.
    custos (list): Lista dos custos para alocar recursos em cada área.

    Retorna:
    list: Quantidade de recursos alocados para cada área.
    """
    # Número de áreas
    num_areas = len(valores_areas)

    # Função objetivo (maximizar valor -> minimizar negativo do valor)
    c = [-valor for valor in valores_areas]

    # Restrições de recursos
    A = [custos]
    b = [recursos_disponiveis]

    # Limites de variáveis (não-negatividade)
    x_bounds = [(0, None) for _ in range(num_areas)]

    # Resolução do problema de otimização
    res = linprog(c, A_ub=A, b_ub=b, bounds=x_bounds, method='highs')

    # Verifica se a solução é viável
    if res.success:
        return res.x
    else:
        raise ValueError("Não foi possível encontrar uma solução ótima")




# Exemplo de cálculo de área marinha
biodiversidade = 80
recursos_naturais = 100
atividades_economicas = 120
valor_area = calcular_valor_area_marinha(biodiversidade, recursos_naturais, atividades_economicas)
print(f"O valor da área marinha é: {valor_area:.16e}")
print()

###########################################################################################################################################################################

# Exemplo de cáclulo de otimização de alocação de recursos
valores_areas = [500, 600, 700, 800]
recursos_disponiveis = 1000
custos = [100, 150, 200, 250]
alocacao_otima = otimizar_alocacao_recursos(valores_areas, recursos_disponiveis, custos)
print(f"A alocação ótima de recursos (otimizada) é: {[f'{x:.16e}' for x in alocacao_otima]}")
print()


############################################################################################################################################################################

# Dados fictícios para encontrar a alocação ótima de recursos.
dados_areas = [
    {"biodiversidade": 80, "recursos_naturais": 100, "atividades_economicas": 120},
    {"biodiversidade": 90, "recursos_naturais": 110, "atividades_economicas": 130},
    {"biodiversidade": 85, "recursos_naturais": 95, "atividades_economicas": 125},
    {"biodiversidade": 95, "recursos_naturais": 105, "atividades_economicas": 135},
]
# Calcular o valor de cada área marinha
valores_areas = [calcular_valor_area_marinha(area["biodiversidade"], area["recursos_naturais"], area["atividades_economicas"]) for area in dados_areas]

# Recursos disponíveis e custos fictícios
recursos_disponiveis = 500
custos = [100, 150, 200, 250]

# Encontrar a alocação ótima de recursos
alocacao_otima = otimizar_alocacao_recursos(valores_areas, recursos_disponiveis, custos)

# Exibir resultados
print(f"Valores das áreas marinhas: {[f'{valor:.16e}' for valor in valores_areas]}")
print(f"Alocação ótima de recursos:{[f'{x:.16e}' for x in alocacao_otima]}")
