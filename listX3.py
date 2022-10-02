#Program to check the element is present in the list using count

def Check(Brr):
    print("Enter the number you want to check in the list")
    Num=int(input())
    size=len(Brr)

    count=Brr.count(Num)
    if count > 0:
        print("Number is present in the list")
    else:
       print("Number is not present in the list")

def main():
    Arr = list()

    print("Enter how many elements you want to insert in the list")
    value=int(input())

    print("Enter the elements in the list")
    for i in range(0,value):
        No=int(input())
        Arr.append(No)
    print(Arr)

    Check(Arr)

if __name__ == "__main__":
    main()