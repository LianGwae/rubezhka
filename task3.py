def generate_fibonacci_sequence(length):
    sequence = [1, 1]
    while len(sequence) < length:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def main():
    length = int(input("Please enter the length of Fibonacci sequence\n"))
    fibonacci_sequence = generate_fibonacci_sequence(length)
    print("The Fibonacci sequence for", length, "is", fibonacci_sequence)

if __name__ == "__main__":
    main()