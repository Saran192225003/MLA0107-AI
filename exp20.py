def towers_of_hanoi(n, source, target, auxiliary):
    if n > 0:
        # Move n-1 disks from source to auxiliary peg
        towers_of_hanoi(n - 1, source, auxiliary, target)

        # Move the nth disk from source to target peg
        print(f"Move disk {n} from {source} to {target}")

        # Move the n-1 disks from auxiliary peg to target peg
        towers_of_hanoi(n - 1, auxiliary, target, source)

def main():
    num_disks = int(input("Enter the number of disks: "))

    if num_disks <= 0:
        print("Number of disks should be greater than 0.")
        return

    towers_of_hanoi(num_disks, 'A', 'C', 'B')

if __name__ == "__main__":
    main()
