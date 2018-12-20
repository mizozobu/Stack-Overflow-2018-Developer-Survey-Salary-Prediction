import os
import csv

print('Enter input csv file name:')
readFile = '{}.csv'.format(input())

print('Enter output csv file name:')
writeFile = '{}.csv'.format(input())

languageCol = 'LanguageWorkedWith'
ratingCol = 'Rating'

with open(readFile, 'r', encoding='utf_8', newline='\n') as inputFile, open(writeFile, 'w', encoding='utf_8', newline='\n') as outputFile:
  inputRows = csv.reader(inputFile, delimiter=',', lineterminator='\n')
  writer = csv.writer(outputFile, delimiter=',', lineterminator='\n')

  writer.writerow(['Respondent', 'ConvertedSalary', languageCol, ratingCol])

  for i, row in enumerate(inputRows):
      if i == 0:
          header = row
          ConvertedSalaryIndex = header.index('ConvertedSalary')
      else:
          try:
              for j, cell in enumerate(row):
                  if header[j].startswith('{}_'.format(languageCol)) and cell == 'Yes':
                      writer.writerow([row[0], row[ConvertedSalaryIndex], header[j].split('_')[1], 1])
                  elif header[j].startswith('{}_'.format(languageCol)) and cell == 'No':
                      writer.writerow([row[0], row[ConvertedSalaryIndex], header[j].split('_')[1], 0])
          except Exception as e:
              print('Error in row {}'.format(j))
              print(e)
