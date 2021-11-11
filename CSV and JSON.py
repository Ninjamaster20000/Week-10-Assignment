#Import csv and json
import csv
import json

#Set up dictionary and final overall list
sales_data = []
dict1 = {'Transaction_Date':'', 'Product':'', 'Price':'', 'Payment_Type':'', 'Name':'', 'City':'', 'State':'', 'Country':'', }

#Open file and setup a for loop to loop through each line of the csv
with open("SalesJan2009.csv", "r") as inFile:
    csvReader = csv.reader(inFile)
    for line in csvReader:
        
        #Define each part in the dictionary
        dict1['Transaction_Date'] = line[0]
        dict1['Product'] = line[1]
        dict1['Price'] = line[2]
        dict1['Payment_Type'] = line[3]
        dict1['Name'] = line[4]
        dict1['City'] = line[5]
        dict1['State'] = line[6]
        dict1['Country'] = line[7]

        #Make a copy of the dictionary so it doesn't repeat the same dictionary in the list
        dict1_copy = dict1.copy()
        #Append the dictionary to the list
        sales_data.append(dict1_copy)

#Write the list to a json file
with open('transaction_data.json', 'w') as outFile:
    json.dump(sales_data, outFile)