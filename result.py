marathi=int(input("Enter the Marathi marks :"))
english=int(input("Enter the English marks :"))
hindi=int(input("Enter the Hindi marks :"))
mathamatics=int(input("Enter the Mathamatics marks : "))
science=int(input("Enter the Science marks :"))
socialscience=int(input("Enter the Social science marks :"))
# calculate the all subject marks
totalmarks=marathi+english+hindi+mathamatics+science+socialscience
print("Obtend Marks :",totalmarks)
persentage=float(totalmarks/600*100)
print("Persentage :",persentage,"%")
if persentage>=90:
    print("Grade A+")
elif persentage>=80:
    print("Grade A ",["Pass"])
elif persentage>=70:
    print("Grade B+",["Pass"])
elif persentage>=60:
    print("Grade B",["Pass"])
elif persentage>=50:
    print("Grade C+",["Pass"])
elif persentage>=40:
    print("Grade C",["Pass"])
elif persentage>=35:
    print("Grade D",["Pass"])
else:
    print("Student is Fail")