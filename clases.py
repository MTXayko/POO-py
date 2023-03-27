class Usuario:	
    def __init__(self):
        self.name = "Matias"
        self.email = "matias@codingdojo.com"
        self.nick = "xayko"
        self.balance_cuenta = 0

Usuario()
guido = Usuario() 
monty = Usuario()
equisde = Usuario()
# Accediendo a los atributos de la instancia
print(guido.name)	# salida: Michael
print(monty.email)	# salida: Michael
print(equisde.nick)

guido.name ='kevin'
monty.name ='cueck'
print(guido.name)
print(monty.name)

monty.nombre_banco ="banco estado"

print(f" 5 {monty.nombre_banco }")

