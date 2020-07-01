hours = int(input("Enter Hours of work: "))
performance = int(input("Enter performance rating from 0 to 10: "))
regular_rate = 10 #this is fixed
overtime_rate = 2.5 #this is fixed
qualified_for_overtime = False #you will have to change this according to performance

if performance>5:
    qualified_for_overtime = True
if qualified_for_overtime == True and hours>50:
    OVERTIME_HOURS = hours-50
    print('You worked overtime!')
else:
    OVERTIME_HOURS = 0
extra_pay = OVERTIME_HOURS*overtime_rate
total_pay = hours*regular_rate+extra_pay


print("Pay:", total_pay)
