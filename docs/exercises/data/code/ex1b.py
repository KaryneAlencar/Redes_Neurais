fatores_s = [0.5, 1.0, 2.0, 4.0]
datasets_s = {s: gerar_dataset(s) for s in fatores_s}

resultados_rij = []
classes = list(parametros.keys())
n_classes = len(classes)

for i in range(n_classes):
    for j in range(i + 1, n_classes):
        c1 = classes[i]
        c2 = classes[j]

        mu_i, mu_j = np.array(parametros[c1]['media']), np.array(parametros[c2]['media'])
        sigma_i, sigma_j = np.array(parametros[c1]['desvio']), np.array(parametros[c2]['desvio'])
        dist_medias = np.linalg.norm(mu_i - mu_j)
        sigma_bar_i = np.mean(sigma_i)
        sigma_bar_j = np.mean(sigma_j)
        r_ij = dist_medias / (sigma_bar_i + sigma_bar_j)
        resultados_rij.append({'Par_de_Classes': f'{c1} e {c2}', 'r_ij': r_ij})
df_rij = pd.DataFrame(resultados_rij)
display(df_rij)
idx_menor = df_rij['r_ij'].idxmin()
menor_par = df_rij.loc[idx_menor, 'Par_de_Classes']
menor_rij_s1 = df_rij.loc[idx_menor, 'r_ij']

print(f"\nO par com o menor r_ij é {menor_par}, com valor {menor_rij_s1:.4f}.")

menor_rij_s2 = menor_rij_s1 / 2
print(f"Como r_ij escala com 1/s, o menor r_ij em s=2 é exatamente a metade: {menor_rij_s2:.4f}")