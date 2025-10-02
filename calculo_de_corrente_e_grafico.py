import matplotlib.pyplot as plt

# --- FUNÇÕES ---

def calcular_corrente(tensao, resistencia):
    """
    Calcula a corrente elétrica (I) em miliampères (mA) com base na Lei de Ohm (I = V / R).

    Args:
        tensao (float/int): A tensão aplicada em Volts (V).
        resistencia (float/int): A resistência do componente em Ohms (Ω).

    Returns:
        float: A corrente resultante em miliampères (mA).
    """
    corrente_A = tensao / resistencia  # Corrente calculada em Ampères (A)
    corrente_mA = corrente_A * 1000    # Conversão de A para miliampères (mA)
    return corrente_mA

# --- CONFIGURAÇÃO DE CONSTANTES E DADOS ---

# Valores de Tensão (em Volts) a serem testados no experimento.
# Cria uma lista de [0, 1, 2, ..., 9]
tensoes = [i for i in range(0, 10)]

# Resistores utilizados (em Ohms)
resistor_100_ohm = 100   # Baixa resistência
resistor_1000_ohm = 1000 # Alta resistência

# --- CÁLCULOS PRINCIPAIS ---

# Aplica a função de cálculo a cada valor de tensão para o resistor de 100 Ω
correntes_100_ohm = [calcular_corrente(tensao, resistor_100_ohm) for tensao in tensoes]
# Aplica a função de cálculo a cada valor de tensão para o resistor de 1000 Ω
correntes_1000_ohm = [calcular_corrente(tensao, resistor_1000_ohm) for tensao in tensoes]

# --- PLOTAGEM DOS GRÁFICOS ---

# Gráfico 1: Análise Individual - Resistor de 100 Ω
plt.figure(figsize=(8, 6))
# Plota a linha (Tensão no X, Corrente no Y) com marcador de círculo
plt.plot(tensoes, correntes_100_ohm, label="Resistor de 100 Ω", marker='o', color='blue')

# Configurações estéticas
plt.title("Relação entre Tensão e Corrente - Resistor de 100 Ω", fontsize=14)
plt.xlabel("Tensão (V)", fontsize=12)
plt.ylabel("Corrente (mA)", fontsize=12)
plt.grid(True)
plt.xticks(tensoes)  # Garante que todos os valores de tensão sejam exibidos no eixo X
plt.tight_layout()   # Ajusta automaticamente os parâmetros do subplot para que caibam na figura
plt.show()

# Gráfico 2: Análise Individual - Resistor de 1000 Ω
plt.figure(figsize=(8, 6))
# Plota a linha (Tensão no X, Corrente no Y) com marcador de quadrado
plt.plot(tensoes, correntes_1000_ohm, label="Resistor de 1000 Ω", marker='s', color='red')

# Configurações estéticas
plt.title("Relação entre Tensão e Corrente - Resistor de 1000 Ω", fontsize=14)
plt.xlabel("Tensão (V)", fontsize=12)
plt.ylabel("Corrente (mA)", fontsize=12)
plt.grid(True)
plt.xticks(tensoes)
plt.tight_layout()
plt.show()

# Gráfico 3: Análise Comparativa - Resistores Juntos
plt.figure(figsize=(8, 6))
# Plota a curva do Resistor de 100 Ω
plt.plot(tensoes, correntes_100_ohm, label="Resistor de 100 Ω", marker='o', color='blue')
# Plota a curva do Resistor de 1000 Ω (menor inclinação = maior resistência)
plt.plot(tensoes, correntes_1000_ohm, label="Resistor de 1000 Ω", marker='s', color='red')

# Configurações estéticas
plt.title("Relação entre Tensão e Corrente - Resistores de 100 Ω e 1000 Ω", fontsize=14)
plt.xlabel("Tensão (V)", fontsize=12)
plt.ylabel("Corrente (mA)", fontsize=12)
plt.grid(True)
plt.xticks(tensoes)
plt.legend()         # Exibe a legenda para diferenciar as duas curvas
plt.tight_layout()
plt.show()
