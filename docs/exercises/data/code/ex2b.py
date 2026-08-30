def gerar_casca(n_amostras, raio_media, raio_std, nome_classe, random_state=rng):
    v = random_state.standard_normal((n_amostras, 5))
    normas = np.linalg.norm(v, axis=1, keepdims=True)
    u = v / normas
    rho = random_state.normal(loc=raio_media, scale=raio_std, size=(n_amostras, 1))
    x = rho * u
    
    df = pd.DataFrame(x, columns=['x1', 'x2', 'x3', 'x4', 'x5'])
    df['classe'] = nome_classe
    return df

df_C = gerar_casca(n_amostras=500, raio_media=2.0, raio_std=0.4, nome_classe='C')
df_D = gerar_casca(n_amostras=500, raio_media=5.0, raio_std=0.4, nome_classe='D')

df_dataset_2 = pd.concat([df_C, df_D], ignore_index=True)

print(f"Shape do Dataset II: {df_dataset_2.shape}")
display(df_dataset_2.head())
display(df_dataset_2.tail())