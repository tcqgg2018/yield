#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'TAN' # 2021-11-8 04:06

## …………………`【更新记录】` ……………………                  
# 2022-01-23 05:44 添加datetime
# 2022-01-10 01:22 更新为类 (v1.0)

import math,time,logging
from random import uniform
from datetime import datetime

#while True:
for i in range(10):

  class Yields():
  #start = time.perf_counter()

    def input_num(self,*agrs):
      model=input('\n【型♦️号】:')
    #batch=input('【批次】')
    #size=input('【尺寸】')
      self.total = int(eval(input("\n【总产量】(pcs): ")))
      self.numper1 = round(eval(input("【分条数】: ")))
      #self.percentage= float(int(input('【合格率】(%):'))/100)
      self.length1 = float(eval(input("【单片长度】(mm): "))/1000)

    def coating(self,*args):
      pieces = math.ceil(self.total/self.numper1*1.01 )
      length2 =math.ceil(pieces*self.length1)
      print('\n【总大片数】:',pieces,'片')
      print('【总米数】:',length2,'米')
      print('【分条数】:',int(self.numper1),'条')
      self.roll = math.ceil(length2/365 )
      self.pieces2 = math.ceil(pieces/self.roll)
      print('【每卷片数】:',self.pieces2,'片')
      print('【卷数】: ',self.roll,'卷')
      print('【每卷米数】: '+str(math.ceil(length2/self.roll))+' '+'米\n')

    def scrapping_order(self):
      num= '{:.4f}'.format(uniform(0.0036, 0.0060))
      if num != 0.0050:
        scraps = int(int(self.total)*float(num))
      scrap = math.ceil(int(scraps)/self.numper1)*self.numper1
      scrap_rate=float(scrap/self.total)*100
      print('【报废清单】\n''【总产量】:',self.total,'pcs')
      print('【报废数】:',int(scrap),'pcs')
      print("【报废率】: {:.2f}%".format(scrap_rate))

    def roll_list(self):
      print('\n【分卷列表】')
      for i in range( 1, int(self.roll)+1):
        print('【第'+str(i)+'卷】:',int(self.pieces2)*i,'片')
      #dur = time.perf_counter() - start
    def __call__(self):
      #print('\n'+'♥️'*3+"下个型号"+'♥️'*3)
      #print(datetime.now())
      print ('\n♥️'+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'♥️')

  yie = Yields()
  try:
    yie.input_num() # 输入
  except Exception:
    print("请输入正确格式！")
  else:
    yie.coating() # 涂布产量
    yie.scrapping_order() # 报废清单
    yie.roll_list()  # 分卷列表
  #yie.dividing_line()  # 分割线
  #finally:
    yie()
