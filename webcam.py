import time, os, datetime

count = 0
img_list = []

#name - name of the photo, num is the iteration
def take_photo(interval, name, num):
	cur_dir = os.getcwd()
	cur_time = datetime.datetime.now()
	#Generates the photo that will display on the page.
	os.system("fswebcam -r 1024x768 --no-banner " + cur_dir + '/' + 'boat-life.jpg')
	#Stores all photos created in a photos folder.
	os.system("fswebcam -r 1024x768 --no-banner " + cur_dir + "/photos/" + name + str(num) + '-' + str(cur_time.year) + '-' + str(cur_time.month) + '-' + str(cur_time.day) + '.jpg')
	img_list.extend(name + str(num) + '-' + str(cur_time.year) + '-' + str(cur_time.month) + '-' + str(cur_time.day) + '.jpg')
	time.sleep(interval)
#end take_photo


while True:
	count = count + 1
	take_photo(3, 'boat', count)
