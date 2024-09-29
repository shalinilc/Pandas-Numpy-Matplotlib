import pandas as pd
import matplotlib.pyplot as plt

file_path = "C:/Users/shali/Desktop/ai nu tech/1-Assessnment/archive/WineQT.csv"
data = pd.read_csv(file_path)

plt.figure(figsize=(10,5))
plt.hist(data['alcohol'])
plt.title('Distribution of Alcohol Content in Wines')
plt.xlabel('Alcohol Content')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.25)
plt.show()

plt.figure(figsize=(10,5))
plt.hist(data['quality'],color='green')
plt.title('Distribution of quality Content in Wines')
plt.xlabel('quality Content')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.25)
plt.show()

#scatter plot
plt.figure(figsize=(10,4))
plt.scatter(data['quality'],data['alcohol'],color='red',edgecolors="black")
plt.title('Distribution of quality Content in Wines')
plt.xlabel('quality Content')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.25)
plt.show()

plt.figure(figsize=(10,8))
plt.scatter(data['citric acid'],data['pH'], alpha=0.9)
plt.title("Relationship between pH and Citric acid")
plt.xlabel('pH')
plt.ylabel('citric acid')
plt.grid(alpha=0.9)
plt.show()

#bax plot
plt.figure(figsize=(10,5))
plt.boxplot([data[data['quality'] == q]['residual sugar'] for q in sorted(data['quality'].unique())],
            labels=sorted(data['quality'].unique()))
plt.show()

plt.figure(figsize=(10, 5))
plt.boxplot([data[data['quality'] == q]['pH'] for q in sorted(data['quality'].unique())],
            labels=sorted(data['quality'].unique()))
plt.title('Spread of pH by Wine Quality')
plt.xlabel('Quality Levels')
plt.ylabel('pH')
plt.grid(axis='y', alpha=0.75)
plt.show()

#bar plots
average_citric_acid = data.groupby('quality')['citric acid'].mean()
average_alcohol = data.groupby('quality')['alcohol'].mean()

# Bar plot for Average Citric Acid
plt.figure(figsize=(10, 5))
average_citric_acid.plot(kind='bar', color='lightblue', alpha=0.7, label='Average Citric Acid')
average_alcohol.plot(kind='bar', color='salmon', alpha=0.7, label='Average Alcohol', secondary_y=True)
plt.title('Average Citric Acid and Alcohol Content by Wine Quality')

#line plots
average_pH = df.groupby('quality')['pH'].mean()

# Line plot for Average pH Level
plt.figure(figsize=(10, 5))
plt.plot(average_pH.index, average_pH.values, marker='o', color='green', linestyle='-.')