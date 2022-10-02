#program to print even numbers in the list

def Even(Brr):
    size = len(Brr)

    for i in range(0,size):
        if Brr[i]%2 == 0:
            print(Brr[i])
        
def main():
    Arr = list()

    print("Enter how many elements you want to store in a list")
    value = int(input())

    print("Enter the elements in the list")
    for i in range(0, value):
        No = int(input())
        Arr.append(No)
    print(Arr)

    Even(Arr)

if __name__ == "__main__":
    main()