#program to interchange the first element of list with the last element

def ListX(newlist):

    size=len(newlist)

    temp=0

    temp = newlist[0]
    newlist[0] = newlist[size-1]
    newlist[size-1] = temp

    return newlist


def main():
    Arr = list()

    print("Enter how many elements you want to insert in the list")
    No=int(input())

    print("Enter the elements of list")

    for i in range(0,No):
        value = int(input())
        Arr.append(value)
    print(Arr)

    Ret=ListX(Arr)

    print("The list after exchange is",Ret)

if __name__ == "__main__":
    main()