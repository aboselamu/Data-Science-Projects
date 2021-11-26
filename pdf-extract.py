import tabula
import pandas as pd
import csv
import math

filen= tabula.read_pdf(input_path=R'C:\Users\joguy\OneDrive\Desktop\five_year_sale_Araga_Dairy.pdf', pages = 'all')
# creating lists of tables 
a = []
for i in range(len(filen)):
    a = a + [filen[i]]
# creating list of column Nobb nr.
y = []
for s in a:
    try:
        for val in s["Nobb nr."]:
            y.append(val)
    finally:
        continue

def isfloat(num):
    try:
        int(num)     
        return True
    except:
        return False
# crating the list of files 
final_list = []

for k in range(len(y)):
    if str(y[k]).isnumeric() or isfloat(y[k]):
        if y[k] not in final_list:
            final_list.append(y[k])
    else:
        pass
len(final_list)

with open('output.csv', 'w', newline='',encoding="utf-8") as csv_1:
  csv_out = csv.writer(csv_1)
  csv_out.writerows([filen[index]] for index in range(0, len(filen)))
