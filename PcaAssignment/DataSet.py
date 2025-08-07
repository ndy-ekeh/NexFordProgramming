from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plotValue
import pandas as pdn

Basedata = load_breast_cancer()
dataValue = pdn.DataFrame(Basedata.data, columns=Basedata.feature_names)
target = Basedata.target

scaler = StandardScaler()
scaled_data = scaler.fit_transform(dataValue)

pca = PCA(n_components=2)
principal_components = pca.fit_transform(scaled_data)


pca_df = pdn.DataFrame(data=principal_components, columns=['PCA1', 'PCA2'])
pca_df['target'] = target

plotValue.figure(figsize=(8,6))
plotValue.scatter(pca_df['PCA1'], pca_df['PCA2'], c=pca_df['target'], cmap='coolwarm', edgecolor='k', s=40)
plotValue.xlabel('Main Component 1')
plotValue.ylabel('Mainn Component 2')
plotValue.title('2D PCA of Breast Cancer Dataset')
plotValue.show()