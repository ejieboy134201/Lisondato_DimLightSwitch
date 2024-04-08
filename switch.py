def adjust_light(level):
    if level == 1:
        return "Light is Off (0%)\n."
    elif level == 2:
        return "Light is set to Low (25%)\n."
    elif level == 3:
        return "Light is set to Medium (50%)\n."
    elif level == 4:
        return "Light is set to High (75%)\n."
    elif level == 5:
        return "Light is set to Maximum (100%)\n."
    else:
        return "Invalid input. Please Enter the desired light level (1-5) or 0 to exit. \n1. Off\n2. Low\n3. Medium\n4. High\n5. Maximum\n0. Close\n\nPlease input here: "

# Main program loop
while True:
    try:
        level = int(input("\nEnter the desired light level (1-5) or 0 to exit. \n1. Off\n2. Low\n3. Medium\n4. High\n5. Maximum\n0. Close\n\nPlease input here: "))
        if level == 0:
            print("Exiting the light control.")
            break
        elif 1 <= level <= 5:
            print(adjust_light(level))
            adjust_again = int(input("Do you want to adjust the light again? \n1. Yes\n2. No\n\nPlease input here: "))
            if adjust_again == 2:
                print("Exiting the light control.")
                break
        else:
            print("Invalid input. Please Enter the desired light level (1-5) or 0 to exit. \n1. Off\n2. Low\n3. Medium\n4. High\n5. Maximum\n0. Close\n\nPlease input here: ")
    except ValueError:
        print("Invalid input. Please enter a number.")
