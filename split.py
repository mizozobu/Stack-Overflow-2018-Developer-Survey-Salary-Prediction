import os
import csv

print('Enter input csv file name:')
readFile = '{}.csv'.format(input())

print('Enter output csv file name:')
writeFile = '{}.csv'.format(input())

print('Enter col name to split:')
colToSplit = input()

with open(readFile, 'r', encoding='utf_8', newline='\n') as inputFile, open('temp.csv', 'w', encoding='utf_8', newline='\n') as outputFile:
  inputRows = csv.reader(inputFile, delimiter=',', lineterminator='\n')
  writer = csv.writer(outputFile, delimiter=',', lineterminator='\n')

  for i, row in enumerate(inputRows):
    if i == 0:
      originalColCount = len(row)
      colCount = originalColCount
      header = row
    
    else:
      try:
        for j, cell in enumerate(row):
          if header[j] == colToSplit:
            for k in range(originalColCount, colCount):
              row.append('No')
              
            originalColName = header[j]
            values = cell.split(';')

            for value in values:
              if value != 'NA':
                splitColName = '{}_{}'.format(originalColName, value)

                if splitColName in header:
                  # when header exists
                  targetIndex = header.index(splitColName)
                  row[targetIndex] = 'Yes'

                else:
                  # when header does not exist
                  header.append(splitColName)
                  row.append('Yes')
                  colCount += 1

      except Exception as e:
        print('Error occurred in spliting row {}'.format(i))
        print(e)
    
    try:
      writer.writerow(row)

    except Exception as e:
      print('Error occurred in writeing row {}'.format(i))
      print(e)
  
  writer.writerow(header)

with open('temp.csv', 'r', encoding='utf_8', newline='\n') as validateFile, open(writeFile, 'w', encoding='utf_8', newline='\n') as outputFile:
  inputRows = csv.reader(validateFile, delimiter=',', lineterminator='\n')
  writer = csv.writer(outputFile, delimiter=',', lineterminator='\n')
  tuples = list(enumerate(inputRows))
  totalRows = len(tuples)
  header = tuples[-1][1]
  colCount = len(header)

  for i, row in tuples:
    if i == 0:
      writer.writerow(header)
    elif i != totalRows - 1:
      for j in range(len(row), colCount):
        row.append('No')

      writer.writerow(row)
  
os.remove('temp.csv')

with open(writeFile, 'r', encoding='utf_8', newline='\n') as validateFile:
  inputRows = csv.reader(validateFile, delimiter=',', lineterminator='\n')
  writer = csv.writer(outputFile, delimiter=',', lineterminator='\n')
  tuples = list(enumerate(inputRows))
  totalRows = len(tuples)
  header = tuples[0][1]
  colCount = len(header)

  for i, row in tuples:
    items = []
    srcItemsText = row[header.index(colToSplit)]
    srcItems = srcItemsText.split(';')

    for j, cell in enumerate(row):
      title = header[j]
      
      if title.startswith('{}_'.format(colToSplit)) and cell == 'Yes':
        breakpoint = title.find('_') + 1
        items.append(title[breakpoint:])
    
    items.sort()
    srcItems.sort()

    if items != srcItems:
      if i != totalRows - 1 and i != 0 and srcItems != ['NA']:
        print('validation error at row: {}'.format(i), items, srcItems)

    
# =RIGHT(C8,LEN(C8)-FIND("_", C8))