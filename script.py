# 1CCPZ
# Integrantes:
# Giovane Salazar - RM:570396
# Leonardo Takachi - RM:569066

import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

# Conjunto de dados:
dados = pd.read_csv("space_missions_dataset.csv")

#######################################
# Tabela de Distribuição de Frequência - Variável Quantitativa Discreta - Tamanho da tripulação
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# Frequência absoluta
freq_abs = dados['Crew Size'].value_counts().sort_index()

# Frequência relativa
freq_rel = dados['Crew Size'].value_counts(normalize=True).sort_index() * 100

# Frequência acumulada
freq_acum = freq_abs.cumsum()

# Frequência relativa acumulada
freq_rel_acum = freq_rel.cumsum()

# Criar tabela de frequência
tabela_freq = pd.DataFrame({
    "Frequência Absoluta": freq_abs,
    "Freq. Relativa (%)": freq_rel.round(2),
    "Freq. Acumulada": freq_acum,
    "Freq. Rel. Acumulada (%)": freq_rel_acum.round(2)
})

# Mostrar tabela
print("\nTABELA DE DISTRIBUIÇÃO DE FREQUÊNCIA VARIÁVEL QUANTITATIVA DISCRETA - TAMANHO DA TRIPULAÇÃO\n")
print(tabela_freq)

#######################################
# Tabela de Distribuição de Frequência - Variável Quantitativa Contínua - Duração da missão
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# Número de classes
k = 7

# Criar classes/intervalos
classes = pd.cut(dados['Mission Duration (years)'], bins=k)

# Frequência absoluta
freq_abs = classes.value_counts().sort_index()

# Frequência relativa
freq_rel = (freq_abs / freq_abs.sum()) * 100

# Frequência acumulada
freq_acum = freq_abs.cumsum()

# Frequência relativa acumulada
freq_rel_acum = freq_rel.cumsum()

# Criar tabela
tabela_freq = pd.DataFrame({
    "Frequência Absoluta": freq_abs,
    "Freq. Relativa (%)": freq_rel.round(2),
    "Freq. Acumulada": freq_acum,
    "Freq. Rel. Acumulada (%)": freq_rel_acum.round(2)
})

# Mostrar tabela
print("\nTABELA DE DISTRIBUIÇÃO DE FREQUÊNCIA VARIÁVEL QUANTITATIVA CONTÍNUA - DURAÇÃO DA MISSÃO (ANOS)\n")
print(tabela_freq)

#######################################
# Gráfico 1 - Variável Qualitativa Nominal
# Gráfico Pizza - Tipo de Missão:

missiontype_counts = dados['Mission Type'].value_counts()

plt.figure(figsize=(8, 8))

plt.pie(
    missiontype_counts,
    labels=missiontype_counts.index,
    autopct='%1.1f%%'
)
plt.title('Tipos de Missões realizadas')
plt.show()

#######################################
# Gráfico 2 - Variável Quantitativa Contínua
# Gráfico Histograma - Duração da missão

plt.hist(dados['Mission Duration (years)'], bins=7)

plt.title('Distribuição da Duração das Missões')
plt.xlabel('Duração da Missão (anos)')
plt.ylabel('Frequência')
plt.show()

#######################################
# Variável 1 - Quantitativa Contínua - Duração da missão
# Medidas de Tendência Central
print('\nMEDIDAS DE TENDÊNCIA CENTRAL - DURAÇÃO DA MISSÃO (ANOS)\n')

media_missionduration = dados['Mission Duration (years)'].mean()
mediana_missionduration = dados['Mission Duration (years)'].median()
moda_missionduration = dados['Mission Duration (years)'].mode()[0]

print(f'Média: {media_missionduration:.2f}')
print(f'Mediana: {mediana_missionduration:.2f}')
print(f'Moda: {moda_missionduration:.2f}')

# Medidas de Dispersão
print('\nMEDIDAS DE DISPERSÃO - DURAÇÃO DA MISSÃO (ANOS)\n')
maximo_missionduration = dados['Mission Duration (years)'].max()
minimo_missionduration = dados['Mission Duration (years)'].min()
amplitude_missionduration = dados['Mission Duration (years)'].max(
) - dados['Mission Duration (years)'].min()
variancia_missionduration = dados['Mission Duration (years)'].var()
desvio_padrao_missionduration = dados['Mission Duration (years)'].std()
coeficiente_variacao_missionduration = (
    desvio_padrao_missionduration / media_missionduration) * 100

print(f"Máximo: {maximo_missionduration}")
print(f"Mínimo: {minimo_missionduration}")
print(f"Amplitude: {amplitude_missionduration}")
print(f"Variância: {variancia_missionduration:.2f}")
print(f"Desvio padrão: {desvio_padrao_missionduration:.2f}")
print(
    f"Coeficiente de variação (%): {coeficiente_variacao_missionduration:.2f}")

# Medidas Separatrizes
print('\nMEDIDAS SEPARATRIZES - DURAÇÃO DA MISSÃO (ANOS)\n')

quartis_missionduration = dados['Mission Duration (years)'].quantile([
    0.25, 0.50, 0.75])

print('Quartis:')
print(quartis_missionduration)

#######################################
# Variável 2 - Quantitativa Discreta - Duração da missão
# Medidas de Tendência Central
print('\nMEDIDAS DE TENDÊNCIA CENTRAL - TAMANHO DA TRIPULAÇÃO (PESSOAS)\n')

media_crewsize = dados['Crew Size'].mean()
mediana_crewsize = dados['Crew Size'].median()
moda_crewsize = dados['Crew Size'].mode()[0]

print(f'Média: {media_crewsize:.2f}')
print(f'Mediana: {mediana_crewsize:.2f}')
print(f'Moda: {moda_crewsize:.2f}')

# Medidas de Dispersão
print('\nMEDIDAS DE DISPERSÃO - TAMANHO DA TRIPULAÇÃO (PESSOAS)\n')
maximo_crewsize = dados['Crew Size'].max()
minimo_crewsize = dados['Crew Size'].min()
amplitude_crewsize = dados['Crew Size'].max() - dados['Crew Size'].min()
variancia_crewsize = dados['Crew Size'].var()
desvio_padrao_crewsize = dados['Crew Size'].std()
coeficiente_variacao_crewsize = (desvio_padrao_crewsize / media_crewsize) * 100

print(f"Máximo: {maximo_crewsize}")
print(f"Mínimo: {minimo_crewsize}")
print(f"Amplitude: {amplitude_crewsize}")
print(f"Variância: {variancia_crewsize:.2f}")
print(f"Desvio padrão: {desvio_padrao_crewsize:.2f}")
print(f"Coeficiente de variação (%): {coeficiente_variacao_crewsize:.2f}")

# Medidas Separatrizes
print('\nMEDIDAS SEPARATRIZES - TAMANHO DA TRIPULAÇÃO (PESSOAS)\n')

quartis_crewsize = dados['Crew Size'].quantile([0.25, 0.50, 0.75])

print('Quartis:')
print(quartis_crewsize)