from customer import Customer
from item import Item
from seller import Seller
vendedor = Seller("DICストア")
for i in range(10):
    Item("CPU", 40830, vendedor)
    Item("Memoria", 13880, vendedor)
    Item("Placa base", 28980, vendedor)
    Item("Unidad de fuente de poder", 8980, vendedor)
    Item("Carcasa de PC", 8727, vendedor)
    Item("HDD de 3.5 pulgadas", 10980, vendedor)
    Item("SSD de 2.5 pulgadas", 13370, vendedor)
    Item("SSD M.2", 12980, vendedor)
    Item("Refrigerador de CPU", 13400, vendedor)
    Item("Tarjeta gráfica", 23800, vendedor)

print("🤖 Por favor, dime tu nombre")
cliente = Customer(input())

print("🏧 Ingresa la cantidad que deseas cargar en tu billetera")
cliente.wallet.deposit(int(input()))

print("🛍️ Comenzando la compra")
fin_compra = False
while not fin_compra:
    print("📜 Lista de productos")
    vendedor.show_items()

    print("️️⛏ Ingresa el número del producto")
    numero = int(input())

    print("⛏ Ingresa la cantidad del producto")
    cantidad = int(input())

    productos = vendedor.pick_items(numero, cantidad)
    for producto in productos:
        cliente.cart.add(producto)
    print("🛒 Contenido del carrito")
    cliente.cart.show_items()
    print(f"🤑 Monto total: {cliente.cart.total_amount()}")

    print("😭 ¿Deseas finalizar la compra? (si/no)")
    fin_compra = input() == "si"

print("💸 ¿Deseas confirmar la compra? (si/no)")
if input() == "si":
    vendedor.wallet.deposit(cliente.cart.total_amount())
    #print(item.owner.name)
    cliente.cart.check_out()

    

print("୨୧┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈ Resultados ┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈୨୧")
print(f"️🛍️ ️Pertenencias de {cliente.name}")
cliente.show_items()
print(f"😱👛 Saldo de la billetera de {cliente.name}: {cliente.wallet.balance}")

print(f"📦 Estado de inventario de {vendedor.name}")
vendedor.show_items()

print(f"😻👛 Saldo de la billetera de {vendedor.name}: {vendedor.wallet.balance}")

print("🛒 Contenido del carrito")
cliente.cart.show_items()
print(f"🌚 Monto total: {cliente.cart.total_amount()}")

print("🎉 Fin")