class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, quantity, price):
        self.items.append({'name': name, 'quantity': quantity, 'price': price})

    def remove_item(self, name):
        for item in self.items:
            if item['name'] == name:
                self.items.remove(item)
                break

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item['quantity'] * item['price']
        return total


cart = ShoppingCart()

cart.add_item('Apple', 2, 1.00)
cart.add_item('Banana', 3, 0.50)
cart.add_item('Orange', 1, 1.50)

print("Товары в корзине:")
for item in cart.items:
    print(f"{item['name']}: {item['quantity']} x {item['price']}")

print(f"Общая цена: {cart.calculate_total()}")

cart.remove_item('Banana')

print("Товары в корзине после удаления:")
for item in cart.items:
    print(f"{item['name']}: {item['quantity']} x {item['price']}")

print(f"Общая цена после удаления: {cart.calculate_total()}")