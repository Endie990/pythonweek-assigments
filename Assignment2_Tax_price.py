#ASSIGNMENT 2- displaying road tax

price= float(input('Please enter cost price of the bike?: '))
if price>100000:
    print('Tax for bike',price,' is 15%')
elif price>50000 and price<=100000:
    print('Tax for bike',price,' is 10%')
elif price<=50000 and price>=0:
    print('Tax for bike',price,' is 5%')
