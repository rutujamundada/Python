# reverse list using slicing method

def reverse(Brr):

    Brr=Brr[::-1]

    return Brr

def main():
    Arr = list()

    print("Enter how many elements you want to insert in the list")
    value=int(input())

    print("Enter the elements in the list")
    for i in range(0,value):
        No=int(input())
        Arr.append(No)
    print(Arr)

    Ret=reverse(Arr)

    print("Reversed list is",Ret)

if __name__ == "__main__":
    main()