df = pd.read_csv('train.csv')

balanceamento = df['Transported'].value_counts(normalize=True) * 100
print("Balanceamento da coluna Transported:")
print(balanceamento)

numericas = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
categoricas = df.select_dtypes(include=['object', 'bool']).columns.tolist()

print("Numéricas:", numericas)
print("Categóricas:", categoricas)

faltantes_abs = df.isnull().sum()
faltantes_pct = (df.isnull().mean() * 100).round(2)

tabela_faltantes = pd.DataFrame({
    'Contagem Absoluta': faltantes_abs,
    'Percentual (%)': faltantes_pct
})

tabela_faltantes = tabela_faltantes[tabela_faltantes['Contagem Absoluta'] > 0].sort_values(by='Percentual (%)', ascending=False)
display(tabela_faltantes)

colunas_gasto = ['RoomService', 'FoodCourt', 'ShoppingMall', 'Spa', 'VRDeck']
estatisticas_gasto = df[colunas_gasto].agg(['mean', 'median', 'max']).T
display(estatisticas_gasto)