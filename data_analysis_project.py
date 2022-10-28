# -*- coding: utf-8 -*-
"""Data_Analysis_Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aT901Y0_hxTWDUVEqT2kQCeT93p3ywXF

ShapeAI 7 Days bootcamp on python and data analysis by Mr Sahil Rahman

The Final Project

Questions:

Dataset Link: https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv

Submission Link: https://docs.google.com/forms/d/e/1FAIpQLSeICtczsmEPuWil1PyjD5Q7Etai-nxwGv16N785SrTg0v0ygg/viewform

Q1. Fill all the null values in the Age columns (Median)

Q2. Remove/delete the two null values from the Embarked column.

Q3. Tell the name of the Passanger, who is a female and she has survived, her age was b/w 20 - 30 and they belongs to the 1st class

Q4. Visualize the Pclass who has Survived and Not Survived w.r.t the Gender

Submitted by

Name: Manash Praim Pathak

email: manash20_ug@ee.nits.ac.in

college: NIT Silchar

# Importing Libraries
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

"""Data Cleaning"""

df.info()

"""Question 1: Fill all the null values in the Age columns (Median) """

df.isnull().sum()

df.describe()

df['Age'].median()

"""From the above to code

we came to know that there are around 177 null values in Age column and its median value is 28.

So, we just need to fill all the null values inside Age column with 28.
"""

df.drop(["Cabin"], axis=1, inplace=True)

df.info()

df.Age.fillna(28,inplace=True)

df.isnull().sum()

"""Question 2: Remove/delete the two null values from the Embarked column."""

df.dropna(inplace=True)

"""Question 3: Tell the name of the Passanger, who is a female and she has survived, her age was b/w 20 - 30 and they belongs to the 1st class.

Solution we will be given in the following steps:-
"""

dfSur = df[df["Survived"]==1] # sfSur will contain all the data about the passengers that have survived

dfSurFe = dfSur[dfSur["Sex"]=='female'] # dfSurFe will contain all the data about the passengers that have survived and were Female

dfSurFePcl = dfSurFe[dfSurFe["Pclass"]==1] # dfSurFePcl will contain all the data about the passengers that have survived, were Female and belonged to 1st class

dfSurFePclAge = dfSurFePcl[dfSurFePcl["Age"]<30] # dfSurFePclAge will contain all the data about the passengers that have survived, were Female, belonged to 1st class and age less than 30

dfSurFePclAge1 = dfSurFePclAge[dfSurFePclAge["Age"]>20] # dfSurFePclAge1 will contain all the data about the passengers that have survived, were Female, belonged to 1st class, age less than 30 and greater than 20.

dfSurFePclAge1.head()

Name_list = dfSurFePclAge1['Name'].tolist()

print(Name_list)

"""This give us the list of all the names of passenger that satisfy the given condition

Question 4: Visualize the Pclass who has Survived and Not Survived w.r.t the Gender
"""

sns.catplot(x="Survived",hue="Pclass", kind="count", col="Sex", data=df )