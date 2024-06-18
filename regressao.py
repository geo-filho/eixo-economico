import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

ipca = {
    'Ano': [2017, 2018, 2019, 2020, 2021, 2022, 2023],
    'IPCA': [2.95, 3.75, 4.31, 4.52, 10.06, 11.73, 4.68]
}


dfIPCA = pd.DataFrame(ipca)

plt.plot(dfIPCA['Ano'],dfIPCA['IPCA'], color = 'blue')

plt.xticks(dfIPCA['Ano'])

plt.xlabel('Ano')
plt.ylabel('IPCA')
plt.title('IPCA')

plt.show();

media = np.mean(ipca['IPCA'])
des = np.std(ipca['IPCA'])

print(dfIPCA)
print('A média do IPCA é ',media)