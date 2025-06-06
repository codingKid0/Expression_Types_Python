# نام دانشجو: حسن معمارزاده، کلاس مباحث ویژه در برنامه‌نویسی، روز دوشنبه
# هدف تمرین: برای هرکدام از عملگرهای مقایسه‌ای، رابطه‌ای، انتصاب و جبری، اکسپرشن تعریف کنید
# توجه: می‌تونستم متغیر تعریف نکنم و مستقیم در تابع پرینت مقادیر مورد نظرم رو مقایسه کنم

# مقایسه‌ای یا همان رابطه‌ای:
Var_A = 10
Var_B = 6
Result = Var_A < Var_B # چک می‌کنه که آیا متغیر دوم از اول بزرگتره

print(Result) # خروجی: False
#*********************************************************************
Var_A = 1
Var_B = 1.01
Result = Var_A == Var_B # چک می‌کنه که آیا متغیر اول و دوم برابرند

print(Result) # خروجی: False
#*********************************************************************
Var_A = True
Var_B = False
Result = Var_A != Var_B # چک می‌کنه که آیا متغیر اول و دوم برابر نیستند

print(Result) # خروجی: True
#*********************************************************************
Var_A = 80
Var_B = 79
Result = Var_A >= Var_B # چک می‌کنه که آیا متغیر اول از دوم بزرگتر یا مساویست

print(Result) # خروجی: True




# انتصاب:
# برای نسبت دادن مقداری به یک متغیر استفاده می‌شود و همچنین می‌تونه به صورت مرکب استفاده بشه یعنی:
# += , -= , *= , /= , %=
Name = "This is Hasan"
print(Name) # خروجی: This is Hasan
#*********************************************************************
Age = "He is 20"
print(Age) # خروجی: He is 20
#*********************************************************************
Pi = 3.14
print(Pi) # خروجی: 3.14
#*********************************************************************
Phone_Number = "+989105092381"
print(Phone_Number) # خروجی: +989105092381




# جبری یا همان محاسباتی
Var_A = 150
Var_B = 5
Result = Var_A / Var_B 

print(Result) # خروجی: 30.0
#*********************************************************************
Var_A = 4
Var_B = 5
Result = Var_A * Var_B 

print(Result) # خروجی: 20
#*********************************************************************
Var_A = 112.3
Var_B = 8.7
Result = (Var_A + Var_B) * 0.5

print(Result) # خروجی: 60.5
#*********************************************************************
Var_A = 580091
Var_B = 1326487
Result = Var_A - Var_B

print(Result) # خروجی: -746396
