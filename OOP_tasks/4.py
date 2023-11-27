import sys

carts = [cart.strip() for cart in sys.stdin]

print(len(carts) - len(set(carts)))
