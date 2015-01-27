import datetime
count = 0;
fo = open("smokes.txt", "w")
string = prepared_Dated = datetime.date.today().__str__() + ":"
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
