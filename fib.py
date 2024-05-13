

def generate_fibonacci(limit):
    fibonacci_sequence = [0, 1]
    while fibonacci_sequence[-1] + fibonacci_sequence[-2] < limit:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return fibonacci_sequence

def main():
    limit = 1000
    fibonacci_sequence = generate_fibonacci(limit)
    print("Fibonacci sequence up to", limit, ":", fibonacci_sequence)

if __name__ == "__main__":
    main()
