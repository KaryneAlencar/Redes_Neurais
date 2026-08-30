parametros = {
    0: {'media' : [2, 3], 'desvio': [0.8, 2.5]},
    1: {'media' : [5, 6], 'desvio': [1.2, 1.9]},
    2: {'media' : [8, 1], 'desvio': [0.9, 0.9]},
    3: {'media' : [15, 4], 'desvio': [0.5, 2.0]}
}

def gerar_dataset(s=1.0, random_state=rng):
    dados = []
    for classe, p in parametros.items():
        desvio_escalado = np.array(p['desvio']) * s
        pontos = random_state.normal(loc=p['media'], scale=desvio_escalado, size=(100, 2))
        df_classe = pd.DataFrame(pontos, columns=['x', 'y'])
        df_classe['classe'] = classe
        dados.append(df_classe)
    return pd.concat(dados, ignore_index=True)

df_s1 = gerar_dataset(1.0)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_s1, x='x', y='y', hue='classe', palette='tab10', s=50, alpha=0.7)

for classe, p in parametros.items():
    plt.scatter(p['media'][0], p['media'][1], color='red', marker='X', s=200, edgecolor='black')
