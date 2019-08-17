print("跳一跳")
print("欢迎回来，开始游戏.......\n","请输入中心、音乐块、微信支付块（退出输入0）")
marks=0
while 1:
    energy=str(input("请输入："))
    if energy==str("中心"):
        marks=marks+2
        print("你的分数为：",marks)
    elif energy==str("音乐块"):
        marks=marks+5
        print("你的分数为：",marks)
    elif energy==str("微信支付块"):
        marks=marks+10
        print("你的分数为：",marks)
    elif energy==str(0):
        print("已退出")
        break
