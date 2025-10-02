import matplotlib.pyplot as plt

# Função para calcular a corrente em mA utilizando a Lei de Ohm: I = (V / R) * 1000
def calcular_corrente(tensao, resistencia):
    corrente_A = tensao / resistencia  # Corrente em amperes (A)
    corrente_mA = corrente_A * 1000  # Convertendo para miliampères (mA)
    return corrente_mA

# Valores das tensões (em volts) para o experimento
tensoes = [i for i in range(0, 10)]  # Tensões de 1V até 10V

# Resistores utilizados
resistor_100_ohm = 100  # Resistência do resistor de 100 Ω
resistor_1000_ohm = 1000  # Resistência do resistor de 1000 Ω

# Calculando as correntes para os dois resistores em mA
correntes_100_ohm = [calcular_corrente(tensao, resistor_100_ohm) for tensao in tensoes]
correntes_1000_ohm = [calcular_corrente(tensao, resistor_1000_ohm) for tensao in tensoes]

# Gráfico 1: Apenas Resistor de 100 Ω
plt.figure(figsize=(8, 6))
plt.plot(tensoes, correntes_100_ohm, label="Resistor de 100 Ω", marker='o', color='blue')
plt.title("Relação entre Tensão e Corrente - Resistor de 100 Ω", fontsize=14)
plt.xlabel("Tensão (V)", fontsize=12)
plt.ylabel("Corrente (mA)", fontsize=12)
plt.grid(True)
plt.xticks(tensoes)  # Exibe todos os pontos de tensão
plt.tight_layout()
plt.show()

# Gráfico 2: Apenas Resistor de 1000 Ω
plt.figure(figsize=(8, 6))
plt.plot(tensoes, correntes_1000_ohm, label="Resistor de 1000 Ω", marker='s', color='red')
plt.title("Relação entre Tensão e Corrente - Resistor de 1000 Ω", fontsize=14)
plt.xlabel("Tensão (V)", fontsize=12)
plt.ylabel("Corrente (mA)", fontsize=12)
plt.grid(True)
plt.xticks(tensoes)  # Exibe todos os pontos de tensão
plt.tight_layout()
plt.show()

# Gráfico 3: Resistor de 100 Ω e Resistor de 1000 Ω juntos
plt.figure(figsize=(8, 6))
plt.plot(tensoes, correntes_100_ohm, label="Resistor de 100 Ω", marker='o', color='blue')
plt.plot(tensoes, correntes_1000_ohm, label="Resistor de 1000 Ω", marker='s', color='red')
plt.title("Relação entre Tensão e Corrente - Resistores de 100 Ω e 1000 Ω", fontsize=14)
plt.xlabel("Tensão (V)", fontsize=12)
plt.ylabel("Corrente (mA)", fontsize=12)
plt.grid(True)
plt.xticks(tensoes)  # Exibe todos os pontos de tensão
plt.legend()
plt.tight_layout()
plt.show()
