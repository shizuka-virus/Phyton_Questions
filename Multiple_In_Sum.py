def main():
    total_sum = 0
    
    while True:
        try:
            num = int(input("Enter a number (enter 0 to terminate): "))
            if num == 0:
                break
            total_sum += num
        except ValueError:
            print("Please enter a valid number.")

    print("Sum of all inputs:", total_sum)

if __name__ == "__main__":
    main()
