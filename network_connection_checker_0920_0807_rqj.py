# 代码生成时间: 2025-09-20 08:07:33
import numpy as np
import requests
from requests.exceptions import ConnectionError, Timeout, RequestException
import socket
import time

"""
网络连接状态检查器
检查指定的主机是否可达，以及是否能够成功连接到指定的端口
"""

class NetworkConnectionChecker:
    def __init__(self, hostname, port):
        """
        初始化网络连接检查器
        :param hostname: 要检查的主机名或IP地址
        :param port: 要检查的端口号
        """
        self.hostname = hostname
        self.port = port

    def check_hostname(self):
        """
        检查主机名是否可达
        :return: True如果主机名可达，否则False
        """
        try:
            socket.gethostbyname(self.hostname)
            return True
        except socket.gaierror:
            return False

    def check_port(self):
        """
        检查指定的端口是否开放
        :return: True如果端口开放，否则False
        """
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            result = sock.connect_ex((self.hostname, self.port))
            sock.close()
            return result == 0
        except socket.error as err:
            print(f"Socket error: {err}")
            return False

    def check_http(self):
        """
        检查是否能够成功连接到指定的端口
        :return: True如果成功连接，否则False
        """
        try:
            response = requests.get(f"http://{self.hostname}:{self.port}", timeout=5)
            return response.status_code == 200
        except (ConnectionError, Timeout) as e:
            print(f"Connection error: {e}")
            return False
        except RequestException as e:
            print(f"Request exception: {e}")
            return False

    def check_connection(self):
        "