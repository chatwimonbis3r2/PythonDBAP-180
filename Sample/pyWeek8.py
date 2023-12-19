# import openpyxl
# myfile = openpyxl.load_workbook("Financial.xlsx")
# worksheet = myfile.active
# print("=" * 100)
# print ("{:<20s} {:<30s} {:<30s} {:^15s} ".format(
# "Segments", "Country", "Product", "Sale"))
# print("-" * 100)
# for i in range(2 , worksheet.max_row+1):
#     segment = worksheet.cell(row=i, column=1).value
#     country = worksheet.cell(row=i, column=2).value
#     product = worksheet.cell(row=i, column=3).value
#     sale = worksheet.cell(row=i, column=10).value
#     print ("{}-{:<20s} {:<30s} {:<30s} {:>15s} ".format(i-1, segment, country, product, sale))
# print("-" * 100)

# import csv
# with open('Financial.csv', 'r') as myFile:reader = csv.reader(myFile)
# print("=" * 100)
# print ("{:<20s} {:<30s} {:<30s} {:^15s} ".format("Segments", "Country", "Product", "Sale"))
# print("-" * 100)
# header = True
# for row in reader:
#     if header == True:
#         header = False
#     else:
#        segment = row[0]
#        country = row[1]
#        product = row[2]
#        sale = row[9]
#        print ("{:<20s} {:<30s} {:<30s} {:>15s} ".format(segment, country, product, sale))
# print("-" * 100)

# import pandas as pd
# # df = pd.read_csv("Financial.csv")
# colname = ['Segment', 'Country', 'Product', 'Sales']
# colindex = [0,1,2,9]
# df = pd.read_csv("Financial.csv", usecols=colindex)
# print("=" * 100)
# print("{:<20s} {:<30s} {:<30s} {:^15s} ".format("Segments", "Country", "Product", "Sale"))
# print("-" * 100)
# for(i, datarow) in df.iterrows():
#     segment = datarow[0]
#     country = datarow[1]
#     product = datarow[2]
#     sale = datarow[3]
#     print("{:<20s} {:<30s} {:<30s} {:>15s} ".format(segment, country, product, sale))
# print("-" * 100)