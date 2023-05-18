enter_User = "James"
enter_Pass = "Platzi"

print ("Bienvenido a Tlalocan")
print ("Usuario: ")
user = input()
print ("Contraseña: ")
pwd = input()


if  user == enter_User and pwd == enter_Pass:
    print ("Acceso concedido")
else:
    print ("Las credenciales son incorrectas")