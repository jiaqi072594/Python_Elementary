# -*- coding: utf-8 -*-
import re
'''phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d')
mo =phoneNumRegex.search('My number is 415-555-4242')
print('Phone number found:'+mo.group())
 
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d)')
mo =phoneNumRegex.search('My number is 415-555-4242')
print('Phone number found:'+'\ngroup(1)\t'+mo.group(1)+'\ngroup(2)\t'
    +mo.group(2)+'\ngroup(0)\t'+mo.group(0)+'\ngroup(0)\t'+mo.group(0))
    #+'\ngroups()\t'+mo.groups())
areaCode,mainNumber = mo.groups()
print('ngroups()\t',mo.groups(),'\nareaCode\t'+areaCode,'\nmainNumber\t'+mainNumber)'''
#?实现可选匹配
heroRegex = re.compile(r'Bat(man)?|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
#print(mo1.group())

mo2 = heroRegex.search(' Bat and Tina.')
#print(mo2.group())

#*匹配零次或多次
heroRegex1 = re.compile(r'Bat(man)*|Tina Fey')
mo3 = heroRegex1.search('Batmanmanmanmanmanmanmanman and Tina Fey.')
#print(mo3.group())

mo4 = heroRegex1.search(' Batss.')
#print(mo4.group())

#加号匹配一次或多次 零次输出None type
heroRegex2 = re.compile(r'Bat(wo)+man')
mo5 = heroRegex2.search('who is Batwoman.')
#print(mo5.group())

mo6 = heroRegex2.search(' who is Batman.')
#print(mo6)

#{}匹配特定次数
heroRegex3 = re.compile(r'(Ha){3}')
mo7 = heroRegex3.search('HaHaHa')
#print(mo7.group())

mo8 = heroRegex3.search('HaHa')
#print(mo8)

#{}? 贪心&非贪心
heroRegex3 = re.compile(r'(Ha){3,5}')
mo9 = heroRegex3.search('HaHaHaHa')
#print(mo9.group())
heroRegex4 = re.compile(r'(Ha){3,5}?')
moA = heroRegex4.search('HaHaHaHa')
#print(moA.group())

#findall() 方法 不同于search（）

#字符分类 

#re.compile(r'[aeiou]')与re.compile(r'[^aeiou]')的区别为^为非

#re.compile(r'^Hello') re.compile(r'Hello$') re.compile(r'^%d$')

#通配字符 '.xx'

# .*匹配除换行外的所有字符 带?为非贪心匹配

#re.DOTALL 作为re.compile的第二个参数 可以让.*匹配包括换行的所有字符

#re.IGNORECASE或者re.I作为re.compile的第二参数可以不区分大小写匹配

#sub()方法替代字符串

#re.VERBOSE为re.compile的第二参数时，可以在正则表达式中添加注释