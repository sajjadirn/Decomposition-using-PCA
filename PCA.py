 import pandas as pd
df = pd.read_csv("./specs/SensorData_question1.csv")
df.insert(12,'Original Input3', df['Input3']) #inserted a new column at index position 12
df.insert(13,'Original Input12', df['Input12']) #inserted a new column at index position 12
#df['Input3']=stats.zscore(df['Input3']) #didnt use the inbuilt function because it gives a different decimal value compared to the ones in the test program
df['Input3'] = (df['Input3'] - df['Input3'].mean())/df['Input3'].std() #doing zscore using the formula
df['Input12'] = (df['Input12']-df['Input12'].min())/(df['Input12'].max()-df['Input12'].min()) #used min max formula to bring the values within [0,1]
df.insert(14,'Average Input',0) #initialized new column with value 0
df['Average Input'] = df.iloc[:,0:12].mean(axis=1)
'''used iloc to specify range of rows and columns,
   in this case : specifies all the rows, and 0:12 specifies columns from index 0 upto 12(exlcusive)
   and calculated the mean with axis 1 because we want the mean of all the rows '''
df.to_csv('./output/question1_out.csv',index = None, float_format='%g')

#Question 2
df2 = pd.read_csv("./specs/DNAData_question2.csv")
'''from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(df2)
std_df2 = scaler.transform(df2)
didnt standardize because it gave a different value compared to the ones in the test program'''
from sklearn.decomposition import PCA
pca = PCA(0.95) #PCA will automatically created components which provide a variance of 95%
principal_components = pca.fit_transform(df2) #performing PCA on df2
principaldf = pd.DataFrame(data=principal_components) #initializing a new DataFrame
n = pca.n_components_
for i in range(n):
    df2['pca%i_width'%i] = pd.cut(principaldf[i],10) #binnig based on width
for i in range(n):
    df2['pca%i_freq'%i] = pd.qcut(principaldf[i],10) #binni ng based on frequency
print(principaldf)
print(df2)
df2.to_csv("./output/question2_out.csv", index=None)
