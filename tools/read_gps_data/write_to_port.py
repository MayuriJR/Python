import serial
import time

ser = serial.Serial()


def port_open():
    ser.port = "COM{}".format(2)  # 设置端口号，应用这种，上边那种会报错
    ser.baudrate = 9600  # 设置波特率
    ser.bytesize = 8  # 设置数据位
    ser.stopbits = 1  # 设置停止位
    ser.parity = "N"  # 设置校验位
    ser.open()  # 打开串口,要找到对的串口号才会成功
    if (ser.isOpen()):
        print("打开成功")
    else:
        print("打开失败")


def port_close():
    ser.close()
    if (ser.isOpen()):
        print("关闭失败")
    else:
        print("关闭成功")


def send(send_data):
    if (ser.isOpen()):
        ser.write(send_data.encode('utf8'))  # utf-8 编码发送
        print("发送成功", send_data)
    else:
        print("发送失败")


f = open(r'C:\Users\Mayuri\Desktop\data.dat', encoding='utf-8')
data = []
for line in f:
    s = line.strip().split('\t')
    data.append(s)
f.close()


def sleep_time(hour, min, sec):
    return hour * 3600 + min * 60 + sec


# 时间间隔
second = sleep_time(0, 0, 1)

if __name__ == "__main__":
    port_open()

    data2 = [str(i) for i in data]  # 需要把数据转换成str类型，否则send（）错误
    for j in data2:
        # for line in data:            #此种数据类型错误，无法send（）
        time.sleep(second)
        print(j)
        send(j)
    port_close()