import os

def del_file(path):
    for i in os.listdir(path):
        path_file = os.path.join(path, i)  # 获取文件绝对路径
        if os.path.isfile(path_file):
            os.remove(path_file)
        else:
            del_file(path_file)


def Clean():
    flag = input('是否清理以前的数据,y:确认,任意键取消\n:')
    if flag == 'Y' or flag == 'y':
        del_file('****')
        del_file('***')
        del_file('****')
        del_file('****')
        print("清理完毕,开始测试")
    else:
        print('文件未清理,开始测试')
