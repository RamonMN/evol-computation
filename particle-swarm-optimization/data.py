import pandas as pd
import matplotlib.pyplot as plt


configs_dejong = []
configs_langermann = []
configs_labels = []


df = pd.read_csv("out.csv", sep=";")


# 27 boxplot PSO dejong
for i in range(1, 28):
    configs_dejong.append(list(df["config" + str(i - 1)]))
    configs_labels.append(str(i))

configs_labels[23] = "$\\bf{24}$"
plt.figure(figsize=(14,8))
plt.boxplot(configs_dejong,
            patch_artist=True,
            vert=True,
            labels=configs_labels,
            showfliers=False)

plt.grid(axis='y')
plt.xlabel("Config.")
plt.ylabel("$\\it{Fitness}$")
plt.title("$\\it{Boxplot}$ da execução do PSO para função DeJong N.5")
plt.axvspan(24-0.4,24+0.4, color='green', alpha=0.2)
configs_labels[23] = "24"
plt.savefig("boxplot_27configs_PSO_DeJong5.pdf")



# 27 boxplot PSO langermann
for i in range(28, 55):
    configs_langermann.append(list(df["config" + str(i - 1)]))

configs_labels[8] = "$\\bf{9}$"
plt.figure(figsize=(14,8))
plt.boxplot(configs_langermann,
            patch_artist=True,
            vert=True,
            labels=configs_labels,
            showfliers=False)

plt.grid(axis='y')
plt.xlabel("Config.")
plt.ylabel("$\\it{Fitness}$")
plt.title("$\\it{Boxplot}$ da execução do PSO para função Langermann")
plt.axvspan(9-0.4,9+0.4, color='green', alpha=0.2)
configs_labels[8] = "9"
plt.savefig("boxplot_27configs_PSO_Langermann.pdf")


# 2 boxplot PSO vs GA dejong
# DeJong5 function with tournament method
df_dejong_ga = pd.DataFrame()
df_dejong_ga["ga"] = pd.read_csv("genetic-algo/Resultado/DeJong5/Torneio/Conf17_Torneio_DeJong.csv", header=None)
best_dejong_pso = configs_dejong[23]
best_dejong_ga = list(df_dejong_ga["ga"])

candles = [best_dejong_ga, best_dejong_pso]
candle_labels = ["GA", "PSO"]

plt.figure(figsize=(14,8))
plt.boxplot(candles,
            patch_artist=True,
            vert=True,
            labels=candle_labels,
            showfliers=False)

plt.grid(axis='y')
plt.ylabel("$\\it{Fitness}$")
plt.title("Comparação entre melhores configs. para GA e PSO para função DeJong N.5")
plt.savefig("boxplot_best_GA_vs_best_PSO_DeJong5.pdf")


# 2 boxplot PSO vs GA Langermann
df_lang_ga = pd.DataFrame()
df_lang_ga["ga"] = pd.read_csv("genetic-algo/Resultado/Langermann/Torneio/Conf20_Torneio_Langermann.csv", header=None)
best_lang_pso = configs_langermann[8]
best_lang_ga = list(df_lang_ga["ga"])

candles_lang = [best_lang_ga, best_lang_pso]

plt.figure(figsize=(14,8))
plt.boxplot(candles_lang,
            patch_artist=True,
            vert=True,
            labels=candle_labels,
            showfliers=False)

plt.grid(axis='y')
plt.ylabel("$\\it{Fitness}$")
plt.title("Comparação entre melhores configs. para GA e PSO para função Langermann")
plt.savefig("boxplot_best_GA_vs_best_PSO_Langermann.pdf")




# evolucao de fitness torneio
dejong5_torneio = pd.read_csv("genetic-algo/Resultado/FitnessMelhor_Media_DeJongN5_Torneio.csv", header=None)
dejong5_torneio_melhores = []
for index, value in enumerate(dejong5_torneio[0]):
    if (index%2) == 0:
        dejong5_torneio_melhores.append(value)


dejong5_pso = pd.read_csv("dejong_best.csv")
dejong5_pso_melhores = dejong5_pso["dejong"]



plt.figure(figsize=(10,6))
plt.plot(dejong5_torneio_melhores, label="Melhor $\\it{Fitness}$ por geração para GA")
plt.plot(dejong5_pso_melhores, label="Melhor $\\it{Fitness}$ por geração para PSO")
plt.xlabel("$\\it{epoch}$")
plt.ylabel("$\\it{Fitness}$")
plt.title("Evolução de $\\it{Fitness}$ PSO vs. GA para Função DeJong N. 5")
plt.grid(axis='y')
plt.legend()
plt.savefig("evolucao_fitness_GA_vs_PSO_DeJong5.pdf")



# evolucao de fitness langermann
lang_torneio = pd.read_csv("genetic-algo/Resultado/FitnessMelhor_Media_Langermann_Torneio.csv", header=None)
lang_torneio_melhores = []
for index, value in enumerate(lang_torneio[0]):
    if (index%2) == 0:
        lang_torneio_melhores.append(value)


lang_pso = pd.read_csv("lang_best.csv")
lang_pso_melhores = lang_pso["lang"]


plt.figure(figsize=(10,6))
plt.plot(lang_torneio_melhores, label="Melhor $\\it{Fitness}$ por geração para GA")
plt.plot(lang_pso_melhores, label="Melhor $\\it{Fitness}$ por geração para PSO")
plt.xlabel("$\\it{epoch}$")
plt.ylabel("$\\it{Fitness}$")
plt.title("Evolução de $\\it{Fitness}$ GA vs. PSO para Função Langermann")
plt.grid(axis='y')
plt.legend()
plt.savefig("evolucao_fitness_GA_vs_PSO_Langermann.pdf")


plt.show()






"""
# DeJong5
df_dejong = pd.DataFrame()

labels = []
for i in range(1, 28):
    config = "c" + str(i)
    file = "out.csv"

    df_dejong[config] = pd.read_csv(file, header=None)
    labels.append(str(i))

lang_roullete_no_elitism = []
lang_roullete_elitism = []

for series_name, series in df_lang_roullete.items():
    if int(series_name.removeprefix("c")) <= 15:
        lang_roullete_no_elitism.append(series)
    else:
        lang_roullete_elitism.append(series)



all_lang_roullete = lang_roullete_no_elitism + lang_roullete_elitism    

lang_roullete_medians = []

for series in all_lang_roullete:
    lang_roullete_medians.append(series.median())

best_lang_roullete = lang_roullete_medians.index(min(lang_roullete_medians)) + 1

print(f"lang (roullete): config {best_lang_roullete}  median {min(lang_roullete_medians)}")


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