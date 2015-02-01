import datetime

def parseDate():
        date_part = date.partition(":")[0]
        print("date part is ", date_part)
        #parse date here        

count = 0;
fo = open("smokes.txt", "r+")
"""
Read Line and parse date of first file
"""
date = fo.readline()
parseDate()

today = datetime.date.today()
string = today.__str__()+ ":"
fo.write(string)
while True:
        x = float(input("Enter value"))
        if x!=0:
                count=count+x
                print("count is ", count)
        else:
                break

fo.write(str(count))
fo.close

