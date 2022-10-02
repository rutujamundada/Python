#program to count occurrences of element in a list

def countx(Brr):
    size=len(Brr)
    count=0

    print("Enter the number you want to count the occurrences")
    cnt=int(input())

    #count=Brr.count(cnt)

    for i in range(0,size):
        if cnt == Brr[i]:
            count = count+1
    return count

def main():
    Arr = list()

    print("Enter how many elements you want to store in a list")
    value=int(input())

    print("Enter the elements in the list")
    for i in range(0,value):
        No=int(input())
        Arr.append(No)
    print(Arr)

    Ret=countx(Arr)

    print("occurrence of element is",Ret,"times")

if __name__ == "__main__":
    main()