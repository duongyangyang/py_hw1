# 定义函数来计算总额
def calculate_total_amount(principal, interest_rate):
    interest = principal * (interest_rate / 100)
    total_amount = principal + interest
    return total_amount

# 主程序
if __name__ == "__main__":
    try:
        # 用户输入本金
        principal = float(input("请输入一年期定期存款本金（单位：人民币元）："))
        
        # 用户输入利率
        interest_rate = float(input("请输入一年期定期存款年利率（例如：2.52）："))
        
        # 计算总额
        total_amount = calculate_total_amount(principal, interest_rate)
        
        # 输出结果
        print(f"一年期满后，您的总金额为：{total_amount:.2f} 元")
        
    except ValueError:
        print("输入无效，请输入数字。")
