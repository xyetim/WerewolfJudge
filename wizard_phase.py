#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
女巫的行动模块
input:死亡玩家号码，玩家身份序列，自救开关
output:解药是否使用，毒死几号玩家
'''

__author__ = 'HuangXiaojun'

import os
import winsound
import time
import numput


def wizard_phase(dead,l,save_self):
    '''女巫阶段，反馈解救情况和毒死玩家号码'''
    cls = os.system('cls')
    winsound.Beep(1000,1000)#唤醒女巫
    _wizard = numput.raw_int('女巫，请输入你的号码：')
    print('注意：女巫一晚不能同时使用两瓶药！')
    _use_save = 0
    _use_poison = 0
    #解药阶段
    if dead == _wizard:
        if save_self == 1:
            print('今晚你死了。')
            _whether_use = input('你要使用解药吗？(y/n)')
        else:
            print('今晚你死了，不能自救。')
            _whether_use = 'n'
    else:
        if dead == 0:
            print('今晚没人死。')
            _whether_use = 'n'
        else:
            print('今晚%d号死了。' % dead)
            _whether_use = input('你要使用解药吗？(y/n)')
    if _whether_use == 'y' or _whether_use == 'Y':
        _use_save = 1
    #毒药阶段
    if _use_save == 0:
        _use_poison = numput.raw_int('你有瓶毒药是否要用？（输入想要毒死的号码，0为不使用）：')
    #将女巫加入玩家身份序列
    l[_wizard-1] = '女巫'
    input('<回车继续>')
    print('女巫闭眼。')
    time.sleep(3)
    return (_use_save,_use_poison)