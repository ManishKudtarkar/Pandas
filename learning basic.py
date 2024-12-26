import pandas as manish
import numpy as shubham

data =shubham.array([[0,3],[10,7],[20,9],[30,14],[40,15]])
print(type(data))
print(data)

columns = ['temp','mobile']
df = manish.DataFrame(data=data,columns=columns)
print(df)

!pip install opendatasets

import opendatasets as od
od.download("https://www.kaggle.com/datasets/architsharma01/loan-approval-prediction-dataset")

data = manish.read_csv("/content/loan-approval-prediction-dataset/loan_approval_dataset.csv")

print(data)
