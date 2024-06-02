#FilterMapReduceEx.py
import functools as ft
print("Enter List of Salaries ranges from 0 to 1000 separated by space:")
salist=[float(sal) for sal in input().split() if 0<=float(sal)<=1000]  # [1000.0, 600.0, 500.0, 100.0]
sal0_500=list(filter(lambda sal: sal<=500,salist))
sal501_1000=list(filter(lambda sal: sal>500,salist))
#Give 20% Hike for those emps whos sal range from 0 to 500
hikesal0_500=list(map(lambda sal: sal+sal*20/100,sal0_500))
#Give 30% Hike for those emps whos sal range from 501 and 1000
hikesal501_1000=list(map(lambda sal: sal+sal*30/100,sal501_1000))
totsal0_500=ft.reduce(lambda x,y:x+y,sal0_500)
tothikesal0_500=ft.reduce(lambda x,y:x+y,hikesal0_500)
totsal501_1000=ft.reduce(lambda x,y:x+y,sal501_1000)
tothikesal501_1000=ft.reduce(lambda x,y:x+y,hikesal501_1000)

#Display 0-500 sal emps
print("-"*50)
print("\tSal0-500\t\tHike Salary")
print("-"*50)
for osl,nsl in zip(sal0_500,hikesal0_500):
	print("\t{}\t\t\t{}".format(osl,nsl))
print("*"*50)
print("\t{}\t\t\t{}".format(totsal0_500,tothikesal0_500))
print("*"*50)
print("\tSal501-1000\t\tHike Salary")
print("-"*50)
for osl,nsl in zip(sal501_1000,hikesal501_1000):
	print("\t{}\t\t\t{}".format(osl,nsl))
print("*"*50)
print("\t{}\t\t\t{}".format(totsal501_1000,tothikesal501_1000))
print("*"*50)
print("TOTAL OLD SALS:{}\tTOTAL NEW SALS:{}".format(totsal0_500+totsal501_1000,tothikesal0_500+tothikesal501_1000))