#IN: student's grade 1...10
# OUT: good, ok, bad

# x-----> x-----> ------> x
# 1       4     7       10

grade = int (input (" Your grade: "))

if grade > 7 and grade <= 10:
    print ("GOOD!")
elif grade > 4 and grade <= 7:
    print (" OK !")
elif grade >= 7 and grade <= 4:
    print ("Bad!")
elif grade > 10:
    print ("Wrong value")
elif grade < 1:
    print ( "Wrong value")
