<h1>Descrição do Projeto</h1>
<p>Este projeto consiste em duas funções principais que ajudam a calcular o valor de áreas marinhas com base em vários fatores e otimizar a alocação de recursos para maximizar o valor dessas áreas. As funções são escritas em Python utilizando a biblioteca scipy.optimize.</p>

<h2>Planejamento de Conservação Marinha</h2>
<h3>Programação de Alocação de Recursos</h3>
<p>Utilizamos programação dinâmica para otimizar a alocação de recursos limitados para a criação e manutenção de áreas marinhas protegidas. Este processo envolve:</p>
  <ul>
    <li>Modelagem de diferentes cenários de alocação de recursos.</li>
    <li>Seleção das áreas prioritárias para conservação, considerando critérios como biodiversidade, vulnerabilidade e conectividade.</li>
  </ul>
  
<h2>Funcionalidades</h2>
<ol>
<li>Calcular Valor de Área Marinha: Calcula o valor de uma área marinha com base em índices de biodiversidade, recursos naturais e atividades econômicas.</li>
<li>Otimizar Alocação de Recursos: Otimiza a alocação de recursos para maximizar o valor total das áreas marinhas, considerando restrições de custos e recursos disponíveis.</li>
</ol>

<h3>Dependências</h3>
<ul>
<li>Python 3.x</li>
<li>SciPy</li>
</ul>
  
<p>Para instalar a biblioteca SciPy, você pode usar o pip:</p>
<p>pip install scipy</p>

<h2>Funções</h2>
<h3>Função calcular_valor_area_marinha</h3>
<p>Calcula o valor de uma área marinha com base em fatores de biodiversidade, recursos naturais e atividades econômicas.</p>
<p>Parâmetros</p>
<ul>
  <li>biodiversidade (float): Índice de biodiversidade da área.</li>
  <li>recursos_naturais (float): Valor dos recursos naturais presentes na área.</li>
  <li>atividades_economicas (float): Valor das atividades econômicas na área.</li>
</ul>
<p>Retorno:</p>
<p>valor_total(float): Valor total da área marinha.</p>
<p>Corpo da Função:</p>

```
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
```
<h3>Função otimizar_alocacao_recursos</h3>
<p>Otimiza a alocação de recursos para maximizar o valor total das áreas marinhas.</p>
<p>Parâmetros</p>
<ul>
  <li>valores_areas (list): Lista dos valores das áreas marinhas.</li>
  <li>recursos_disponiveis (float): Total de recursos disponíveis.</li>
  <li>custos (list): Lista dos custos para alocar recursos em cada área.</li>
</ul>
<p>Retorno:</p>
<p>res.x(list): Quantidade de recursos alocados para cada área.</p>
<p>Corpo da Função:</p>

```
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

```

<h3>Exemplo de utilização de dados fictícios para encontrar a alocação ótima de recursos, utilizando as funções "calcular_valor_area_marinha" e "otimizar_alocacao_recursos" e um dicinário de objetos de áreas marinhas hipotéticas:</h3>

```
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
```
