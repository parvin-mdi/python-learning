print('Please enter 10 number.')
counter = 0
input_numbers = []
for i in range(10):
    counter = counter + 1
    number = int(input(f'number {counter} :'))
    input_numbers.append(number)


def is_prime(n):
    if n == 2:
        return True
    if n <= 1:
        return False

    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True


def prime_divisor_counter(n):
    counter = 0
    for i in range(1,n):
        if (n % i == 0) and (is_prime(i)):
            counter = counter + 1
    return counter


def get_max_value_with_index(n):
    value = 0
    counter = 0
    for i in n:
        if value <= i:
            value = i

    return value, (n.index(value))

prime_divisor_counts = []
for i in input_numbers:
    prime_divisor_counts.append(prime_divisor_counter(i))

max_count, max_index = get_max_value_with_index(prime_divisor_counts)
print(f'The answer is {input_numbers[max_index]} which has {max_count} prime divisors.')