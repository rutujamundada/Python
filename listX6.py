# program to copy list

def Copy(Crr):

    Brr = Crr.copy()
 
    print("Original list is :",Crr)
    print("Duplicate list is:",Brr)


def main():
    Arr = list()
    print("Enter how many elements you want to insert in the list")
    value=int(input())

    print("Enter the elements in the list")
    for i in range(0,value):
        No=int(input())
        Arr.append(No)
    print(Arr)

    Copy(Arr)

if __name__ == "__main__":
    main()