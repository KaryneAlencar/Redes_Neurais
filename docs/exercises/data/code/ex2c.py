X1 = df_dataset_1[['x1', 'x2', 'x3', 'x4', 'x5']]
y1 = df_dataset_1['classe']

X2 = df_dataset_2[['x1', 'x2', 'x3', 'x4', 'x5']]
y2 = df_dataset_2['classe']

pca1 = PCA(n_components=2, random_state=42)
X1_pca = pca1.fit_transform(X1)
df_pca1 = pd.DataFrame(X1_pca, columns=['PC1', 'PC2'])
df_pca1['classe'] = y1

pca2 = PCA(n_components=2, random_state=42)
X2_pca = pca2.fit_transform(X2)
df_pca2 = pd.DataFrame(X2_pca, columns=['PC1', 'PC2'])
df_pca2['classe'] = y2

var_exp1 = pca1.explained_variance_ratio_.sum()
var_exp2 = pca2.explained_variance_ratio_.sum()

print(f"Variância explicada pelos 2 primeiros componentes (Dataset I): {var_exp1:.4f}")
print(f"Variância explicada pelos 2 primeiros componentes (Dataset II): {var_exp2:.4f}")

dist_centros_1 = np.linalg.norm(mu_A - mu_B)

mu_C = df_C[['x1', 'x2', 'x3', 'x4', 'x5']].mean().values
mu_D = df_D[['x1', 'x2', 'x3', 'x4', 'x5']].mean().values
dist_centros_2 = np.linalg.norm(mu_C - mu_D)

print(f"Distância entre os centros em 5D (Dataset I): {dist_centros_1:.4f}")
print(f"Distância entre os centros em 5D (Dataset II): {dist_centros_2:.4f}")

df_dataset_1['raio'] = np.linalg.norm(df_dataset_1[['x1', 'x2', 'x3', 'x4', 'x5']].values, axis=1)
df_dataset_2['raio'] = np.linalg.norm(df_dataset_2[['x1', 'x2', 'x3', 'x4', 'x5']].values, axis=1)