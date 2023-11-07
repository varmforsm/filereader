
import csv, zipfile

gus = {}
ess = []
ans = {}
ars = {}

class GeoUnit():
    """ Class for storing geographic unit data """
    def __init__(self, anzic06, area, year, geo_count, ec_count):
        self.anzic06 = anzic06
        self.area = area
        self.year = year
        self.geo_count = geo_count
        self.ec_count = ec_count

class EnterpriseSurvey():
    """ Class for storing enterprise survey data """
    def __init__(self, year, aggregation, code, name, units, varCode, varName, varCategory, value,	anzic06):
        self.year = year
        self.aggregation = aggregation
        self.code = code
        self.name = name
        self.units = units
        self.varCode = varCode
        self.varName = varName
        self.varCategory = varCategory
        self.value = value
        self.anzic06 = anzic06

class LookupAnzsic06():
    """ Class for looking up Anzsic06 """
    def __init__(self, anzsic06, description, sortOrder):
        self.anzsic06 = anzsic06
        self.description = description
        self.sortOrder = sortOrder

class LookupArea():
    """ Class for looking up area"""
    def __init__(self, area, description, sortOrder):
        self.area = area
        self.description = description
        self.sortOrder = sortOrder

def decodeGeoUnit(line):
    post = line.split(",")
    gus[post[0]] = GeoUnit(post[0], post[1], post[2], post[3], post[4])

def decodeEnterpriseSurvey(line):
    ess.append(EnterpriseSurvey(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9]))

def decodeLookupAnzsic06(line):
    ans[line[0]] = LookupAnzsic06(line[0], line[1], line[2]) 

def decodeLookupArea(line):
    ars[line[0]] = LookupArea(line[0], line[1], line[2]) 

def readCsvFile(fileName, interpreter):
    file = open(fileName)
    with file as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in csvreader:
            interpreter(row)
    file.close()

# Using readline()




datafile = zipfile.ZipFile('geographic-units-by-industry-and-statistical-area-2000-2023-descending-order-february-2023.zip', 'r')
data = datafile.open('geographic-units-by-industry-and-statistical-area-2000-2023-descending-order-february-2023.csv', 'r', 'utf-8')
while line := data.readline():
    line = line.decode()
    if line.split(",")[2] == "2021":
        decodeGeoUnit(line)

datafile.close()
file2 = open('annual-enterprise-survey-2021-financial-year-provisional-csv.csv')

with file2 as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in csvreader:
        if row[0][0:4] == "2021":
            decodeEnterpriseSurvey(row)

file2.close()

# Simple generic CSV file-reader
readCsvFile('lookup-area.csv', decodeLookupArea)
readCsvFile('lookup-anzsic06.csv', decodeLookupAnzsic06)


