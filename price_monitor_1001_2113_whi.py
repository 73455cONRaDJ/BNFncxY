# 代码生成时间: 2025-10-01 21:13:58
import numpy as np
import requests
from datetime import datetime

class PriceMonitor:
    """
    价格监控系统，用于跟踪商品价格变化。
    """

    def __init__(self, url):
        """
        初始化价格监控系统。
        :param url: 商品价格信息的URL
        """
        self.url = url
        self.prices = []
        self.last_updated = None

    def fetch_price(self):
        """
        从指定URL获取商品价格信息。
        """
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # 检查响应状态码
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching price: {e}")
            return None

    def update_prices(self):
        """
        更新价格列表。
        """
        price_data = self.fetch_price()
        if price_data is not None:
            price = price_data.get('price')
            if price is not None:
                self.prices.append(price)
                self.last_updated = datetime.now()
                print(f"Updated price to {price} at {self.last_updated}")

    def get_price_history(self):
        """
        获取商品价格历史记录。
        :return: 价格历史记录列表
        """
        return self.prices

    def get_last_updated(self):
        """
        获取最后更新时间。
        :return: 最后更新时间
        """
        return self.last_updated

    def detect_price_changes(self):
        """
        检测价格变化。
        """
        if len(self.prices) < 2:
            return False

        price_diff = np.diff(self.prices)
        return np.any(price_diff != 0)

# 使用示例
if __name__ == '__main__':
    url = "https://api.example.com/product/price"
    monitor = PriceMonitor(url)
    monitor.update_prices()
    print("Price history: ", monitor.get_price_history())
    print("Last updated: ", monitor.get_last_updated())
    print("Price change detected: ", monitor.detect_price_changes())
