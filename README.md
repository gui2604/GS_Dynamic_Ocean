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
  <li>biodiversidade = 80</li>
  <li>recursos_naturais = 100</li>
  <li>atividades_economicas = 120</li>
</ul>
<p>Corpo da Função:</p>
<span>
    peso_biodiversidade = 0.4<br>
    peso_recursos_naturais = 0.3<br>
    peso_atividades_economicas = 0.3<br>
    valor_total = (<br>
            peso_biodiversidade * biodiversidade +<br>
            peso_recursos_naturais * recursos_naturais +<br>
            peso_atividades_economicas * atividades_economicas<br>
    )<br>
    return valor_total
</span>
<p>Exemplo de Uso da função:</p>
<span>valor_area = calcular_valor_area_marinha(biodiversidade, recursos_naturais, atividades_economicas)
print(f"O valor da área marinha é: {valor_area:.2f}")</span>

<div></div>

##Função otimizar_alocacao_recursos
Otimiza a alocação de recursos para maximizar o valor total das áreas marinhas.
Parâmetros
valores_areas (list): Lista dos valores das áreas marinhas.
recursos_disponiveis (float): Total de recursos disponíveis.
custos (list): Lista dos custos para alocar recursos em cada área.
Retorno
list: Quantidade de recursos alocados para cada área.
Exemplo
valores_areas = [500, 600, 700, 800]
recursos_disponiveis = 1000
custos = [100, 150, 200, 250]
alocacao_otima = otimizar_alocacao_recursos(valores_areas, recursos_disponiveis, custos)
print(f"A alocação ótima de recursos é: {alocacao_otima}")

<div></div>



