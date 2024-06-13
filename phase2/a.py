import pandas as pd 
import matplotlib.pyplot as plt


##Get the data
#file_path = "/Users/baharspring/MUNI_Data_Analytics/phase2/Mall_Customers.csv"
df = pd.read_csv('Mall_Customers.csv')
#print(df.head(5))
#print(df.tail(5))
#print('General information:', df.info)
print('Types of features:', df.dtypes)
#print('Description:', df.describe)
#print(df['Age'])
#print(df['Gender'])
age = df['Age']
gender = ['Gender']
annual_income = ['Annual Income (k$)']
##Plot the data
figure, axis = plt.subplots(2, 2)

#plt.bar(df['Age'],df['Annual Income (k$)'], color='skyblue')
axis[0, 0].set_title("Annual Income (k$) vs Spending Score (1-100)", fontsize = "6") 
axis[0,0].scatter(df['Annual Income (k$)'],df['Spending Score (1-100)'], color='blue')
axis[0, 1].set_title("Age", fontsize = "6")
axis[0,1].hist(df['Age'], color='skyblue')
axis[1, 0].set_title("Gender vs Spending Score (1-100)", fontsize = "6")
axis[1,0].bar(df['Gender'],df['Spending Score (1-100)'], color='yellow')
axis[1, 1].set_title("Gender vs Annual Income (k$)", fontsize = "6")
axis[1,1].bar(df['Gender'],df['Annual Income (k$)'], color='pink')
#axis[0,2].scatter(df['CustomerID'],df, color='orange')

#plt.scatter(df['Age'],df['Gender'])


#plt.xlabel('Age')
#plt.ylabel('Annual Income (k$)')
#plt.title('Something')
plt.savefig('a.png')
plt.show()





