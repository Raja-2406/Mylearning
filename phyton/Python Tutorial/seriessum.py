next_term = int(input("Please enter the next term: "))
num_terms = int(input("Please enter the number of terms in the series: "))

current_term = next_term
total_sum = 0

print("The series:")
for i in range(num_terms):
    if(i==num_terms -1):
        print(current_term)
        total_sum +=current_term
    else:
        print(current_term, end=" + ")
        total_sum += current_term
        current_term = current_term * 10 + next_term

print("\nThe sum of the series:", total_sum)
