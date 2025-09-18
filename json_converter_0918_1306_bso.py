# 代码生成时间: 2025-09-18 13:06:33
import json
import numpy as np

"""
JSON数据格式转换器

该程序可以将JSON数据格式转换为NumPy数组，并支持反向转换。
它遵循Python最佳实践，具有清晰的结构、适当的错误处理和必要的注释。
"""


def json_to_numpy(json_data):
    """将JSON数据转换为NumPy数组。"""
    try:
        # 尝试将JSON数据解析为Python字典
        data = json.loads(json_data)
        # 将字典转换为NumPy数组
        return np.array(data)
    except json.JSONDecodeError:
        # 如果JSON数据格式不正确，抛出异常
        raise ValueError("Invalid JSON data.")


def numpy_to_json(numpy_array):
    """将NumPy数组转换为JSON数据。"""
    try:
        # 将NumPy数组转换为Python字典
        return json.dumps(numpy_array.tolist())
    except TypeError:
        # 如果数组中包含不支持的数据类型，抛出异常
        raise ValueError("Unsupported data type in NumPy array.")


def main():
    """主函数，演示JSON数据格式转换器的使用。"""
    # 示例JSON数据
    json_data = '{"array": [1, 2, 3, 4, 5]}'
    
    try:
        # 将JSON数据转换为NumPy数组
        numpy_array = json_to_numpy(json_data)
        print("NumPy array: ", numpy_array)
        
        # 将NumPy数组转换回JSON数据
        converted_json = numpy_to_json(numpy_array)
        print("Converted JSON: ", converted_json)
    except ValueError as e:
        # 处理可能的异常
        print("Error: ", e)

if __name__ == "__main__":
    main()