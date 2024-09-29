import pandas as pd

file_path = "C:/Users/shali/Desktop/ai nu tech/1-Assessnment/archive/WineQT.csv"
data = pd.read_csv(file_path)

print(data.head())
print(data.info())
print(data.describe())
print(data.isnull())
print(data.isnull().sum())

#data filtering
sorted_quality_asc = data.sort_values(by='quality', ascending=True)
print(sorted_quality_asc.head())

sorted_quality_des = data.sort_values(by='quality', ascending=False)
print(sorted_quality_des.head())

sorted_alcohol_asc = data.sort_values(by='alcohol', ascending=True)
print(sorted_alcohol_asc.head())

sorted_alcohol_des = data.sort_values(by='alcohol', ascending=False)
print(sorted_alcohol_des.head())

#group
grouped = data.groupby('quality').mean()[['pH','alcohol','residual sugar']]
print(grouped)

median = data.groupby('quality')['alcohol'].median()
print(median)

#adding new colomn
data['quality_category'] = data['quality'].apply(lambda x: 'High Quality' if x > 7 else 'Low Quality')
print(data[['quality', 'quality_category']].head(200))
