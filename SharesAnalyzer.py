from companyShareAnalyzerBean import CompanyDataBean
class DataInconsistantException(Exception):
    pass
class CompanyShareAnalyzer:
    def __init__(self,path):
        self.__path__=path
        self.result_=None
    def readFile(self):
        try:
            with open(self.__path__, 'r') as f:
                for ln in f:
                    ln = ln.split(',') # Removing the last ','
                    if self.result_ == None:
                        self.result_= [ CompanyDataBean(x,0,None,0) for x in ln[2:]]
                        continue
                    if len(self.result_) == len(ln[2:]):
                        yield (ln[:2],ln[2:])
                    else:
                        raise DataInconsistantException("Please check the data inside the file")
	except IOError, err:
            print "IOError : %r" %(err)
            raise IOError("File dosen't Exist")

    def getResultSharePriceAnalysis(self):
        for period,shareValue in self.readFile():
            for i, val in enumerate(shareValue):
               if self.result_[i] >  val:
                   self.result_[i]=CompanyDataBean(self.result_[i].name,val,period[1],period[0])
        return self.result_
    
    def printResults(self):
    	for i in self.result_ :
            print i
