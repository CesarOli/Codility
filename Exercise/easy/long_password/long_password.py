import re

def solutions(S):
    words = S.split()
    max_length = -1

    for word in words:
        if not word.isalnum():
            continue

        letters = sum(c.isalpha() for c in word)
        digits = sum(c.isdigit() for c in word)

        if letters % 2 == 0 and digits % 2 == 1:
            max_length = max(max_length, len(word))

    return max_length

if __name__== "__main__":
    test_string = "test 5 a0A pass007 ?xy1"
    print(solutions(test_string))
