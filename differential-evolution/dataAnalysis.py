import matplotlib.pyplot as plt
import pandas as pd


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




labels_1 = []
labels_2 = []
j=1
dejongCandlesDE = []
for series_name, series in df_dejong_de.items():
    labels_1.append(str(j))
    labels_2.append(str(j))
    j += 1
    dejongCandlesDE.append(series)

langCandlesDE = []
for series_name, series in df_lang_de.items():
    langCandlesDE.append(series)



# BOXPLOT ALL CONFIGS DE FOR DEJONG
labels_1[0] = "$\\bf{1}$"
labels_1[1] = "$\\bf{2}$"
labels_1[2] = "$\\bf{3}$"
labels_1[6] = "$\\bf{7}$"
labels_1[7] = "$\\bf{8}$"
labels_1[8] = "$\\bf{9}$"
labels_1[12] = "$\\bf{13}$"
labels_1[13] = "$\\bf{14}$"
labels_1[14] = "$\\bf{15}$"
labels_1[18] = "$\\bf{19}$"
labels_1[19] = "$\\bf{20}$"
labels_1[20] = "$\\bf{21}$"
plt.figure(figsize=(14,8))
plt.boxplot(dejongCandlesDE,
            patch_artist=True,
            vert=True,
            showfliers=False,
            labels=labels_1)

plt.grid(axis='y')
plt.xlabel("Config.")
plt.ylabel("$\\it{Fitness}$")
plt.title("$\\it{Boxplot}$ da execução da ED para função DeJong N.5")
plt.axvspan(1-0.4,1+0.4, color='green', alpha=0.2)
plt.axvspan(2-0.4,2+0.4, color='green', alpha=0.2)
plt.axvspan(3-0.4,3+0.4, color='green', alpha=0.2)
plt.axvspan(7-0.4,7+0.4, color='green', alpha=0.2)
plt.axvspan(8-0.4,8+0.4, color='green', alpha=0.2)
plt.axvspan(9-0.4,9+0.4, color='green', alpha=0.2)
plt.axvspan(13-0.4,13+0.4, color='green', alpha=0.2)
plt.axvspan(14-0.4,14+0.4, color='green', alpha=0.2)
plt.axvspan(15-0.4,15+0.4, color='green', alpha=0.2)
plt.axvspan(19-0.4,19+0.4, color='green', alpha=0.2)
plt.axvspan(20-0.4,20+0.4, color='green', alpha=0.2)
plt.axvspan(21-0.4,21+0.4, color='green', alpha=0.2)
#plt.savefig("differential-evolution/dejong_boxplot_all_config.pdf")


# BOXPLOT ALL CONFIGS DE FOR LANGERMANN
labels_2[18] = "$\\bf{19}$"
plt.figure(figsize=(14,8))
plt.boxplot(langCandlesDE,
            patch_artist=True,
            vert=True,
            showfliers=False,
            labels=labels_2)

plt.grid(axis='y')
plt.xlabel("Config.")
plt.ylabel("$\\it{Fitness}$")
plt.title("$\\it{Boxplot}$ da execução da ED para função Langermann")
plt.axvspan(19-0.4,19+0.4, color='green', alpha=0.2)
#plt.savefig("differential-evolution/lang_boxplot_all_config.pdf")




# BOXPLOT BEST GA VS PSO VS DE FOR DEJONG
best_dejong_pso = all_dejong_pso[23]
best_dejong_ga = list(df_dejong_ga["ga"])
best_dejong_de = dejongCandlesDE[18]


candles = [best_dejong_ga, best_dejong_pso, best_dejong_de]
candle_labels = ["GA", "PSO", "DE"]

plt.figure(figsize=(14,8))
plt.boxplot(candles,
            patch_artist=True,
            vert=True,
            labels=candle_labels,
            showfliers=False)

plt.grid(axis='y')
plt.ylabel("$\\it{Fitness}$")
plt.title("Comparação entre melhores configs. para GA, PSO e DE para função DeJong N.5")
#plt.savefig("differential-evolution/boxplot_GA_PSO_DE_DeJong5.pdf")


# BOXPLOT BEST GA VS PSO VS DE FOR LANGERMANN
best_lang_pso = all_langermann_pso[8]
best_lang_ga = list(df_lang_ga["ga"])
best_lang_de = langCandlesDE[18]


candles = [best_lang_ga, best_lang_pso, best_lang_de]
candle_labels = ["GA", "PSO", "DE"]

plt.figure(figsize=(14,8))
plt.boxplot(candles,
            patch_artist=True,
            vert=True,
            labels=candle_labels,
            showfliers=False)

plt.grid(axis='y')
plt.ylabel("$\\it{Fitness}$")
plt.title("Comparação entre melhores configs. para GA, PSO e DE para função Langermann")
#plt.savefig("differential-evolution/boxplot_GA_PSO_DE_lang.pdf")






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


plt.figure(figsize=(10,6))
plt.plot(dejong5_torneio_melhores, label="Melhor $\\it{Fitness}$ por geração para GA")
plt.plot(dejong5_pso_melhores, label="Melhor $\\it{Fitness}$ por geração para PSO")
plt.plot(dejong5_de_melhores, label="Melhor $\\it{Fitness}$ por geração para DE")
plt.xlabel("$\\it{epoch}$")
plt.ylabel("$\\it{Fitness}$")
plt.title("Evolução de $\\it{Fitness}$ PSO vs. GA vs. DE para Função DeJong N. 5")
plt.grid(axis='y')
plt.legend()
plt.savefig("differential-evolution/evolucao_fitness_GA_vs_PSO_vs_DE_DeJong5.pdf")






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


plt.figure(figsize=(10,6))
plt.plot(lang_torneio_melhores, label="Melhor $\\it{Fitness}$ por geração para GA")
plt.plot(lang_pso_melhores, label="Melhor $\\it{Fitness}$ por geração para PSO")
plt.plot(lang_de_melhores, label="Melhor $\\it{Fitness}$ por geração para DE")
plt.xlabel("$\\it{epoch}$")
plt.ylabel("$\\it{Fitness}$")
plt.title("Evolução de $\\it{Fitness}$ GA vs. PSO vs. DE para Função Langermann")
plt.grid(axis='y')
plt.legend()
plt.savefig("differential-evolution/evolucao_fitness_GA_vs_PSO_vs_DE_Langermann.pdf")





#plt.show()


"""


df_lang_roullete = pd.DataFrame()

labels = []
for i in range(1, 31):
    config = "c" + str(i)
    file = "Resultado/Langermann/Roleta/Conf" + str(i) + "_Roleta_Langermann.csv"

    df_lang_roullete[config] = pd.read_csv(file, header=None)
    labels.append(str(i))

lang_roullete_no_elitism = []
lang_roullete_elitism = []

for series_name, series in df_lang_roullete.items():
    if int(series_name.removeprefix("c")) <= 15:
        lang_roullete_no_elitism.append(series)
    else:
        lang_roullete_elitism.append(series)




labels[17] = "$\\bf{18}$"
plt.figure(figsize=(14,8))
plt.boxplot(lang_roullete_no_elitism + lang_roullete_elitism,
            patch_artist=True,
            vert=True,
            labels=labels)

plt.grid(axis='y')
plt.xlabel("Config.")
plt.ylabel("$\\it{Fitness}$")
plt.title("$\\it{Boxplot}$ da execução do AG para função Langermann com seleção por roleta")
plt.axvspan(18-0.4,18+0.4, color='green', alpha=0.2)
plt.savefig("lang_roleta_boxplot.pdf")
labels[17] = "18"

"""