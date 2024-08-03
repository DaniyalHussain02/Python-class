def factorial(num):
    fac=1
    for i in range(1,num+1):
        fac=i*fac
    return fac






if __name__=="__main__":
    num=int(input("Enter a number whose factorial you want to :"))
    ans=factorial(num)
    print(f"The factorial of {num} is:",ans)