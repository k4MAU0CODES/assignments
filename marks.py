subject_1=int(input("enter subject1 marks:"))
subject_2=int(input("enter subject2 marks:"))
subject_3=int(input("enter subject3 marks:"))
subject_4=int(input("enter subject4 marks:"))
if subject_1<0 or subject_1>100 or subject_2<0 or subject_2>100 or subject_3<0 or subject_3>100 or subject_4<0 or subject_4>100:
else:
    average=(subject_1+subject_2+subject_3+subject_4)/4
print(average)
if average>=70<=100:
    print=("A")
elif average>=60<70:
    print=("B")
elif average>=50<60:
    print=("C")
elif average>=40<50:
    print=("D")
elif average>=0<40:
    print=("fail")





