#program to find smallest and largest number in the list

def smallest(Brr):
    size=len(Brr)

    min = Brr[0]
    for i in range(0,size):
        if Brr[i] < min:
            min = Brr[i]
    return min

def largest(Brr):
    size = len(Brr)
    max = 0

    for i in range(0, size):
        if Brr[i] > max:
            max = Brr[i]
    return max

def main():
    Arr = list()

    print("Enter how many elements you want to store in a list")
    value = int(input())

    print("Enter the elements in the list")
    for i in range(0, value):
        No = int(input())
        Arr.append(No)
    print(Arr)

    Ret = smallest(Arr)

    print("smallest number in the list is:", Ret)

    Ret = largest(Arr)

    print("largest number in the list is:", Ret)


if __name__ == "__main__":
    main()