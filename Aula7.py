# ## Desafio 1

# *Você é um analista de dados, e decidiu trocar de emprego.*

# *Utilize a media, moda, mediana e o desvio padrão para decidir qual empresa faz sentido para você:*

# *Justificar por que decidiu por essa empresa.*

# ***Verifique isso através dos salários:***

import statistics






empresa1 = [1000,6000,1200,8000,1400]

empresa2 = [5000,4000,3000,2000,7000]

empresa3 = [1200,1300,8000,3000,15000]

empresa4 = [1400,1750,2000,4500,5900]

empresa5 = [1400,1750,2000,4500,5900]



media_empresa1 = sum(empresa1) / len(empresa1)
print(f"Média da empresa 1: {media_empresa1}")

n = len(empresa1)
mediana_da_empresa_1 = (empresa1[n//2] if n % 2 != 0 else (empresa1[n//2 - 1] + empresa1[n//2]) / 2)
print(f"Mediana da empresa 1: {mediana_da_empresa_1}")

moda_da_empresa_1 = statistics.mode(empresa1)
print(f"Moda Da Empresa 1: {moda_da_empresa_1}")

media_empresa2 = sum(empresa2) / len(empresa2)
print(f"Média da empresa 2: {media_empresa2}")

n = len(empresa2)
mediana_da_empresa_2 = (empresa2[n//2] if n % 2 != 0 else (empresa2[n//2 - 1] + empresa2[n//2]) / 2)
print(f"Mediana da empresa 2: {mediana_da_empresa_2}")

moda_da_empresa_2 = statistics.mode(empresa2)
print(f"Moda Da Empresa 2: {moda_da_empresa_2}")


media_empresa3 = sum(empresa3) / len(empresa3)
print(f"Média da empresa 3: {media_empresa3}")

n = len(empresa3)
mediana_da_empresa_3 = (empresa3[n//2] if n % 2 != 0 else (empresa3[n//2 - 1] + empresa3[n//2]) / 2)
print(f"Mediana da empresa 3: {mediana_da_empresa_3}")

moda_da_empresa_3 = statistics.mode(empresa3)
print(f"Moda Da Empresa 3: {moda_da_empresa_3}")


media_da_empresa4 = sum(empresa4) / len(empresa4)
print(f"Média da empresa 4: {media_da_empresa4}")

n = len(empresa4)
mediana_da_empresa_4 = (empresa4[n//2] if n % 2 != 0 else (empresa4[n//2 - 1] + empresa4[n//2]) / 2)
print(f"Mediana da empresa 4: {mediana_da_empresa_4}")

moda_da_empresa_4 = statistics.mode(empresa4)
print(f"Moda Da Empresa 4: {moda_da_empresa_4}")


media_empresa5 = sum(empresa4) / len(empresa4)
print(f"Média da empresa 5: {media_empresa5}")

n = len(empresa4)
mediana_da_empresa_5 = (empresa5[n//2] if n % 2 != 0 else (empresa5[n//2 - 1] + empresa5[n//2]) / 2)
print(f"Mediana da empresa 5: {mediana_da_empresa_5}")


moda_da_empresa_5 = statistics.mode(empresa5)
print(f"Moda Da Empresa 5: {moda_da_empresa_5}")

escolha_final = ('Eu escolho a empresa numero 3, pois a media e a mediana dela me agrada bastante')
print(f'Escolha final: {escolha_final}')