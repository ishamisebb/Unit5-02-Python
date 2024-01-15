def calculate_area(base, height):
    try:
        area = 0.5 * base * height
        print("the area is {} cm^2".format(area))
    except ValueError:
        print("invalid input please enter valid number")


def main():
    try:
        base = float(input("enter base of triangle  in cm"))
        height = float(input("enter height of triangle in cm"))
        print("")
        if base < 0 or height < 0:
            print("invalid input please enter valid number")
        else:
            calculate_area(base, height)
    except ValueError:
        print("invalid input please enter valid number")

if __name__ == "__main__":
    main()

