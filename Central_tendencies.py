import csv 
import statistics
import pandas as pd

df = pd.read_csv("SOCR-HeightWeight.csv")
data = df["Height(Inches)"].tolist()

mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)

print(mean)
print(median)
print(mode)