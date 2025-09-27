# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')


import matplotlib.pyplot as plt
# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
# pip install numpy matplotlib
import numpy as np


def logarithmic_spiral(a, b, c, theta_max, num_points=1000):
    """
    生成对数螺旋曲线的坐标

    参数:
    a: 初始半径
    b: 螺旋增长率
    c: z轴方向增长率
    theta_max: 最大角度（弧度）
    num_points: 点的数量

    返回:
    x, y, z: 螺旋曲线的坐标
    """
    theta = np.linspace(0, theta_max, num_points)
    r = a * np.exp(b * theta)  # 对数螺旋的半径公式

    x = r * np.cos(theta)
    y = r * np.sin(theta)
    z = c * theta  # z轴方向的线性增长

    return x, y, z


def main():
    print("对数螺旋曲线绘制程序")
    print("====================")

    # 获取用户输入
    try:
        a = float(input("请输入初始半径 (默认 1.0): ") or 1.0)
        b = float(input("请输入螺旋增长率 (默认 0.1): ") or 0.1)
        c = float(input("请输入z轴方向增长率 (默认 0.5): ") or 0.5)
        theta_max = float(input("请输入最大角度(弧度) (默认 4π): ") or (4 * np.pi))
    except ValueError:
        print("输入无效，使用默认值")
        a, b, c, theta_max = 1.0, 0.1, 0.5, 4 * np.pi

    # 生成螺旋曲线
    x, y, z = logarithmic_spiral(a, b, c, theta_max)

    # 创建3D图形
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # 绘制螺旋曲线
    ax.plot(x, y, z, 'b-', linewidth=2, label=f'a={a}, b={b}, c={c}')

    # 设置图形属性
    ax.set_xlabel('X轴')
    ax.set_ylabel('Y轴')
    ax.set_zlabel('Z轴')
    ax.set_title('3D对数螺旋曲线')
    ax.legend()

    # 添加网格
    ax.grid(True)

    # 显示图形
    plt.tight_layout()
    plt.show()

    # 可选：保存图形
    save = input("是否保存图形? (y/n): ").lower()
    if save == 'y':
        filename = input("请输入文件名 (默认: spiral_plot.png): ") or "spiral_plot.png"
        plt.savefig(filename, dpi=300)
        print(f"图形已保存为 {filename}")


if __name__ == "__main__":
    main()