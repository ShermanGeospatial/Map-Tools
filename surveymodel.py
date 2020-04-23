# surveymodel.py
# D. Sherman
# A basic model for storing and manipulating survey data loaded from a text file

class SurveyModel:
    def __init__( self ):

        self.fileNameList = list()
        self.surveyDataDict = dict()

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
            
    def getFileName( self ):

        return self.fileNameList[-1]

    def getSurveyData(self):

        return self.surveyDataDict[self.fileNameList[-1]].getSurveyData()

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
        self.dataList = list()

        try:
            with open(fileName) as fp:
                
                for line in fp:

                    entry = line.split(',')

                    point = SurveyPoint(int(entry[0]),float(entry[1]),float(entry[2]),float(entry[3]),entry[4])
                    point.printPoint()
                    self.dataList.append(point)

        except ValueError:

                    print("Invalid File Format")

    def getSurveyData(self):

        return tuple(self.dataList)

class Job(SurveyModel):

    def __init__( self, jobName = None ):

        super().__init__()
        self.jobName = jobName
        self.currentFile = None

    def getJobName(self):

        return self.jobName

    