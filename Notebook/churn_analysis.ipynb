# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session



import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/kaggle/input/telco-customer-churn/WA_Fn-UseC_-Telco-Customer-Churn.csv")  


print(df.head())
print(df.info())
print(df.describe())


df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

df.dropna(subset=['TotalCharges'], inplace=True)

df.reset_index(drop=True, inplace=True)

print(df['Churn'].value_counts())
churn_rate = df['Churn'].value_counts(normalize=True) * 100
print("Churn Rate (%):")
print(churn_rate)


plt.figure(figsize=(6,4))
sns.countplot(x='Contract', hue='Churn', data=df)
plt.title('Churn by Contract Type')
plt.ylabel('Number of Customers')
plt.xlabel('Contract Type')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

bins = [0, 6, 12, 24, 48, 72]
labels = ['0–6', '6–12', '12–24', '24–48', '48–72']
df['TenureGroup'] = pd.cut(df['tenure'], bins=bins, labels=labels)

plt.figure(figsize=(6,4))
sns.countplot(x='TenureGroup', hue='Churn', data=df)
plt.title('Churn by Tenure Group')
plt.xlabel('Tenure Range (months)')
plt.ylabel('Number of Customers')
plt.tight_layout()
plt.show()


import matplotlib.pyplot as plt
import seaborn as sns

services = ['OnlineSecurity', 'TechSupport', 'MultipleLines', 'StreamingTV']

# Create 2x2 subplot layout
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle('Churn by Services', fontsize=16)


axes = axes.flatten()

for i, service in enumerate(services):
    sns.countplot(x=service, hue='Churn', data=df, ax=axes[i])
    axes[i].set_title(f'Churn by {service}')
    axes[i].set_xlabel('')
    axes[i].set_ylabel('')

plt.tight_layout(rect=[0, 0, 1, 0.95])  # Leave space for suptitle
plt.show()


plt.figure(figsize=(7, 4))
sns.countplot(y='PaymentMethod', hue='Churn', data=df)
plt.title('Churn by Payment Method')
plt.legend(title='Churn', loc='upper right', bbox_to_anchor=(1.25, 1))  # Move legend outside the plot
plt.tight_layout()
plt.show()


plt.figure(figsize=(6,4))
sns.histplot(data=df, x='MonthlyCharges', hue='Churn', kde=True, bins=30)
plt.title('Monthly Charges Distribution by Churn')
plt.tight_layout()
plt.show()


print(df.groupby('Contract')['Churn'].value_counts(normalize=True).unstack() * 100)

print(df.groupby('TenureGroup')['Churn'].value_counts(normalize=True).unstack() * 100)

# Average MonthlyCharges by Churn
print(df.groupby('Churn')['MonthlyCharges'].mean())

# Churn % by PaymentMethod
print(df.groupby('PaymentMethod')['Churn'].value_counts(normalize=True).unstack() * 100)

churn_tables = {}
for service in services:
    churn_rate = df.groupby([service])['Churn'].value_counts(normalize=True).unstack() * 100
    churn_rate = churn_rate.rename(columns={'No': 'Churn: No (%)', 'Yes': 'Churn: Yes (%)'})
    churn_rate = churn_rate.reset_index()
    churn_tables[service] = churn_rate
    print(f"\nChurn Rate by {service}:\n")
    print(churn_rate)
