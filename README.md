# ⚡ Ohm Law Visualizer: Demonstração Gráfica em Python

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![Matplotlib](https://img.shields.io/badge/Library-Matplotlib-blue.svg)]()

Este projeto Python demonstra o princípio fundamental da **Lei de Ohm ($V=R \cdot I$)** através de visualizações gráficas geradas pela biblioteca **Matplotlib**.

O script calcula a corrente em miliampères ($\text{mA}$) para uma variação de tensão em dois resistores de valores distintos ($\mathbf{100\,\Omega}$ e $\mathbf{1000\,\Omega}$) e plota os resultados em gráficos individuais e combinados, ilustrando a relação linear entre tensão e corrente.

## ✨ Conceitos e Características

* **Relação Linear:** O gráfico resultante é uma linha reta, provando que, para um resistor fixo, $V$ é diretamente proporcional a $I$.
* **Lei de Ohm:** Implementa a fórmula $I = V/R$ e realiza a conversão para miliampères ($I_{\text{mA}} = I_{\text{A}} \cdot 1000$).
* **Análise de Resistência:** Demonstra que um resistor de maior valor (maior inclinação da reta $R$) resulta em uma corrente menor para a mesma tensão.
* **Visualização:** Gera três gráficos distintos para análise: individual e comparativo.

---

## 🚀 Guia de Início Rápido

### Pré-requisitos
Certifique-se de ter o **Python (3.6 ou superior)** instalado.

### 1. Clonagem e Dependências
Clone o repositório (usando seu usuário `bizogue`) e instale a única dependência necessária para os gráficos:

```bash
git clone [https://github.com/bizogue/ohm-law-visualizer-python.git](https://github.com/bizogue/ohm-law-visualizer-python.git)
cd ohm-law-visualizer-python
pip install matplotlib
