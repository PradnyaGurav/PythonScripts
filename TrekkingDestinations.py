#!/usr/bin/python

##need to work in EOF exception

try :
	while True:
		x = int(raw_input("Please enter an budget for trek: "))
		print 'READ:',x
		except EOFError as e:
		print e
		
		
x = raw_input("Please enter an budget for trek: ")
print "Amount : ", x
if x <= 0 :
	x = 0
	print('Kindly Enter the valid amount 500<=1500')
elif x ==500 : 
	print('Yay!! you can go to Garbet point ,Matheran')
elif x >= 600 & x<=1000 :
	print('You can trek to Karnala or Visapur')
elif x >= 1050 & x <= 1500 :
	print('You can trek to Kalsubai!! or train to Aandharband')
else :
	print('Yet manymore to come')