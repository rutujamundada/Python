#program to find sum  elements in the list

def Addition(Brr):
   size=len(Brr)
   sum=0

   for i in range(0,size):
       sum = sum+Brr[i]
   return sum

def main():
    Arr = list()

    print("Enter how many elements you want to store in a list")
    value=int(input())

    print("Enter the elements in the list")
    for i in range(0,value):
        No=int(input())
        Arr.append(No)
    print(Arr)

    Ret=Addition(Arr)

    print("Addition of all elements in the list is:",Ret)

if __name__ == "__main__":
    main()