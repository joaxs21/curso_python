# Programa para calcular IMC
# Desenvolvido por Kayo
print("***************************************")
print("*         CALCULADORA DE IMC          *")
print("***************************************")
print()

#criação das variaveis
nome = ""
peso = 0
altura = 0.0
imc = 0.0

# ENTRADA DOS DADOS
nome = input("Qual o seu nome: ")
peso = int (input("Qual o seu peso: "))
altura = float (input("Qual a sua altura: "))

# PROCESSAR OS VALOR PARA OBTER O IMC
imc = peso / altura ** 2

# CLASSIFICAR OS IMCs
if imc <18.5:
    situacao ="Abaixo do peso"
elif imc >= 18.5 and imc < 25.0:
    situacao = "Peso Normal"
elif imc >= 25 and imc < 30:
    situacao = "Sobre Peso"
elif imc >= 30 and imc < 35:
    situacao = "Obesidade Grau 1"
elif imc >= 35 and imc < 40:
    situacao = "Obseidade Grau 2"
if imc >= 40:
    situacao = "Obesidade Grau 3"
    
    


#SAIDA DO PRECESSAMENTO
print()
print("************************************")
print("*             RESULTADO            *")
print("************************************")
print("*                                  *")
print("NOME: " + nome)
print ("PESO: " + str(peso)+ " Kg")
print("ALTURA: " + str(altura) + " M")
print("IMC: " + str(imc))
print (situacao)
 
