def isTriangleValid(a, b, c) :
    if ((a + b > c) and
        (b + c > a) and
        (c + a > b )) :
        return True
    else : return False

def defineTriangle(a, b , c) :
    if ((a == b and b == c)) :
        return 'This is an Equilateral Triangle'
    elif ((a == b)  or
          (b == c)  or
          (c == a)) :
        return 'This is an Isosceles Triangle'
    else :
        return 'This is a Scalene Triangle'



def triangle():
    print('Define 3 side lengths of a triangle and I will define the triangle based on your measurements.')
    side_a = float(input("A: "))
    side_b = float(input("B: "))
    side_c = float(input("C: "))

    if (isTriangleValid(side_a, side_b, side_c)) :
        return defineTriangle(side_a, side_b, side_c)
    else :
        return "This triangle is invalid!"

    



if __name__ == "__main__":
    while True:
        print('--------------Triangle Checker---------------')
        print("""Menu:
        [1] Use Triangle Checker
        [2] Quit Program""")
        choice = input("Enter number of option: ")
        if(choice == '2') : 
            print("Exiting Program...")
            break
        elif(choice == '1') :
            print(triangle())
            print("")
        else :
            print("Invalid choice, returning to menu.")