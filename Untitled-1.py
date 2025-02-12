class GroceryStore:
    def __init__(self, name, apples_sold, apple_price, oranges_sold, orange_price):
        self.name = name
        self.apples_sold = apples_sold
        self.apple_price = apple_price
        self.oranges_sold = oranges_sold
        self.orange_price = orange_price

    def calculate_revenue(self):
        return (self.apples_sold * self.apple_price) + (self.oranges_sold * self.orange_price)


# Дэлгүүрийн объектууд үүсгэх
bambaruush = GroceryStore("Bambaruush", 534, 5000, 487, 10000)
jimshen = GroceryStore("Jimshen", 764, 4800, 423, 9300)
fruits = GroceryStore("Fruits", 136, 5000, 228, 10000)

bambaruush_revenue = bambaruush.calculate_revenue()
jimshen_revenue = jimshen.calculate_revenue()
fruits_revenue = fruits.calculate_revenue()

total_revenue = bambaruush_revenue + jimshen_revenue + fruits_revenue

print(f"{bambaruush.name} дэлгүүрийн орлого: {bambaruush_revenue}₮")
print(f"{jimshen.name} дэлгүүрийн орлого: {jimshen_revenue}₮")
print(f"{fruits.name} дэлгүүрийн орлого: {fruits_revenue}₮")
print(f"Нийт борлуулалтын орлого: {total_revenue}₮")
