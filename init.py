from concrete import fhe

# 定义一个简单的加法函数
@fhe.compiler({"x": "encrypted", "y": "encrypted"})
def add(x, y):
    return x + y

# 创建输入集以生成电路
inputset = [(2, 3), (1, 4), (5, 6)]  # 示例输入对
circuit = add.compile(inputset)

# 模拟客户端：加密输入
x, y = 7, 8  # 要加密的两个整数
encrypted_x = circuit.encrypt(x)
encrypted_y = circuit.encrypt(y)

# 模拟服务器：在加密数据上执行加法
encrypted_result = circuit.run(encrypted_x, encrypted_y)

# 模拟客户端：解密结果
result = circuit.decrypt(encrypted_result)

# 输出结果
print(f"加密计算：{x} + {y} = {result}")

# 验证
assert result == x + y, "计算错误"
print("验证成功！")