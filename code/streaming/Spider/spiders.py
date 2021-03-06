#coding=utf-8

import requests
import pandas as pd 

def getDateFromWeb(dateList=None):

	for date in dateList:
		target = 'http://aigaogao.com/tools/sectors.html?dt=' + date
		print(target)

		csvPath = './sharesPackage/' + date + '.csv'

		tables = pd.read_html(target, attrs={'id':'sectscmp'})

		usefulTable = tables[0]

		usefulTable.columns = ['分类', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
		usefulTable = usefulTable.drop([2,3], axis=1)

		usefulTable.columns = ['分类', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]	
		usefulTable.to_csv(csvPath, encoding="utf-8", index=0)


def getDateList(dateBegin='2007-01-01'):
	import datetime
	dateEnd = datetime.datetime.now().strftime('%Y-%m-%d')
	dateEnd = datetime.datetime.strptime(dateEnd, '%Y-%m-%d')
	# print('dateEnd', dateEnd)

	dateList = []
	dateBegin = datetime.datetime.strptime(dateBegin, '%Y-%m-%d')
	dateList.append(dateBegin.strftime('%Y-%m-%d'))

	while dateBegin < dateEnd:
		dateBegin += datetime.timedelta(days=+1)
		# print('dateBegin: ', dateBegin)
		dateList.append(dateBegin.strftime('%Y-%m-%d'))

	return dateList


if __name__ == '__main__':

	dateList = getDateList('2007-01-01')
	print(len(dateList))

	getDateFromWeb(dateList)