import time, os, datetime

count = 0
img_list = []

#name - name of the photo, num is the iteration
def take_photo(interval, name, num):
	print(name + " " + str(num))
	cur_dir = os.getcwd()
	time = datetime.datetime.now()
	os.system("fswebcam -r 640x480 --no-banner " + cur_dir + "/photos/" + name + str(num) + '-' + str(time.year) + '-' + str(time.month) + '-' + str(time.day))
	img_list.extend(name + str(num) + '-' + str(time.year) + '-' + str(time.month) + '-' + str(time.day))
	time.sleep(interval)



while True:
	count = count + 1
	take_photo(3, 'boat', count)
