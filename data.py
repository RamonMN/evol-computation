import pandas as pd
import matplotlib.pyplot as plt


# Langermann function with roullete method
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




# Langermann function with tournament method
df_lang_tournament = pd.DataFrame()

for i in range(1, 31):
    config = "c" + str(i)
    file = "Resultado/Langermann/Torneio/Conf" + str(i) + "_Torneio_Langermann.csv"

    df_lang_tournament[config] = pd.read_csv(file, header=None)

lang_tournament_no_elitism = []
lang_tournament_elitism = []

for series_name, series in df_lang_tournament.items():
    if int(series_name.removeprefix("c")) <= 15:
        lang_tournament_no_elitism.append(series)
    else:
        lang_tournament_elitism.append(series)



all_lang_tournament = lang_tournament_no_elitism + lang_tournament_elitism    

lang_tournament_medians = []

for series in all_lang_tournament:
    lang_tournament_medians.append(series.median())

best_lang_tournament = lang_tournament_medians.index(min(lang_tournament_medians)) + 1

print(f"lang (tournament): config {best_lang_tournament}  median {min(lang_tournament_medians)}")


labels[19] = "$\\bf{20}$"
plt.figure(figsize=(14,8))
plt.boxplot(lang_tournament_no_elitism + lang_tournament_elitism,
            patch_artist=True,
            vert=True,
            labels=labels)

plt.grid(axis='y')
plt.xlabel("Config.")
plt.ylabel("$\\it{Fitness}$")
plt.title("$\\it{Boxplot}$ da execução do AG para função Langermann com seleção por torneio")
plt.axvspan(20-0.4,20+0.4, color='green', alpha=0.2)
plt.savefig("lang_torneio_boxplot.pdf")
labels[19] = "20"






# DeJong5 function with roullete method
df_dejong_roullete = pd.DataFrame()

for i in range(1, 31):
    config = "c" + str(i)
    file = "Resultado/DeJong5/Roleta/Conf" + str(i) + "_Roleta_DeJong.csv"

    df_dejong_roullete[config] = pd.read_csv(file, header=None)

dejong_roullete_no_elitism = []
dejong_roullete_elitism = []

for series_name, series in df_dejong_roullete.items():
    if int(series_name.removeprefix("c")) <= 15:
        dejong_roullete_no_elitism.append(series)
    else:
        dejong_roullete_elitism.append(series)


all_dejong_roullete = dejong_roullete_no_elitism + dejong_roullete_elitism    

dejong_roullete_medians = []

for series in all_dejong_roullete:
    dejong_roullete_medians.append(series.median())

best_dejong_roullete = dejong_roullete_medians.index(min(dejong_roullete_medians)) + 1

print(f"DeJong5 (roullete): config {best_dejong_roullete}  median {min(dejong_roullete_medians)}")



labels[23] = "$\\bf{24}$"
plt.figure(figsize=(14,8))
plt.boxplot(dejong_roullete_no_elitism + dejong_roullete_elitism,
            patch_artist=True,
            vert=True,
            labels=labels)

plt.grid(axis='y')
plt.xlabel("Config.")
plt.ylabel("$\\it{Fitness}$")
plt.title("$\\it{Boxplot}$ da execução do AG para função De Jong N.5 com seleção por roleta")
plt.axvspan(24-0.4,24+0.4, color='green', alpha=0.2)
plt.savefig("dejong5_roleta_boxplot.pdf")
labels[23] = "24"







# DeJong5 function with tournament method
df_dejong_tournament = pd.DataFrame()

for i in range(1, 31):
    config = "c" + str(i)
    file = "Resultado/DeJong5/Torneio/Conf" + str(i) + "_Torneio_DeJong.csv"

    df_dejong_tournament[config] = pd.read_csv(file, header=None)

dejong_tournament_no_elitism = []
dejong_tournament_elitism = []

for series_name, series in df_dejong_tournament.items():
    if int(series_name.removeprefix("c")) <= 15:
        dejong_tournament_no_elitism.append(series)
    else:
        dejong_tournament_elitism.append(series)

all_dejong_tournament = dejong_tournament_no_elitism + dejong_tournament_elitism    

dejong_tournament_medians = []

for series in all_dejong_tournament:
    dejong_tournament_medians.append(series.median())

best_dejong_tournament = dejong_tournament_medians.index(min(dejong_tournament_medians)) + 1

print(f"DeJong5 (tournament): config {best_dejong_tournament}  median {min(dejong_tournament_medians)}")


labels[16] = "$\\bf{17}$"
plt.figure(figsize=(14,8))
plt.boxplot(dejong_tournament_no_elitism + dejong_tournament_elitism,
            patch_artist=True,
            vert=True,
            labels=labels)

plt.grid(axis='y')
plt.xlabel("Config.")
plt.ylabel("$\\it{Fitness}$")
plt.title("$\\it{Boxplot}$ da execução do AG para função De Jong N.5 com seleção por torneio")
plt.axvspan(17-0.4,17+0.4, color='green', alpha=0.2)
plt.savefig("dejong5_torneio_boxplot.pdf")
labels[16] = "17"


plt.show()




#no_elitism_list = []
#elitism_list = []

#for series_name, series in df.items():
#    if int(series_name.removeprefix("conf")) <= 15:
#        no_elitism_list.append(series)
#    else:
#        elitism_list.append(series)

#print(elitism_list)

#plt.boxplot(elitism_list)
#plt.show()
