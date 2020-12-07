import time
import serial


def ser_get():
    portx = 'com1'  # 端口号
    bps = 9600  # 波特率
    timeout = None  # 超时时间设置，None代表永远等待操作
    ser = serial.Serial(portx, bps, timeout=timeout)  # 打开串口，并得到串口对象
    return ser


def ser_read():
    data = ''
    ser = ser_get()
    try:
        while True:
            num = ser.inWaiting()
            if num != 0:
                data = ser.read(num)  # 获取串口内容
                print('********************************************')
                t = time.ctime()
                print(t, ':', str(data.decode("utf8")))
                with open(r'D:/test.txt', 'a+') as f:
                    f.writelines(t)
                    f.writelines(':\n')
                    f.writelines(data.decode('utf8'))
            time.sleep(0.5)
    except Exception as e:
        print(e)
    finally:
        ser.close()


if __name__ == "__main__":
    print("start running:")
    ser_read()
