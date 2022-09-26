print("Addition to demonstrate Industrial Programming")

def Addition(Value1,Value2):
    ans = Value1 + Value2
    return ans

def main():
    print("Enter first number:")
    no1=int(input())

    print("Enter second number:")
    no2=int(input())

    Ret=Addition(no1,no2)

    print("Addition is:",Ret)

if __name__ == "__main__":
    print("Inside starter")
    main()