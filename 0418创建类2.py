#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Keawen
class wupin:
    def __init__(self, mianji):
        self.zhanyongmianji = mianji

    def huoqumianji(self):
        return self.zhanyongmianji

class Chuang(wupin):
    pass
class Chaji(wupin):
    pass
class Home:
    def __init__(self, mianji):
        self.keyongmianji = mianji

    def rongna(self, wupin):
        if self.keyongmianji > wupin.huoqumianji():
            self.keyongmianji = self.keyongmianji - wupin.huoqumianji()
            print('可以安置好物品...剩余的面积为%d' % self.keyongmianji)
        else:
            print('不能安置好物品...剩余的面积为%d' % self.keyongmianji)


fangzi_bj = Home(120)
chaji = Chaji(100)
fangzi_bj.rongna(chaji)
muchaung = Chuang(4)
fangzi_bj.rongna(muchaung)