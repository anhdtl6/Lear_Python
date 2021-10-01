# Bài 1: Định dạng thời gian
print("Bạn hãy nhập vào số giây")
n = int(input())
int_hours = round(n/3600,)
int_minutes = round(n% 3660 /60,)
int_second = round(n% 3600 %60,)
if n<0:
    print("Bạn hãy nhập số nguyên dương nhé")
else:
    {
        print("Số giây sau khi chuyển đổi là: ", int_hours ,"giờ",int_minutes,"phút",int_second,"giây")
    }

# Bài 2: Chuyển đổi đơn vị độ dài
print("Bạn hãy nhập vào độ dài km")
leght = float(input())
float_m= round(float(leght*1000),2)
float_dm=round(float(leght*10000),2)
float_cm=round(float(leght*100000),2)
float_mm= round(float(leght*1000000),2)
float_mile= round(float(leght/1.609344),2)
float_inch= round(float(leght*1567839370.1),2)
print("Độ dài sau khi quy đổi các đơn vị là:",float_m,"mét,",float_dm,"dm,",float_cm,"cm,",float_mm,"mm,", float_mile, "mile,", float_inch,"ich")

# Bài 3: Chuyển đổi nhiệt độ
print("Bạn hãy nhập vào nhiệt độ")
celcius = float(input())
float_F= float(celcius*9/5+32)
float_K= float(celcius+237.15)
float_R= float((celcius+273.15)*9/5)

print("Nhiệt độ sau khi chuyển đổi là: ",float_F,"độ Farenheit, ",float_K,"độ Kenven,",float_R,"độ Rankine")


