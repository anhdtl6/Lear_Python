# Bài 1: Số lớn nhất
print("Nhập số a: ")
int_a = input()
print("Nhập số b: ")
int_b = input()
print("Nhập số c: ")
int_c = input()
print("Các số bạn vừa nhập vào là: ",int_a,',', int_b,',', int_c)
int_max = int_a
if (int_b>int_max):
    int_max=int_b
elif(int_c>int_max):
    int_max=int_c
print("Số lớn nhất là: ", int_max)

# Bài số 2: Chỉ số BMI
print("Nhập vào chiều cao của bạn")
height = float(input())
print("Nhập vào cân nặng của bạn")
weight = float(input())

bmi= round(weight/(height*height),2)
print("Chỉ số BMI của bạn là: ", bmi)

if(bmi<17):
    print("Gầy độ II")
elif(17<= bmi <18.5):
    print("Gầy độ I")
elif(18.5 <= bmi <25):
    print("Bình thường")
elif(25 <= bmi < 30):
    print("Thừa cân")
elif(30 <= bmi < 35):
    print("Béo phì độ I")
else:
    print("Béo phì độ II")

# Bài 3: Năm nhuận
print("Bạn hãy nhập vào một năm bạn muốn kiếm tra")
year= int(input())
isLeap=False
if(year % 4 ==0):
    if(year % 100 == 0):
        if(year % 400 == 0):
            isLeap = True
        else:
            isLeap = False
    else:
        isLeap = True
else:
    isLeap = False

if(isLeap == True):
    print(year, "là năm nhuận")
else:
    print(year, "không phải là năm nhuận")
