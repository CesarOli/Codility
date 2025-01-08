def solution(S):
    """
    Finds the symmetry point of a string, if any.
    """
    n = len(S)
    if n % 2 == 0:
        return -1  # No symmetry point if the length is even

    mid = n // 2
    left = S[:mid]
    right = S[mid + 1:]

    if left == right[::-1]:
        return mid
    return -1


# Test cases
if __name__ == "__main__":
    # Example test cases
    print(solution("racecar"))  # Expected output: 3
    print(solution("x"))        # Expected output: 0
    print(solution("abcd"))     # Expected output: -1
    print(solution("abccba"))   # Expected output: -1
