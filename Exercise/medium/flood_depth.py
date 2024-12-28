def solution(A):
    if len(A) < 3:
        return 0
    
    max_left = [0] * len(A)
    max_rigth = [0] * len(A)

    max_left[0] = A[0]
    for i in range(1, len(A)):
        max_left[i] = max(max_left[i - 1], A[i])

    max_rigth[-1] = A[-1]
    for i in range(len(A) - 2, -1, -1):
        max_rigth[i] = max(max_rigth[i + 1], A[i])
        
    max_depth = 0
    for i in range(1, len(A) - 1):
        if max_left[i - 1] > A[i] and max_rigth[i + 1] > A[i]:
            water_depth = min(max_left[i], max_rigth[i]) - A[i]
            max_depth = max(max_depth, water_depth)

    return max_depth

# Testes
if __name__ == "__main__":
    # Teste inicial
    A = [1, 3, 2, 1, 2, 1, 5, 3, 3, 4, 2]
    print('Teste 1 - Entrada: ', A)
    print('Resultado esperado: 2')
    print('Resultado obtido:', solution(A))
    
    # Teste adicional 1
    A = [5, 8]
    print('\nTeste 2 - Entrada: ', A)
    print('Resultado esperado: 0')
    print('Resultado obtido:', solution(A))

    # Teste adicional 2
    A = [4, 1, 1, 0, 2, 3]
    print('\nTeste 3 - Entrada:', A)
    print('Resultado esperado: 3')
    print('Resultado obtido:', solution(A))

    # Teste adicional 3
    A = [1, 1, 0, 2, 1]
    print('\nTeste 4 - Entrada:', A)
    print('Resultado esperado: 0')
    print('Resultado obtido:', solution(A))
