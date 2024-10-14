def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_consecutive_primes(start, count):
    num = start
    primes_found = 0
    while primes_found < count:
        if is_prime(num):
            print(num, end=' ')
            primes_found += 1
        num += 1

# Input from the user
start = int(input("Enter the starting number: "))
count = int(input("Enter how many prime numbers to print: "))

print(f"The first {count} prime numbers starting from {start} are: ", end='')
print_consecutive_primes(start, count)
