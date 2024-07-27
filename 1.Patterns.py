def lower_triangular(n):
    for i in range(n):
        for j in range(i + 1):

            print('*', end=' ')
        print()

# Example usage:
print("Lower triangle pattern :")
lower_triangular(5)

def upper_triangular(n):
    for i in range(n):
        for j in range(n):

            if j >= i:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

# Example usage:
print("Upper triangle pattern :")
upper_triangular(5)

def pyramid(n):
    for i in range(n):
        # Printing spaces
        for j in range(n - i - 1):
            print(' ', end=' ')
        # Printing stars
        for j in range(2 * i + 1):
            print('*', end=' ')
        print()

# Example usage:
print("Pyramidal pattern :")
pyramid(5)
