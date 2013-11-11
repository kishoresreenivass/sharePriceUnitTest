from companySharesAnalyzer import CompanyShareAnalyzer, DataInconsistantException
import unittest
class TestCompanyShareAnalyzer(unittest.TestCase):
    
    def test_for_inconsistant_data_in_file(self): 
        shareAnalyzer = CompanyShareAnalyzer("shareData_inconsistant.csv")
        self.assertRaises(DataInconsistantException,  lambda: shareAnalyzer.getResultSharePriceAnalysis())
    def test_for_inexistant_file(self):
        shareAnalyzer = CompanyShareAnalyzer("some_non_existant_file.csv")
        self.assertRaises(IOError, lambda: shareAnalyzer.getResultSharePriceAnalysis())
    def test_share_value(self):
        shareAnalyzer = CompanyShareAnalyzer("shareData.csv")
        self.result=shareAnalyzer.getResultSharePriceAnalysis()
        self.assertEquals(100, self.result[8].value)
    def test_share_month(self):
        shareAnalyzer = CompanyShareAnalyzer("shareData.csv")
        self.result=shareAnalyzer.getResultSharePriceAnalysis()
        self.assertEquals('jul', self.result[0].month)
    def test_share_year(self):
        shareAnalyzer = CompanyShareAnalyzer("shareData.csv")
        self.result=shareAnalyzer.getResultSharePriceAnalysis()
        self.assertEquals(1990, self.result[6].year)
        print '\nHere are the results for the final test case \n'
        shareAnalyzer.printResults()
if __name__ == '__main__':
    unittest.main()
