import pandas as pd
# Importing dataset
df = pd.read_csv('Stores.csv')

# Reading columns
df.rename(columns=
          {'Store ID': 'ID_Loja',
           'Store_Area': 'Area_da_Loja',
           'Items_Available': 'Itens_Disponíveis',
           'Daily_Customer_Count': 'Contagem_Diarias_Visitantes',
           'Store_Sales': 'Vendas_Loja'}, inplace=True)

# Taking the measures for the column 'Itens_Disponíveis'
i_a_count = df['Itens_Disponíveis'].count()
i_a_max = df['Itens_Disponíveis'].max()
i_a_min = df['Itens_Disponíveis'].min()
i_a_mean = df['Itens_Disponíveis'].mean()
i_a_std = df['Itens_Disponíveis'].std()

# Printing the metrics
print('Itens_Disponiveis_Stats')
print(f'Count: {i_a_count}')
print(f'Max: {i_a_max}')
print(f'Min: {i_a_min}')
print(f'Mean: {i_a_mean}')
print(f'STD: {i_a_std}')
print('\n')

# Taking the measures for the column 'Contagem_Diarias_Visitantes'
d_c_count = df['Contagem_Diarias_Visitantes'].count()
d_c_max = df['Contagem_Diarias_Visitantes'].max()
d_c_min = df['Contagem_Diarias_Visitantes'].min()
d_c_mean = df['Contagem_Diarias_Visitantes'].mean()
d_c_std = df['Contagem_Diarias_Visitantes'].std()

# Printing the metrics
print('Contagem_Diarias_Visitantes')
print(f'Count: {d_c_count}')
print(f'Max: {d_c_max}')
print(f'Min: {d_c_min}')
print(f'Mean: {d_c_mean}')
print(f'STD: {d_c_std}')
print('\n')

# Taking the measures for the column 'Vendas_Loja'
s_s_count = df['Vendas_Loja'].count()
s_s_max = df['Vendas_Loja'].max()
s_s_min = df['Vendas_Loja'].min()
s_s_mean = df['Vendas_Loja'].mean()
s_s_std = df['Vendas_Loja'].std()

# Printing the metrics
print('Vendas_Loja')
print(f'Count: {s_s_count}')
print(f'Max: {s_s_max}')
print(f'Min: {s_s_min}')
print(f'Mean: {s_s_mean}')
print(f'STD: {s_s_std}')
print('\n')
