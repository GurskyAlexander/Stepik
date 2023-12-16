def is_prime(number: int) -> bool:
    return sum(number % i == 0 for i in range(1, number+1)) == 2

