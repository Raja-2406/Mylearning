try:
    N = int(input("Please enter the number of terms in the series: "))
    if N <= 0:
        print("0.00")
    else:
        common_ratio = 0.5  # Adjust this value based on the actual common ratio
        first_term = 1.0

        current_term = first_term
        sum_of_series = 0.0

        print("The geometric series:")
        for _ in range(N):
            print(f"{current_term:.2f}", end=" + ")
            sum_of_series += current_term
            current_term *= common_ratio

        print("\b\b ")  # Remove the trailing "+ "
        print(f"\nSum of the series: {sum_of_series:.2f}")
except ValueError:
    print("Invalid input. Please enter a positive integer.")
