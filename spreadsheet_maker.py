import csv
import math


def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier



          
with open('newest5.17.23GO.csv', mode='r') as csv_file:
	productsAndPrices = list(csv.DictReader(csv_file))
	print(productsAndPrices)
	#print the products/prices out to see
	for row in productsAndPrices:
		print(row)
		#print(type(row))


#with open('test_anesia_real.csv', mode='r') as csv_file:
with open('testcsvsall/Week 11_12-11_18/1113-Table 1.csv', mode='r') as csv_file:
	anesiasQuantities = list(csv.DictReader(csv_file))
	print("!!!!!!!")
	#print the Anesia sheet out to see
	for row in anesiasQuantities:
		print(row)
		#print(type(row))


#make an empty list of dicts to put outputSpread in
outputSpread = [{}] 
print("~~~~~~~~~~~~~~~~~~")
print(type(outputSpread))
print(type(outputSpread[0]))

#need to go through anesiasQuantities by each row, search for the price, compute line total, and add it to the row...

#each row in anesiasQuantities needs to be a row in outputSpread
for row in anesiasQuantities:
	print(f'\t Product is {row["product"]} and there were {row["quantity"]}.')

	invoiceNumber = row["invoiceNumber"]
	clientName = row["clientName"]
	invoiceDate = row["invoiceDate"]
	terms = "Net 30"
	message = row["message"]
	product = row["product"]
	quantity = row["quantity"]
	

	res = None
	for sub in productsAndPrices:
	    if sub['product'] == row["product"]:
	        res = sub
	        break
	print("The found value is : " + str(res))

	price = res["price"]

	print("The price is : " + res["price"] + " and the quantity is " + row["quantity"])
	lineTotal = float(res["price"]) * float(row["quantity"])
	lineTotal = round_up(lineTotal, 2)
	print(row["quantity"] + " at $" + res["price"] + " is total of $" + str(lineTotal))

	#row for putting in new outputSpread
	#outputRow = dict({'invoiceNumber': invoiceNumber, 'clientName': clientName, 'invoiceDate': invoiceDate, 'terms': terms, 'message': message, 'product': product, 'quantity': quantity, 'price': price, 'lineTotal': lineTotal})
	outputRow = dict({'invoice no.': invoiceNumber, 'customer': clientName, 'invoiceDate': invoiceDate, 'terms': terms, 'message': message, 'product': product, 'qty': quantity, 'rate': price, 'amount': lineTotal})
	#add the row to the outputSpread

	#if its not an invoice head row and the quantity is 0 dont add it (dont waste the space)
	#if quantity != '0':
	if clientName == '' and quantity == '0':
		print("dont include this line")
	else:
		outputSpread.append(outputRow)

print("*!*!*!*!*!*!*!*!*!*!*!*!*!*!*")
del outputSpread[0]
print(outputSpread)

# field names
#fields = ['invoiceNumber', 'clientName', 'invoiceDate', 'terms', 'message', 'product', 'quantity', 'price', 'lineTotal']
fields = ['invoice no.', 'customer', 'invoiceDate', 'terms', 'message', 'product', 'qty', 'rate', 'amount']

# name of csv file
filename = "output_spreadsheet.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv dict writer object
    writer = csv.DictWriter(csvfile, fieldnames = fields)
      
    # writing headers (field names)
    writer.writeheader()
      
    # writing data rows
    writer.writerows(outputSpread)







#
# Things i can add: if an items quantity is 0, skip it
# Make header names same as in  quickbooks so dont have to select them
# Need to put all the accounts in a huge spreadsheet for anesia to fill them in
# figure out a way to do invoice numbers
# How to handle certain days not having all accounts