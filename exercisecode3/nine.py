while True:
    num = int(input("Enter a number: "))

    if num < 0:
        print("Negative number entered, stopping...")
        break  # exit the loop

    elif num == 0:
        print("Zero is ignored, continue entering numbers.")
        continue  # skip rest of the loop, ask again

    else:
        print(f"You entered: {num}")
        pass  # does nothing, just a placeholder

print("Program ended")