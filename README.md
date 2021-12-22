# yield.py
#calculated yield
import math
from random import uniform

for i in range(10):
  try:
    total = int(eval(input("\n【总产量】(pcs): ")))
    numper1 = round(eval(input("【分条数】: ")))
    #percentage= float(int(input('【合格率】(%):'))/100)
    length1 = float(eval(input("【单片长度】(mm): "))/1000)
    
  except Exception:
    print("请输入数字！")
    
  else:
    pieces = math.ceil(total/numper1*1.01 )
    length2 =math.ceil(pieces*length1)
    print('\n【总大片数】:',pieces,'片')
    print('【总米数】:',length2,'米')
    print('【分条数】:',int(numper1),'条')
    roll = math.ceil(length2/360 )
    pieces2 = math.ceil(pieces/roll)
    print('【每卷片数】:',pieces2,'片')
    print('【卷数】: ',roll,'卷')
    print('【每卷米数】: '+str(math.ceil(length2/roll))+' '+'米\n')
    
    num= '{:.4f}'.format(uniform(0.0036, 0.0058))
    scraps = int(int(total)*float(num))
    scrap = math.ceil(int(scraps)/numper1)*numper1
    scrap_rate=float(scrap/total)*100
    
    print('【报废清单】\n''【总产量】:',total,'pcs')
    print('【报废数】:',int(scrap),'pcs')
    print("【报废率】: {:.2f}%".format(scrap_rate))
    #print("【报废率】:",round(scrap_rate,2),'%\n')
    
    print('\n【分卷列表】')
    for i in range( 1, int(roll)+1):
      print('【第'+str(i)+'卷】:',int(pieces2)*i,'片')
#  2021-11-8 04:06 TAN.
    print('\n'+'♥️'*3+"下个型号"+'♥️'*3)
