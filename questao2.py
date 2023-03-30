# Função para verificar se um número está na sequência de Fibonacci
def in_fibonacci(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    return b == numero

# Função para calcular a sequência de Fibonacci até um determinado limite


def sequencia_fibonacci(limite):
    fibonacci = [0, 1]
    while fibonacci[-1] < limite:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci


# Exemplo de uso
numero = int(input("Digite um número: "))
fibonacci = sequencia_fibonacci(numero)
if in_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
print(f"Sequência de Fibonacci até {numero}: {fibonacci}")
