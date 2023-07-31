"""
Title: Near Misses Finder for xn + yn ≠ zn
File Name: HW1.py

External Files:
  - None

External Files Created:
  - None

Programmers:
  - [Harshavardhan Pullakandam]
  - [Anil Kumar Banoth]

Email Addresses:
  - [harshavardhanpulla@lewisu.edu]
  - [anilkumarbanoth@lewisu.edu]

Course Number and Section: [CPSC 60500] - [001]
Date Submitted: [7/30/2023]

Explanation:
An interactive user can use this programme to look for "near misses" of the pattern xn + yn zn, where x, y, z, n, and k
are positive numbers. The user is asked to enter numbers for n (the power to use in the equation) and k 
(which restricts the range of x and y possibilities to test) when the programme asks for them. 
The programme then determines the lowest "miss" between (xn + yn) and the closest bracketing values zn and (z+1)n 
in order to search systematically for x, y, and z combinations that are "almost right".

Each possible x, y, z combination is considered, and the program calculates the miss and the relative miss as a
percentage for each combination. The smallest relative miss is kept track of, and the corresponding x, y, and z values
are stored to determine the best "near miss." The program displays the best "near miss" found along with all near
misses in a tabulated format, including the x, y, z values, the miss, and the relative miss.

Note: Fermat’s last theorem states that there should not be any xn + yn = zn combinations that are exactly right for any
n > 2, but we are searching for near misses that satisfy the inequality.

Resources Used:
  - NONE
"""

def calculate_miss(x, y, z, n):
    # Calculate (x^n + y^n), zn, and (z+1)^n
    xn_yn = x ** n + y ** n
    zn = z ** n
    znp1 = (z + 1) ** n

    # Calculate the two possible "miss" values
    miss1 = xn_yn - zn
    miss2 = znp1 - xn_yn

    # Check which "miss" value is smaller and return the corresponding z
    if miss1 < miss2:
        return miss1, z
    else:
        return miss2, z + 1


def main():
    n = int(input("Enter the value of n (2 < n < 12): "))
    k = int(input("Enter the value of k (k > 10): "))

    smallest_miss = float('inf')
    best_x, best_y, best_z = None, None, None
    results = []

    for x in range(10, k + 1):
        for y in range(10, k + 1):
            # Iterate over z values that are greater than both x and y
            for z in range(max(x, y) + 1, k + 1):
                # Calculate the "miss" and nearest value of zn or (z+1)^n
                miss, nearest_zn = calculate_miss(x, y, z, n)
                # Calculate the relative miss as a percentage
                relative_miss = (abs(miss) / (x ** n + y ** n)) * 100

                # Check if the current relative miss is smaller than the smallest so far
                if relative_miss < smallest_miss:
                    # Update the smallest relative miss and the corresponding x, y, z
                    smallest_miss = relative_miss
                    best_x, best_y, best_z = x, y, nearest_zn

                # Append the current result to the results list
                results.append((x, y, z, miss, relative_miss))

    # Print the best "near miss" found and all near misses in the results list
    print("\nNear Misses for xn + yn ≠ zn:")
    print(f"n: {n}, k: {k}")
    print(f"Best x: {best_x}, Best y: {best_y}, Best z: {best_z}")
    print(f"Smallest Miss: {abs(best_x ** n + best_y ** n - best_z)}")
    print(f"Smallest Relative Miss: {smallest_miss:.2f}%")

    print("\nAll Near Misses:")
    print("x\t| y\t| z\t| Miss\t| Relative Miss")
    print("-" * 42)
    for x, y, z, miss, relative_miss in results:
        print(f"{x}\t| {y}\t| {z}\t| {miss}\t| {relative_miss:.2f}%")


if __name__ == "__main__":
    main()
