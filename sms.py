import io
import unittest
from unittest import TestCase
class Sms(TestCase):
    def test_constructor(self):
        fp = io.open("score.csv","r",encoding = "utf-8")
        line = fp.readlines()
        sum = list()
        avg = list()
        self.assertIsNotNone(sum)   
        self.assertIsNotNone(avg)          

        for i in range(len(line)):
            std = line[i].split(",") 
            sum.append(int(std[2])+int(std[3])+int(std[4]))
            avg.append(round(sum[i]/3,3))

        ranking = list()
        self.assertIsNotNone(ranking)      

        for i in range(len(line)):
            std = line[i].split(",") 
            sum.append(int(std[2])+int(std[3])+int(std[4]))
            avg.append(round(sum[i]/3,3))

        ranking = list()
        self.assertIsNotNone(ranking)
        
        for content in sum:
            r = 1
            for content2 in sum:
                if content < content2:
                    r=r+1
            ranking.append(r)

        fp.close()
          
if(__name__=="__main__"):
    unittest.main()