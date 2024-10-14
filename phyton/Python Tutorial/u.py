a = int(input())
b = a + 1
count = 0

while count < 1:
    r = 0
    c = 0
    temp_b = b  # Use a temporary variable to preserve the value of b
    while temp_b > 0:
        r = temp_b % 10
        c = c * 10 + r
        temp_b = temp_b // 10
    print(c)
    if c == a:
        print(c)
        count += 1
    b += 1
