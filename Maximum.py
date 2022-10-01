#Program to find larger number

def Maximum(Value1,Value2):
    if Value1 > Value2:
        return Value1
    else:
        return Value2

def main():
    print("Enter first number")
    No1=input()

    print("Enter second number")
    No2=input()

    Ret=Maximum(int(No1),int(No2))

    print("The Larger number is:",Ret)

if __name__ == "__main__":
    main()