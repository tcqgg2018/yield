#♥️涂布面密度展示图表

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import mlab
from matplotlib import rcParams

#设置显示器size
fig = plt.figure(dpi=256,figsize=(10, 18))
plt.style.use('bmh')
#while True:
try:
	
		y1 = list(map(float,input('头部面密度:').split(',')))
		y2 = list(map(float,input('中间面密度:').split(',')))
		y3 = list(map(float,input('尾部面密度:').split(',')))
		
except (ValueError,RuntimeError, TypeError, NameError):
		print('请重新输入正确格式！')
else:
		n1 = len(y1)
		n2 = len(y2)
		n3 = len(y3)
	
	#♦️头部面密度
		plt.subplot(3,1,1)
		mean1 = sum(y1)/n1
		mean2 = sum(y2)/n2
		mean3 = sum(y3)/n3
		means = sum(y1+y2+y3)/(n1+n2+n3)
		#直方图📊
		rects1 =plt.bar(left = range(1,n1*2,2),height =y1,label='{:.1f}'.format(mean1),color=('r','g','y'),edgecolor = 'white',width = 1.5,align="center")
		#标题
		plt.title('Surface density reference chart',fontsize=28)
		plt.ylabel('Head',fontsize=23)
		#个个图上显示数字
		def autolabel(rects1):
			for rect in rects1:
				height = rect.get_height()
				plt.text(rect.get_x()+rect.get_width()/5., 1.03*height, '%s' % int(height),fontsize=18)
		autolabel(rects1)
	# 直方图上垂直显示数据
#def autolabel(rects1,Num=1.03,rotation1=90,NN=1):
#for rect in rects1:
#height = rect.get_height()
#plt.text(rect.get_x()-0.04+rect.get_width()/2., Num*height, '%s'%float(height*NN),rotation=rotation1)
	#autolabel(rects1,1.09)
		plt.xticks((range(1,n1*2+2,2)),(range(1,n1+2)))
		plt.ylim(0,max(y1)*1.5)
		plt.legend()
		#设置刻度标记的大小
		plt.tick_params(axis='both',which='major',labelsize=20)
	
		# ♦️中间面密度
		plt.subplot(3,1,2)
		rects2 =plt.bar(left = range(1,n2*2,2),height =y2,label='{:.1f}'.format(mean2),color=('y','g','#6c671a','#6cd91a'),width = 1.5,align="center")
		plt.ylabel('Middle',fontsize=23)
		def autolabel(rects2):
			for rect in rects2:
				height = rect.get_height()
				plt.text(rect.get_x()+rect.get_width()/5., 1.03*height, '%s' % int(height),fontsize=18)
		autolabel(rects2)
		plt.xticks((range(1,n2*2,2)),(range(1,n2+1)))
		plt.ylim(0,max(y2)*1.5)
		plt.legend()
		#设置刻度标记的大小
		plt.tick_params(axis='both',which='major',labelsize=20)
	
	#♦️尾部面密度
		plt.subplot(3,1,3)
		rects3 =plt.bar(left = range(1,n3*2,2),height =y3,label='{:.1f}'.format(mean3),color=('g','#e89c9e','#e8469e','#79469e'),width = 1.5,align="center")
		plt.ylabel('Tail',fontsize=23)
		def autolabel(rects3):
			for rect in rects3:
				height = rect.get_height()
				plt.text(rect.get_x()+rect.get_width()/4., 1.03*height, '%s' % int(height),fontsize=18)
		autolabel(rects3)
		plt.xticks((range(1,n3*2,2)),(range(1,n3+1)))
		plt.ylim(0,max(y3)*1.5)
		plt.legend()
		plt.xlabel('Density average:'+str(round(means,1)),fontsize=24)
	#设置刻度标记的大小
		plt.tick_params(axis='both',which='major',labelsize=20)
	
		plt.show()

