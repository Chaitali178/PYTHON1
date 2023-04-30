students=(
    ("Chaitali",  19,"female","Computer science "),
    ("Swati",  19,"female","Computer science "),
    ("Sejal",  19,"female","Computer science "),
    ("Kalyani",  19,"female","Computer science "),
    ("Bhagyashree",  19,"female","Computer science ")
)
print("|      Name    |   Age   |  Gender |   Education in    |")
print("|--------------|---------|---------|-------------------|")
for student in students:
    print("|  {:<11} |  {:<5}  |  {:<6} |  {:<9}|".format(student[0],student[1],student[2],student[3])) 