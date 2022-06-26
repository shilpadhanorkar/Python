income=float(input("Please enter your amount:-"))
n=income

if  n<=250000:
    tax=0
elif n <=500000:
    tax=0+((n-250000)* 0.05)
elif n <= 1000000:
    tax=0+12500+((n-500000)* 0.1)
else:
    tax=0+12500+50000+ ((n-1000000) * 0.3)  
    
print("Taxable amount",tax,"Ruppes")