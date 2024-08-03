def calculate_gcd(num1,num2):
    if num1>num2:
        for i in range(1,num2+1):
            if num1%i==0 and num2%i==0:
               ans=i
    else:
          for i in range(1,num1+1):
            if num1%i==0 and num2%i==0:
               ans=i      
    return ans      
def calculate_lcm(num1,num2,gcd):
     return ((num1*num2)/gcd)       
    
    
    
    
    
    
num1=int(input("Enter num 1:"))
num2=int(input("Enter num 2:"))
gcd=calculate_gcd(num1,num2)
lcm=calculate_lcm(num1,num2,gcd)
print(f"The GCD is:{gcd} AND LCM is: {lcm}")
