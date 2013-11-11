class CompanyDataBean:
    def __init__(self,name,value=0,month=None,year=0):
        self.name=name
        self.value=int(value)
        self.month=month
        self.year=int(year)
    def __gt__(self,value):
        return (int(value) > self.value) 
    def __str__(self):
        return "Company Name : %10s ShareValue : %6s  Month/Year : %4s/%4d" % (str(self.name).strip(), self.value, self.month,self.year)
