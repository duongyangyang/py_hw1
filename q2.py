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
        
        total_amount = []
        # 计算转存 0 次后的总额
        total_amount.append(calculate_total_amount(principal, interest_rate))
        print(f"一年期满后，您的总金额为：{total_amount[0]:.2f} 元")

        # 计算转存一次后的总额
        for i in range (1,3):
            total_amount.append(calculate_total_amount(total_amount[i-1], interest_rate))
            print(f"自动转存 {i} 次后，您的总金额为：{total_amount[i]:.2f} 元")
        
        
    except ValueError:
        print("输入无效，请输入数字。")
