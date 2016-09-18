import time, os, datetime, shutil

count = 0

#name - name of the photo, num is the iteration
def take_photo(interval, name, num):
	cur_dir = os.getcwd()
	cur_time = datetime.datetime.now()
	cur_img = cur_dir + "/photos/" + name + str(num) + '-' + str(cur_time.year) + '-' + str(cur_time.month) + '-' + str(cur_time.day) + '.jpg'

	#Stores all photos created in a photos folder.
	os.system("fswebcam -r 640x480 --no-banner " + cur_img)
	
	#Creates a copy of the current photo to serve up as the homepage image.
	shutil.copy2(cur_img, cur_dir + '/boat-life.jpg')

	time.sleep(interval)
#end take_photo


while True:
	count = count + 1
	take_photo(3, 'boat', count)
