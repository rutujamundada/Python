#program to demonstrate concept of list take values of list from user

def main():
    Arr = list()

    print("Enter how many elements you want to store...?")
    size=int(input())

    print("please enter the values")
    for i in range(0,size):
        no = int(input())
        Arr.append(no)  #Arr.insert(i,no)
    print(Arr)

if __name__ == "__main__":
    main()