# 代码生成时间: 2025-09-16 06:47:38
import numpy as np

class ShoppingCart:
# 增强安全性
    """
    A class representing a shopping cart which keeps track of items added.
    Each item is represented by its name and quantity.
# 优化算法效率
    """

    def __init__(self):
        # Initialize the shopping cart dictionary
        self.cart = {}

    def add_item(self, item_name, quantity):
        """
        Add an item to the shopping cart.
# 添加错误处理
        
        Parameters:
        item_name (str): The name of the item to add.
        quantity (int): The quantity of the item to add.
        
        Raises:
        ValueError: If quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.cart[item_name] = self.cart.get(item_name, 0) + quantity

    def remove_item(self, item_name, quantity):
        """
        Remove an item from the shopping cart.
        
        Parameters:
        item_name (str): The name of the item to remove.
        quantity (int): The quantity of the item to remove.
        
        Raises:
        ValueError: If quantity is negative or if item does not exist in the cart.
        """
        if quantity < 0:
# 改进用户体验
            raise ValueError("Quantity cannot be negative.")
        if item_name not in self.cart:
            raise ValueError(f"Item '{item_name}' does not exist in the cart.")
        if self.cart[item_name] < quantity:
            raise ValueError(f"Not enough quantity of '{item_name}' in the cart.")
        self.cart[item_name] -= quantity
        if self.cart[item_name] == 0:
            del self.cart[item_name]

    def get_cart_items(self):
        """
        Return a list of items in the cart with their quantities.
        """
        return list(self.cart.items())

    def get_total_items(self):
# 扩展功能模块
        """
# NOTE: 重要实现细节
        Return the total number of items in the cart.
# 改进用户体验
        """
        return sum(self.cart.values())

    def clear_cart(self):
# NOTE: 重要实现细节
        """
        Clear the entire cart.
        """
        self.cart.clear()

# Example usage:
# TODO: 优化性能
if __name__ == '__main__':
    cart = ShoppingCart()
    cart.add_item("apple", 3)
    cart.add_item("banana", 2)
    print("Cart items:", cart.get_cart_items())
    print("Total items:", cart.get_total_items())
    cart.remove_item("apple", 1)
    print("Cart items after removal:", cart.get_cart_items())
    cart.clear_cart()
    print("Cart items after clearing:", cart.get_cart_items())
