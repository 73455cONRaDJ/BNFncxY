# 代码生成时间: 2025-09-21 07:24:50
import numpy as np
c"""
购物车类，用于管理购物车中的商品和数量。
"""

def validate_product_id(product_id):
    """
    验证商品ID是否为正整数。
    """
    if isinstance(product_id, int) and product_id > 0:
        return True
    else:
        raise ValueError("Product ID must be a positive integer.")

def validate_quantity(quantity):
    """
    验证数量是否为非负整数。
    """
    if isinstance(quantity, int) and quantity >= 0:
        return True
    else:
        raise ValueError("Quantity must be a non-negative integer.")

class ShoppingCart:
    """
    购物车类，包含添加商品、删除商品、计算总价等功能。
    """
    def __init__(self):
        """
        初始化购物车，使用numpy数组存储商品ID和数量。
        """
        self.products = np.zeros((0, 2), dtype=int)

    def add_product(self, product_id, quantity):
        """
        添加商品到购物车。
        """
        validate_product_id(product_id)
        validate_quantity(quantity)
        # 查找购物车中是否已存在该商品
        idx = np.where(self.products[:, 0] == product_id)[0]
        if idx.size > 0:
            # 如果存在，则更新数量
            self.products[idx, 1] += quantity
        else:
            # 如果不存在，则添加新商品
            self.products = np.vstack((self.products, [product_id, quantity]))

    def remove_product(self, product_id):
        """
        从购物车中删除商品。
        """
        validate_product_id(product_id)
        idx = np.where(self.products[:, 0] == product_id)[0]
        if idx.size > 0:
            self.products = np.delete(self.products, idx, axis=0)
        else:
            raise ValueError("Product not found in cart.")

    def get_total_price(self, price_list):
        """
        计算购物车中商品的总价。
        """
        if not isinstance(price_list, list) or len(price_list) != self.products.shape[0]:
            raise ValueError("Price list must match the number of products in cart.")
        total_price = 0
        for i in range(self.products.shape[0]):
            total_price += self.products[i, 0] * price_list[i]
        return total_price

    def get_cart_details(self):
        """
        返回购物车中商品的详细信息。
        """
        cart_details = []
        for i in range(self.products.shape[0]):
            cart_details.append({"product_id": self.products[i, 0], "quantity": self.products[i, 1]})
        return cart_details

# 示例用法
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_product(1, 2)
    cart.add_product(2, 3)
    cart.add_product(1, 1)  # 增加商品1的数量
    print(cart.get_cart_details())
    price_list = [10, 20]
    print("Total price: ", cart.get_total_price(price_list))
    cart.remove_product(2)
    print(cart.get_cart_details())
