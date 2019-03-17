# 记录所有的名片字典
card_list = []
def show_menu():
    print('*'*20)
    print("欢迎您使用名片系统!")
    print('0退出名片系统!')
    print('1新建名片!')
    print('2显示名片!')
    print('3查询名片!')
    print('*' * 20)


def new_card():
    '''新增名片'''
    print('- '*20)
    print('新增名片')
    # 1.提示用户输入名片的详细信息

    name_str = input("输入你的名字:")
    phone_str = input("输入你的电话:")
    qq_str = input("请输入你的qq:")
    email_str = input("请输入你的邮箱:")
    # 2用户输入的信息建立名片字典
    card_dict = {'name': name_str,
                 "phone": phone_str,
                 "qq": qq_str,
                 "email": email_str}

    # 3将名片字典添加到名片字典中
    card_list.append(card_dict)
    print(card_list)

    # 4提示用户添加成功
    print("添加%s的名片成功" % name_str)

def show_all():
    '''显示所有名片'''
    print('- ' * 20)
    print("显示所有名片")
    # 判断是否存在名片记录,如果没有,提示用户并且返回
    if len(card_list) == 0:
        print('当前没有任何的名片记录,请使用添加功能')
        #return 可以返回一个函数的执行结果
        #下方的代码不会被执行
        #如果return 后面没有任何的内容.表示会返回到调用函数的位置
        #并且不会返回任何的结果
        return

    # 打印表头
    for name in ['姓名', "电话", "qq", "邮箱"]:
        print(name, end="\t\t")
    print('')
    # 打印分割线
    print("=" * 30)
    # 遍历名片的列表一次输出字典的信息
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict['name'],
                                        card_dict["phone"],
                                        card_dict['qq'],
                                        card_dict["email"]))


def search_card():
    print('-' * 20)
    print("查找名片")
