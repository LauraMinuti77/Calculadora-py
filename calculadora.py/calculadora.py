calculadora.py

# Calculadora simples em Python
print("Calculadora")

# Digite os números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Escolha da operação
operacao = input("Escola a operação que deseja realizar (+, -, *, /): ")

# Realização da operação
if operacao == "+":
  resultado = num1 + num2
elif operacao == "-":
  resultado = num1 - num2
elif operacao == "*":
  resultado = num1 * num2
elif operacao == "/":
    if num2 != 0:
       resultado = num1 / num2
    else: 
       resultado = "Erro: divisão por zero!"

else: 
   resultado = "Operação inválida!"

# Exibição dos resultados
print("Resultado: ", resultado)

