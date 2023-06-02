total_min=int(input("Enter the number of minutes:"))
hours=total_min//60
minutes=total_min%60
time="{}:{}".format(hours,minutes)
print("The total time of the number of minutes",total_min,"is: ",hours,
        "hours  &",minutes,"minutes")