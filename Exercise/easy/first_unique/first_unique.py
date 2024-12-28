def solutions(A):
    occurrences = {}

    for num in A:
        if num in occurrences:
            occurrences[num] += 1
        else:
            occurrences[num] = 1

    for num in A:
        if occurrences[num] == 1:
            return num
        
    return -1

if __name__ == "__main__":
    
    #primeiro teste
    A = [1, 4, 3, 3, 1, 2]
    print(solutions(A)) #espera-se o resultado igual a 4

    #segundo teste
    A = [6, 4, 4, 6]
    print(solutions(A)) #espera-se o resultado igual a -1

    #terceito teste
    A = [4, 10, 5, 4, 2, 10]
    print(solutions(A)) #espera-se o resultado igual a 5