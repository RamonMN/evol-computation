import pandas as pd
import matplotlib.pyplot as plt


dejong5_roleta = pd.read_csv("Resultado/FitnessMelhor_Media_DeJongN5_Roleta.csv", header=None)
dejong5_torneio = pd.read_csv("Resultado/FitnessMelhor_Media_DeJongN5_Torneio.csv", header=None)
lang_roleta = pd.read_csv("Resultado/FitnessMelhor_Media_Langermann_Roleta.csv", header=None)
lang_torneio = pd.read_csv("Resultado/FitnessMelhor_Media_Langermann_Torneio.csv", header=None)


dejong5_roleta_melhores = []
dejong5_roleta_media = []
for index, value in enumerate(dejong5_roleta[0]):
    if (index%2) == 0:
        dejong5_roleta_melhores.append(value)
    else:
        dejong5_roleta_media.append(value)

dejong5_torneio_melhores = []
dejong5_torneio_media = []
for index, value in enumerate(dejong5_torneio[0]):
    if (index%2) == 0:
        dejong5_torneio_melhores.append(value)
    else:
        dejong5_torneio_media.append(value)

lang_roleta_melhores = []
lang_roleta_media = []
for index, value in enumerate(lang_roleta[0]):
    if (index%2) == 0:
        lang_roleta_melhores.append(value)
    else:
        lang_roleta_media.append(value)

lang_torneio_melhores = []
lang_torneio_media = []
for index, value in enumerate(lang_torneio[0]):
    if (index%2) == 0:
        lang_torneio_melhores.append(value)
    else:
        lang_torneio_media.append(value)


#fig, ax = plt.subplots()
#ax.plot(dejong5_roleta_melhores, label="Melhor $\\it{Fitness}$ por Geração")
#ax.plot(dejong5_roleta_media, label="$\\it{Fitness}$ Médio por Geração")

#ax.set(xlabel="$\\it{epoch}$", ylabel="$\\it{Fitness}$", title="Função De Jong N. 5 com seleção em roleta e configuração 24")
#ax.grid(axis='y')
#ax.legend()

plt.figure(figsize=(10,6))
plt.plot(dejong5_roleta_melhores, label="Melhor $\\it{Fitness}$ por Geração")
plt.plot(dejong5_roleta_media, label="$\\it{Fitness}$ Médio por Geração")
plt.xlabel("$\\it{epoch}$")
plt.ylabel("$\\it{Fitness}$")
plt.title("Função De Jong N. 5 com seleção em roleta e configuração 24")
plt.grid(axis='y')
plt.legend()
plt.savefig("dejong5_roleta_24.pdf")

plt.figure(figsize=(10,6))
plt.plot(dejong5_torneio_melhores, label="Melhor $\\it{Fitness}$ por Geração")
plt.plot(dejong5_torneio_media, label="$\\it{Fitness}$ Médio por Geração")
plt.xlabel("$\\it{epoch}$")
plt.ylabel("$\\it{Fitness}$")
plt.title("Função De Jong N. 5 com seleção em torneio e configuração 17")
plt.grid(axis='y')
plt.legend()
plt.savefig("dejong5_torneio_17.pdf")

plt.figure(figsize=(10,6))
plt.plot(lang_roleta_melhores, label="Melhor $\\it{Fitness}$ por Geração")
plt.plot(lang_roleta_media, label="$\\it{Fitness}$ Médio por Geração")
plt.xlabel("$\\it{epoch}$")
plt.ylabel("$\\it{Fitness}$")
plt.title("Função Langermann com seleção em roleta e configuração 18")
plt.grid(axis='y')
plt.legend()
plt.savefig("lang_roleta_18.pdf")

plt.figure(figsize=(10,6))
plt.plot(lang_torneio_melhores, label="Melhor $\\it{Fitness}$ por Geração")
plt.plot(lang_torneio_media, label="$\\it{Fitness}$ Médio por Geração")
plt.xlabel("$\\it{epoch}$")
plt.ylabel("$\\it{Fitness}$")
plt.title("Função Langermann com seleção em torneio e configuração 20")
plt.grid(axis='y')
plt.legend()
plt.savefig("lang_torneio_20.pdf")


plt.show()