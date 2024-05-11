import matplotlib.pyplot as plt
import pandas as pd

# Clonal Selection Algorithm dataframes
df_dejong_csa = pd.read_csv("clonal-selection-algorithm/dejong_configs_clonalg.csv", sep=";")
df_lang_csa = pd.read_csv("clonal-selection-algorithm/lang_configs_clonalg.csv", sep=";")

# Differential evolution dataframes
df_dejong_de = pd.read_csv("differential-evolution/dejong_configs.csv", sep=";")
df_lang_de = pd.read_csv("differential-evolution/lang_configs.csv", sep=";")

# Genetic algorithm dataframes
df_dejong_ga = pd.DataFrame()
df_dejong_ga["ga"] = pd.read_csv("genetic-algo/Resultado/DeJong5/Torneio/Conf17_Torneio_DeJong.csv", header=None)

df_lang_ga = pd.DataFrame()
df_lang_ga["ga"] = pd.read_csv("genetic-algo/Resultado/Langermann/Torneio/Conf20_Torneio_Langermann.csv", header=None)

# Particle swarm optimization dataframes
df_all_pso = pd.read_csv("particle-swarm-optimization/results/out.csv", sep=";")

all_dejong_pso = []
all_langermann_pso = []

for i in range(1, 28):
    all_dejong_pso.append(list(df_all_pso["config" + str(i - 1)]))

for i in range(28, 55):
    all_langermann_pso.append(list(df_all_pso["config" + str(i - 1)]))

#print(f"dejong -> media-mediana-max-min")
#for series_name, series in df_dejong_csa.items():
#    print(f"{series.mean()};{series.median()};{series.max()};{series.min()}")

#print(f"lang -> media-mediana-max-min")
#for series_name, series in df_lang_csa.items():
#    print(f"{series.mean()};{series.median()};{series.max()};{series.min()}")


labels_1 = []
dejongCandlesCSA = []
j=1
for series_name, series in df_dejong_csa.items():
    labels_1.append(str(j))
    j += 1
    dejongCandlesCSA.append(series)


"""
labels_2 = []
langCandlesCSA = []
j=1
for series_name, series in df_lang_csa.items():
    labels_2.append(str(j))
    j+=1
    langCandlesCSA.append(series)
"""


# BOXPLOT ALL CONFIGS DE FOR DEJONG
#labels_1[3] = "$\\bf{4}$"
#plt.figure(figsize=(14,8))
#plt.boxplot(dejongCandlesCSA,
#            patch_artist=True,
#            vert=True,
#            showfliers=False,
#            labels=labels_1)

#plt.grid(axis='y')
#plt.xlabel("Config.")
#plt.ylabel("$\\it{Fitness}$")
#plt.title("$\\it{Boxplot}$ da execução da CLONALG para função DeJong N.5")
#plt.axvspan(4-0.4,4+0.4, color='green', alpha=0.2)
#plt.savefig("clonal-selection-algorithm/dejong_boxplot_all_config_csa.pdf")


"""
# BOXPLOT ALL CONFIGS DE FOR LANGERMANN
labels_2[7] = "$\\bf{8}$"
plt.figure(figsize=(14,8))
plt.boxplot(langCandlesCSA,
            patch_artist=True,
            vert=True,
            showfliers=False,
            labels=labels_2)

plt.grid(axis='y')
plt.xlabel("Config.")
plt.ylabel("$\\it{Fitness}$")
plt.title("$\\it{Boxplot}$ da execução da CLONALG para função Langermann")
plt.axvspan(8-0.4,8+0.4, color='green', alpha=0.2)
#plt.savefig("clonal-selection-algorithm/lang_boxplot_all_config_csa.pdf")
"""


# BOXPLOT BEST GA VS PSO VS DE FOR DEJONG
#best_dejong_pso = all_dejong_pso[23]
#best_dejong_ga = list(df_dejong_ga["ga"])
#best_dejong_de = list(df_dejong_de["config19"])
#best_dejong_csa = dejongCandlesCSA[3]


#candles = [best_dejong_ga, best_dejong_pso, best_dejong_de, best_dejong_csa]
#candle_labels = ["GA", "PSO", "DE", "CLONALG"]

#plt.figure(figsize=(14,8))
#plt.boxplot(candles,
#            patch_artist=True,
#            vert=True,
#            labels=candle_labels,
#            showfliers=False)

#plt.grid(axis='y')
#plt.ylabel("$\\it{Fitness}$")
#plt.title("Comparação entre melhores configs. para GA, PSO, DE e CLONALG para função DeJong N.5")
#plt.savefig("clonal-selection-algorithm/boxplot_GA_PSO_DE_CSA_DeJong5.pdf")
#plt.show()

"""
# BOXPLOT BEST GA VS PSO VS DE FOR LANGERMANN
best_lang_pso = all_langermann_pso[8]
best_lang_ga = list(df_lang_ga["ga"])
best_lang_de = list(df_lang_de["config19"])
best_lang_csa = langCandlesCSA[7]


candles = [best_lang_ga, best_lang_pso, best_lang_de, best_lang_csa]
candle_labels = ["GA", "PSO", "DE", "CLONALG"]

plt.figure(figsize=(14,8))
plt.boxplot(candles,
            patch_artist=True,
            vert=True,
            labels=candle_labels,
            showfliers=False)

plt.grid(axis='y')
plt.ylabel("$\\it{Fitness}$")
plt.title("Comparação entre melhores configs. para GA, PSO, DE e CLONALG para função Langermann")
#plt.savefig("clonal-selection-algorithm/boxplot_GA_PSO_DE_CSA_lang.pdf")
"""



# FITNESS PER EPOCH DEJONG
dejong5_torneio = pd.read_csv("genetic-algo/Resultado/FitnessMelhor_Media_DeJongN5_Torneio.csv", header=None)
dejong5_torneio_melhores = []
for index, value in enumerate(dejong5_torneio[0]):
    if (index%2) == 0:
        dejong5_torneio_melhores.append(value)


dejong5_pso = pd.read_csv("particle-swarm-optimization/results/dejong_best.csv")
dejong5_pso_melhores = dejong5_pso["dejong"]

dejong5_de = pd.read_csv("differential-evolution/de_dejong_best.csv")
dejong5_de_melhores = dejong5_de["dejong"]

dejong_csa = pd.read_csv("clonal-selection-algorithm/csa_dejong_best.csv")
dejong_csa_melhores = dejong_csa["dejong"]

plt.figure(figsize=(10,6))
plt.plot(dejong5_torneio_melhores, label="Melhor $\\it{Fitness}$ por geração para GA")
plt.plot(dejong5_pso_melhores, label="Melhor $\\it{Fitness}$ por geração para PSO")
plt.plot(dejong5_de_melhores, label="Melhor $\\it{Fitness}$ por geração para DE")
plt.plot(dejong_csa_melhores, label="Melhor $\\it{Fitness}$ por geração para CLONALG")
plt.xlabel("$\\it{epoch}$")
plt.ylabel("$\\it{Fitness}$")
plt.title("Evolução de $\\it{Fitness}$ PSO vs. GA vs. DE para Função DeJong N. 5")
plt.grid(axis='y')
plt.legend()
plt.savefig("clonal-selection-algorithm/evolucao_fitness_GA_vs_PSO_vs_DE_vs_CSA_DeJong5.pdf")

plt.show()


"""

# FITNESS PER EPOCH LANG
lang_torneio = pd.read_csv("genetic-algo/Resultado/FitnessMelhor_Media_Langermann_Torneio.csv", header=None)
lang_torneio_melhores = []
for index, value in enumerate(lang_torneio[0]):
    if (index%2) == 0:
        lang_torneio_melhores.append(value)


lang_pso = pd.read_csv("particle-swarm-optimization/results/lang_best.csv")
lang_pso_melhores = lang_pso["lang"]

lang_de = pd.read_csv("differential-evolution/de_lang_best.csv")
lang_de_melhores = lang_de["lang"]

lang_csa = pd.read_csv("clonal-selection-algorithm/csa_lang_best.csv")
lang_csa_melhores = lang_csa["lang"]


plt.figure(figsize=(10,6))
plt.plot(lang_torneio_melhores, label="Melhor $\\it{Fitness}$ por geração para GA")
plt.plot(lang_pso_melhores, label="Melhor $\\it{Fitness}$ por geração para PSO")
plt.plot(lang_de_melhores, label="Melhor $\\it{Fitness}$ por geração para DE")
plt.plot(lang_csa_melhores, label="Melhor $\\it{Fitness}$ por geração para CLONALG")
plt.xlabel("$\\it{epoch}$")
plt.ylabel("$\\it{Fitness}$")
plt.title("Evolução de $\\it{Fitness}$ GA vs. PSO vs. DE para Função Langermann")
plt.grid(axis='y')
plt.legend()
plt.savefig("clonal-selection-algorithm/evolucao_fitness_GA_vs_PSO_vs_DE_vs_CSA_Langermann.pdf")

plt.show()

"""