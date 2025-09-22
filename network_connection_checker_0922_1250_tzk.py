# 代码生成时间: 2025-09-22 12:50:08
import numpy as np
import requests
from requests.exceptions import ConnectionError

"""
网络连接状态检查器
该模块提供了一个简单的函数来检查指定网站的连接状态。
"""

def check_website_connection(url):
    """检查指定网站的连接状态。
    
    参数:
    url (str): 要检查的网站URL
    
    返回:
    tuple: 包含连接状态和状态码的元组。
    """
    try:
        # 发送HTTP请求以检查连接
        response = requests.get(url, timeout=5)  # 设置超时时间为5秒
        # 返回连接成功和响应状态码
        return (True, response.status_code)
    except ConnectionError as e:
        # 如果连接失败，返回连接失败和错误信息
        return (False, str(e))
    except Exception as e:
        # 处理其他可能的异常
        return (False, str(e))

# 示例使用
if __name__ == '__main__':
    url_to_check = 'http://www.google.com'
    connection_status, status_code = check_website_connection(url_to_check)
    if connection_status:
        print(f'Website {url_to_check} is accessible. Status code: {status_code}')
    else:
        print(f'Failed to connect to {url_to_check}. Error: {status_code}')
