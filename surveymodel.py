# surveymodel.py
# D. Sherman
# A basic model for storing and manipulating survey data loaded from a text file
from PyQt5 import QtCore
from PyQt5.QtCore import Qt

class SurveyModel:
    def __init__( self ):

        self.fileNameList = list()
        self.surveyDataDict = dict()
        self.pointDict = dict()

    def isValid( self, fileName ):

        try: 
            file = open( fileName, 'r' )
            file.close()
            return True
        except:
            return False

    def addFileName( self, fileName ):

        if self.isValid( fileName ):
            self.fileNameList.append(fileName)
            self.surveyDataDict[fileName] = SurveyData(fileName)
            self.pointDict.update(self.getSurveyData())

    def getFileName( self ):

        return self.fileNameList[-1]

    def getSurveyData(self):

        return self.surveyDataDict[self.fileNameList[-1]].getSurveyData()

    def getPointTable(self):

        pointTable = list()

        for pointKeys in self.pointDict.keys():

            point = self.pointDict[pointKeys]

            pointTable.append([point.num,point.northing,point.easting,point.height,point.description])
            
        return PointTableModel(pointTable)

class PointTableModel(QtCore.QAbstractTableModel):

    def __init__(self,data):

        super(PointTableModel,self).__init__()
        self._data = data

    def data(self,index,role):

        if role == Qt.DisplayRole:

            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        
        return len(self._data)

    def columnCount(self, index):

        return len(self._data[0])

class SurveyPoint:

    def __init__( self , num, northing, easting, height, description):

        self.num = num
        self.northing = northing
        self.easting = easting
        self.height = height
        self.description = description


    def printPoint(self):

        pointString = '' 
        pointString += str(self.num) + ' '
        pointString += str(self.northing) + ' '
        pointString += str(self.easting) + ' '
        pointString += str(self.height) + ' '
        pointString += str(self.description)

        print(pointString)

    def getPointString(self):

        pointString = '' 
        pointString += str(self.num) + '\t'
        pointString += str(self.northing) + '\t'
        pointString += str(self.easting) + '\t'
        pointString += str(self.height) + '\t'
        pointString += str(self.description)

        return pointString

class SurveyData:

    def __init__( self , fileName):

        self.fileName = fileName
        self.dataDict = dict()

        try:
            with open(fileName) as fp:
                
                for line in fp:

                    entry = line.split(',')

                    point = SurveyPoint(int(entry[0]),float(entry[1]),float(entry[2]),float(entry[3]),entry[4])
                    self.dataDict[int(entry[0])] = point

        except ValueError:

                    print("Invalid File Format")

    def getSurveyData(self):

        return self.dataDict

class Job(SurveyModel):

    def __init__( self, jobName = None ):

        super().__init__()
        self.jobName = jobName

    def getJobName(self):

        return self.jobName

    