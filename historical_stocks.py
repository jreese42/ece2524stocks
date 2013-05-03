import csv
import sys

def fillArray(ticker):
	temp_arr = []
	csvPath = 'stock_histories/' + ticker + '_historical_data.csv'
	f = open(csvPath)
	reader = csv.reader(f)
	for row in reader:
		if (row[1] != 'Open'):
			temp_arr.append(row[1])

	return temp_arr


AAME_array = fillArray('AAME')
AMAT_array = fillArray('AMAT')
BA_array = fillArray('BA')
CF_array = fillArray('CF')
GE_array = fillArray('GE')
GOOG_array = fillArray('GOOG')
GRT_array = fillArray('GRT')
MSFT_array = fillArray('MSFT')
NTAP_array = fillArray('NTAP')
SNE_array = fillArray('SNE')
SPG_array = fillArray('SPG')
VZ_array = fillArray('VZ')
WDC_array = fillArray('WDC')
YHOO_array = fillArray('YHOO')

#print(BA_array[0])
#print(CF_array[0])
#print(GE_array[0])
#print(GOOG_array[0])
#print(GRT_array[0])
#print(MSFT_array[0])
#print(NTAP_array[0])
#print(SNE_array[0])
#print(SPG_array[0])
#print(VZ_array[0])
#print(WDC_array[0])
#print(YHOO_array[0])

print(len(AAME_array))
print(len(AMAT_array))
print(len(BA_array))
print(len(CF_array))
print(len(GE_array))
print(len(GOOG_array))
print(len(GRT_array))
print(len(MSFT_array))
print(len(NTAP_array))
print(len(SNE_array))
print(len(SPG_array))
print(len(VZ_array))
print(len(WDC_array))
print(len(YHOO_array))





#var = 'NTAP'
#var2 = 'this_is_the_string_with_' + var + '_included'
#print(var2)


#f = open('stock_histories/NTAP_historical_data.csv')
#reader = csv.reader(f)
#for row in reader:
#	if (row[1] != 'Open'):
#		NTAP_array.append(row[1])
#f.close()






