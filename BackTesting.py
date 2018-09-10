import csv
# from matplotlib import pyplot as plt
import numpy as np
import argparse
import os

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-d', '--directory', help='directory pathway')
	parser.add_argument('-f', '--filename', help='random distribution or fixed variable')
	args = parser.parse_args()

	filenames = []
	if args.filename:
		filenames = args.filename

	else:
		for file in os.listdir(args.directory):
			if file.endswith('.csv'):
				filenames.append(file)
	print(filenames)
	for file in filenames:
		#===========================================
		#Create a dictionary
		dictionary = {}

		#Opening a CSV file to load all the data
		with open(args.directory + '/' + file) as csvfile:

			reader = csv.DictReader(csvfile)

			for row in reader:

				DictList = []

				# 0 Open : 1 Close : 2 High : 3 Low : 4 Volume

				DictList.append(row['open'])
				DictList.append(row['close'])
				DictList.append(row['high'])
				DictList.append(row['low'])
				DictList.append(row['volume'])

				dictionary[row['date']]  = DictList

		csvfile.close()
		#We can a dictionary with the date as key, and a list following that has all the other data

		#===========================================


		"""
		Strategy outline:
		
		We want to maximize the objective function of Profits = Sell - Buy
		
		
		
		
		"""

		#===========================================
		#Data Visualization
		#Here I'm creating the graph
		OpenData = []
		CloseData = []
		HighData = []
		LowData = []
		#Volume = []

		#I'm going to iterate through and create the keys
		for key in dictionary.keys():
			OpenData.append(float(dictionary[key][0]))
			CloseData.append(float(dictionary[key][1]))
			HighData.append(float(dictionary[key][2]))
			LowData.append(float(dictionary[key][3]))

		# plt.figure(figsize=(15,8)) #Changing the size of the plot
		#
		# xAxisList = [0, 127]
		#
		# plt.rc('grid', linestyle="-", color='black') #Puts grids on it
		# plt.grid(True)
		#
		# plt.xticks(np.arange(min(xAxisList), max(xAxisList), 1.0))
		# plt.yticks(np.arange(min(LowData), max(HighData), 5.0))
		#
		# plt.ylabel('Price')
		# plt.xlabel('Trading Day - 126 total') #You need to learn how to plot the date
		#
		# plt.plot(OpenData, 'r') #Open is Red
		# plt.plot(CloseData, 'b') #Close is blue
		# plt.plot(HighData, 'c') #High is Cyan
		# plt.plot(LowData, 'm') #Low is Magenta
		#
		# plt.show()
		#
		# #===========================================




		#===========================================

		#Initializing values block
		Profits = 0.0
		Losses = 0.0
		TradingDays = len(dictionary.keys())
		PositiveCounter = 0

		#===========================================






		#===========================================
		#Strategy 1 - Buy at open and sell at close on the same day
		"""
		for key in dictionary.keys():
			print("On " + str(key) + ", the open price was " + dictionary[key][0] + " and the close price was " + dictionary[key][1])
			print("			and High is " + dictionary[key][2] + " low is " + dictionary[key][3])
			DayProfits = float(dictionary[key][1]) - float(dictionary[key][0])
			Profits = Profits + DayProfits
			
			if (DayProfits > 0):
				PositiveCounter+=1
				
		#Profits are: 5.712000000001353
		#Trading Success rate is: 0.5396825396825397
		"""
		#===========================================
		#HAS idea - check times when close and high are SUPER CLOSE

		#===========================================
		#Strategy 2 - If close < open, and close is close to low. Buy right before close
		#Sell at some inputted percent above the close price'
		#For stocks that do not get sold -

		#look into this some more!!!

		KeyList = list(dictionary.keys()) #it's in backwards order

		tradeCount = 0
		#AverageSpread = 0
		failedTradeCount = 0

		#The attempt ratio is the price that we will try to sell the stock at ( a multiplier)
		AttemptRatio =input("Enter Attempt Ratio Here")
		AttemptRatio = float(AttemptRatio)

		#We multiply the close price by this value and it must still be less than open
		OpenCloseRatio = input("Enter Open Close Ratio")
		OpenCloseRatio = float(OpenCloseRatio)

		for key in dictionary.keys():
			close = dictionary[key][1]
			open = dictionary[key][0]
			low = dictionary[key][3]
			high = dictionary[key][2]
			volume = dictionary[key][4]


			if (open > close) and (float(low) > (float(close)*float(0.99))) and (OpenCloseRatio*float(close) < float(open)): #trying within 10%
				print("On " + str(key) + ", the open price was " + open + " and the close price was " + close)
				print("			and High is " + high + " low is " + low)
				print("		Buy at " + close)
				#print("		Volume yesterday was: " +  dictionary[KeyList[KeyList.index(key)+1]][4]) #index out of range
				print("		Volume today was: " + volume)
				#Price we are trying to sell it at
				AttemptSell = float(close)*AttemptRatio

				print("		Try to sell at " + str(AttemptSell))
				print("		tomorrow's high caps at: " + str(float(dictionary[KeyList[KeyList.index(key)-1]][2])))

				#if the attempt is less than the next day high
				if (AttemptSell < float(dictionary[KeyList[KeyList.index(key)-1]][2])):
					DayProfits = float(AttemptSell) - float(close)
					PositiveCounter +=1
					print("			and day profits today are : " + str(DayProfits))
					Profits = Profits + DayProfits

				else:
					#When a trade fails, instead, sell at close that day
					print("Trade failed")
					failedTradeCount = failedTradeCount + 1
					DayLosses = (float(AttemptSell) - float(dictionary[KeyList[KeyList.index(key)-1]][1]))
					print("and day losses are : " + str(DayLosses))
					Losses = Losses + DayLosses



				tradeCount = tradeCount + 1


		#AverageSpread = float(Profits/tradeCount)
		totalTradeRatio = float(PositiveCounter/tradeCount)
		#===========================================
		"""
		GOOGL
		When Attempt ratio = X, result is z.zz, with profits of $$$
		
		#NOTE : These results do not include what happens to stocks that DON't sell
		
		1.001 ; 0.846 ; 47.92790999999477
		1.003 ; 0.827 ;140.2242899999942
		1.004 ; 0.769 ; 173.6934000000001
		1.005 ; 0.711 ; 200.228
		1.006 ; 0.712 ; 240.27384000000006
		1.007 ; 0.635 ; 250.40133999999557
		1.008 ; 0.596 ; 267.7084000000003
		1.009 ; 0.558 ; 281.9094299999972
		1.010 ; 0.519 ; 291.2843999999999
		
		#Without losses, it seems that this value is always increasing.
		With losses...we are always negative
		
		
		
		For an attempt ratio of 1.005, the days that fail are:
		
		What trend is noticable in these days that fail?
		
		It kind of looks like the open and clsoe price are super close? Maybe avoid trades where opena dn close are super close to each other
		might be helpful to make a graph
		
		"""






		#===========================================
		#Results Block
		TradingRatio = float(PositiveCounter / TradingDays)

		print("Profits are: " + str(Profits))
		print("Losses are: " + str(Losses))
		print("Trading Success rate over all days: " + str(TradingRatio))
		print("Total trades: " + str(tradeCount))
		print("Total trades ratio is: " + str(totalTradeRatio))
		print("Failed trade count is: " + str(failedTradeCount) + " and positive is: " + str(PositiveCounter))

		#print("The average spread from the high to the buy price is: " + str(AverageSpread))

		#for GOOGL - spread is its 11.09863269230769 .... about 1%
		#===========================================

		"""
		Learned material
		
		d.items() returns tuples
		d.keys() is where the keys come back as
		"""
